"""Load the markdown syllabus into the local SQLite database (db/syllabus.db).

Safe to re-run after editing the syllabus: existing rows are matched and updated in
place, removed content is soft-deleted (deleted_at), and re-added content is restored,
so user status rows stay attached to their subsections.
"""
import argparse
import re
import sqlite3
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

DB_DIR = Path(__file__).resolve().parent
REPO_ROOT = DB_DIR.parent
SCHEMA_PATH = DB_DIR / "schema.sql"
DEFAULT_DB_PATH = DB_DIR / "syllabus.db"

TRACK_ORDER = ["ML", "Deep_Learning", "LLM_Engineering", "AI_Agents"]
NOW_SQL = "strftime('%Y-%m-%dT%H:%M:%fZ', 'now')"

SECTION_DIR_RE = re.compile(r"^(\d{2})_(\w+)$")
TOPIC_HEADING_RE = re.compile(r"^(\d+\.\d+[a-z]?)\s+(.*)$")
LIST_ITEM_RE = re.compile(r"^([-*+]|\d+[.)])\s+(.*)$")
CHECKBOX_RE = re.compile(r"^\[[ xX]\]\s+(.*)$", re.DOTALL)
GOAL_RE = re.compile(r"^>\s*\*\*Goal:\*\*\s*(.+)$")
META_PART_RE = re.compile(r"^\*\*([^*:]+):\*\*\s*(.*)$")

SUBSECTION_KIND_RULES = [
    (re.compile(r"^learning objectives$"), "objectives"),
    (re.compile(r"^hands-on exercises$"), "exercises"),
    (re.compile(r"^(mini |stretch |capstone-prep )?project$"), "project"),
    (re.compile(r"^(recommended )?(resources|reading)$|^key papers"), "resources"),
    (re.compile(r"^definition of done$"), "definition_of_done"),
    (re.compile(r"^capstone \d+$"), "capstone"),
    (re.compile(r"^lab \d+$"), "lab"),
    (re.compile(r"^common pitfalls$"), "pitfalls"),
]

ITEM_KIND_BY_SUBSECTION_KIND = {
    "objectives": "objective",
    "exercises": "exercise",
    "resources": "resource",
    "definition_of_done": "done_criterion",
}

CHILD_TABLE = {
    "tracks": ("sections", "track_id"),
    "sections": ("subsections", "section_id"),
    "subsections": ("subsection_items", "subsection_id"),
}


@dataclass
class Node:
    row: dict
    children: list = field(default_factory=list)


# ───────────────────────────── parsing ─────────────────────────────

def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "untitled"


def clean_md(lines):
    text = "\n".join(lines).strip()
    text = re.sub(r"^(---\s*)+", "", text)
    text = re.sub(r"(\s*---)+$", "", text)
    return text.strip()


def split_on_h2(lines):
    blocks = [(None, [])]
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            blocks.append((line[3:].strip(), []))
        else:
            blocks[-1][1].append(line)
    return blocks


def classify_heading(heading):
    topic = TOPIC_HEADING_RE.match(heading)
    if topic:
        number, title = topic.groups()
        return "topic", number, title, slugify(title)
    base = re.sub(r"\s*\(.*\)$", "", heading.split(" — ")[0]).strip()
    kind = next((k for rx, k in SUBSECTION_KIND_RULES if rx.match(base.lower())), "other")
    return kind, None, heading, slugify(base)


def parse_items(lines, subsection_kind):
    raw_items, current, in_fence = [], None, False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence, current = not in_fence, None
            continue
        if in_fence:
            continue
        match = LIST_ITEM_RE.match(line)
        if match:
            current = [match.group(2)]
            raw_items.append(current)
        elif current is not None and line.strip() and line[0] in " \t":
            current.append(line.rstrip())
        elif line.strip():
            current = None

    items = []
    for position, parts in enumerate(raw_items):
        content = "\n".join(parts).strip()
        checkbox = CHECKBOX_RE.match(content)
        if checkbox:
            content = checkbox.group(1)
        kind = ITEM_KIND_BY_SUBSECTION_KIND.get(subsection_kind) or ("checklist" if checkbox else "point")
        items.append(Node({
            "kind": kind,
            "content": content,
            "is_checkbox": int(bool(checkbox)),
            "sort_order": position,
        }))
    return items


def parse_section(path, root, sort_order):
    number, slug = SECTION_DIR_RE.match(path.parent.name).groups()
    lines = path.read_text(encoding="utf-8").splitlines()
    (_, preamble), *blocks = split_on_h2(lines)

    h1_index = next((i for i, l in enumerate(preamble) if l.startswith("# ")), None)
    h1 = preamble.pop(h1_index)[2:].strip() if h1_index is not None else slug.replace("_", " ")
    title = re.sub(r"^\d{2}\s*[—-]\s*", "", h1)

    goal = level = est_time = None
    for line in preamble:
        if goal_match := GOAL_RE.match(line.strip()):
            goal = goal_match.group(1).strip()
        if line.startswith("**Level:**"):
            meta = {}
            for part in line.split(" · "):
                if part_match := META_PART_RE.match(part.strip()):
                    meta[part_match.group(1).strip().lower()] = part_match.group(2).strip()
            level, est_time = meta.get("level"), meta.get("time")

    subsections, seen_slugs = [], Counter()
    for position, (heading, body) in enumerate(blocks):
        kind, sub_number, sub_title, sub_slug = classify_heading(heading)
        seen_slugs[sub_slug] += 1
        if seen_slugs[sub_slug] > 1:
            sub_slug = f"{sub_slug}-{seen_slugs[sub_slug]}"
        subsections.append(Node({
            "kind": kind,
            "number": sub_number,
            "slug": sub_slug,
            "title": sub_title,
            "body_md": clean_md(body),
            "sort_order": position,
        }, parse_items(body, kind)))

    return Node({
        "number": number,
        "slug": slug,
        "title": title,
        "goal": goal,
        "level": level,
        "est_time": est_time,
        "intro_md": clean_md(preamble),
        "source_path": path.relative_to(root).as_posix(),
        "sort_order": sort_order,
    }, subsections), h1


def parse_tracks(root):
    track_dirs = []
    for directory in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        section_files = [
            sub / f"{sub.name}.md"
            for sub in sorted(directory.iterdir())
            if sub.is_dir() and SECTION_DIR_RE.match(sub.name) and (sub / f"{sub.name}.md").is_file()
        ]
        if section_files:
            track_dirs.append((directory, section_files))

    rank = {name: i for i, name in enumerate(TRACK_ORDER)}
    track_dirs.sort(key=lambda t: (rank.get(t[0].name, len(TRACK_ORDER)), t[0].name))

    tracks = []
    for position, (directory, section_files) in enumerate(track_dirs):
        sections, title, description = [], directory.name.replace("_", " "), None
        for section_position, path in enumerate(section_files):
            section, h1 = parse_section(path, root, section_position)
            sections.append(section)
            if section.row["number"] == "00":
                title = h1.split(" — ")[0].strip()
                paragraphs = [p for p in section.row["intro_md"].split("\n\n") if p.strip()]
                description = paragraphs[0].strip() if paragraphs else None
        tracks.append(Node({
            "slug": directory.name.lower(),
            "title": title,
            "description": description,
            "source_dir": directory.name,
            "sort_order": position,
        }, sections))
    return tracks


# ───────────────────────────── syncing ─────────────────────────────

def reconcile(conn, table, parent_col, parent_id, nodes, key, fallback, stats):
    """Sync one parent's children with `nodes`. Returns (ids aligned with nodes, soft-deleted ids)."""
    where, params = (f"{parent_col} = ?", (parent_id,)) if parent_col else ("1 = 1", ())
    existing = [dict(r) for r in conn.execute(
        f"SELECT * FROM {table} WHERE {where} ORDER BY deleted_at IS NOT NULL, deleted_at DESC", params)]
    live = [r for r in existing if r["deleted_at"] is None]
    dead = [r for r in existing if r["deleted_at"] is not None]

    matched, used = [None] * len(nodes), set()

    def claim(pool, keyfn):
        index = {}
        for r in pool:
            k = keyfn(r)
            if r["id"] not in used and k is not None:
                index.setdefault(k, r)
        for i, node in enumerate(nodes):
            k = keyfn(node.row)
            if matched[i] is None and k is not None and k in index and index[k]["id"] not in used:
                matched[i] = index[k]
                used.add(index[k]["id"])

    claim(live, key)
    claim(dead, key)
    if fallback:
        claim(live, fallback)

    gone = [r["id"] for r in live if r["id"] not in used]
    if gone:
        conn.executemany(f"UPDATE {table} SET deleted_at = {NOW_SQL} WHERE id = ?", [(i,) for i in gone])
        stats[table]["deleted"] += len(gone)

    ids = []
    for node, row in zip(nodes, matched):
        if row is None:
            values = dict(node.row, **({parent_col: parent_id} if parent_col else {}))
            cursor = conn.execute(
                f"INSERT INTO {table} ({', '.join(values)}) VALUES ({', '.join('?' * len(values))})",
                tuple(values.values()))
            ids.append(cursor.lastrowid)
            stats[table]["inserted"] += 1
            continue

        changed = {c: v for c, v in node.row.items() if row[c] != v}
        if changed or row["deleted_at"] is not None:
            assignments = [f"{c} = ?" for c in changed] + ["deleted_at = NULL"]
            conn.execute(f"UPDATE {table} SET {', '.join(assignments)} WHERE id = ?",
                         (*changed.values(), row["id"]))
            stats[table]["restored" if row["deleted_at"] is not None else "updated"] += 1
        ids.append(row["id"])
    return ids, gone


def cascade_soft_delete(conn, table, ids, stats):
    while table in CHILD_TABLE and ids:
        child, fk = CHILD_TABLE[table]
        marks = ", ".join("?" * len(ids))
        child_ids = [r[0] for r in conn.execute(
            f"SELECT id FROM {child} WHERE deleted_at IS NULL AND {fk} IN ({marks})", ids)]
        if child_ids:
            conn.execute(f"UPDATE {child} SET deleted_at = {NOW_SQL} WHERE id IN ({', '.join('?' * len(child_ids))})",
                         child_ids)
            stats[child]["deleted"] += len(child_ids)
        table, ids = child, child_ids


def sync(conn, tracks, stats):
    by_slug = lambda r: r["slug"]
    by_number = lambda r: r["number"]
    by_content = lambda r: " ".join(r["content"].split()).lower()
    by_position = lambda r: r["sort_order"]

    track_ids, gone = reconcile(conn, "tracks", None, None, tracks, by_slug, None, stats)
    cascade_soft_delete(conn, "tracks", gone, stats)
    for track, track_id in zip(tracks, track_ids):
        section_ids, gone = reconcile(conn, "sections", "track_id", track_id, track.children,
                                      by_slug, by_number, stats)
        cascade_soft_delete(conn, "sections", gone, stats)
        for section, section_id in zip(track.children, section_ids):
            subsection_ids, gone = reconcile(conn, "subsections", "section_id", section_id, section.children,
                                             by_slug, by_number, stats)
            cascade_soft_delete(conn, "subsections", gone, stats)
            for subsection, subsection_id in zip(section.children, subsection_ids):
                reconcile(conn, "subsection_items", "subsection_id", subsection_id, subsection.children,
                          by_content, by_position, stats)


# ───────────────────────────── entry point ─────────────────────────────

def print_parse_summary(tracks):
    kinds = Counter(sub.row["kind"] for t in tracks for s in t.children for sub in s.children)
    item_kinds = Counter(i.row["kind"] for t in tracks for s in t.children for sub in s.children for i in sub.children)
    for t in tracks:
        subs = sum(len(s.children) for s in t.children)
        items = sum(len(sub.children) for s in t.children for sub in s.children)
        print(f"{t.row['source_dir']:<16} sections={len(t.children):<3} subsections={subs:<4} items={items}")
    print("subsection kinds:", dict(kinds))
    print("item kinds:      ", dict(item_kinds))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help="SQLite file (default: db/syllabus.db)")
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="folder containing the track folders")
    parser.add_argument("--dry-run", action="store_true", help="parse and print counts without touching the database")
    args = parser.parse_args()

    tracks = parse_tracks(args.root.resolve())
    print_parse_summary(tracks)
    if args.dry_run:
        return

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    stats = defaultdict(Counter)
    with conn:
        sync(conn, tracks, stats)
    conn.close()

    print(f"\n{'table':<18}{'inserted':>9}{'updated':>9}{'restored':>9}{'deleted':>9}")
    for table in ("tracks", "sections", "subsections", "subsection_items"):
        s = stats[table]
        print(f"{table:<18}{s['inserted']:>9}{s['updated']:>9}{s['restored']:>9}{s['deleted']:>9}")
    print(f"\ndatabase: {args.db}")


if __name__ == "__main__":
    main()
