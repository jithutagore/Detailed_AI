-- Syllabus + user status schema (SQLite). Safe to re-run.
-- Soft deletes everywhere: uniqueness is enforced only among live rows (WHERE deleted_at IS NULL).

PRAGMA foreign_keys = ON;

-- ─────────────────────────── syllabus content ───────────────────────────
CREATE TABLE IF NOT EXISTS tracks (
    id          INTEGER PRIMARY KEY,
    slug        TEXT    NOT NULL,
    title       TEXT    NOT NULL,
    description TEXT,
    source_dir  TEXT    NOT NULL,
    sort_order  INTEGER NOT NULL DEFAULT 0,
    created_at  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at  TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS tracks_slug_uq ON tracks (slug) WHERE deleted_at IS NULL;

CREATE TABLE IF NOT EXISTS sections (
    id          INTEGER PRIMARY KEY,
    track_id    INTEGER NOT NULL REFERENCES tracks (id),
    number      TEXT    NOT NULL,
    slug        TEXT    NOT NULL,
    title       TEXT    NOT NULL,
    goal        TEXT,
    level       TEXT,
    est_time    TEXT,
    intro_md    TEXT,
    source_path TEXT    NOT NULL,
    sort_order  INTEGER NOT NULL DEFAULT 0,
    created_at  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at  TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS sections_track_slug_uq ON sections (track_id, slug) WHERE deleted_at IS NULL;
CREATE INDEX IF NOT EXISTS sections_track_idx ON sections (track_id);

CREATE TABLE IF NOT EXISTS subsections (
    id         INTEGER PRIMARY KEY,
    section_id INTEGER NOT NULL REFERENCES sections (id),
    kind       TEXT    NOT NULL CHECK (kind IN (
                   'topic', 'objectives', 'exercises', 'project', 'resources',
                   'definition_of_done', 'capstone', 'lab', 'pitfalls', 'other')),
    number     TEXT,
    slug       TEXT    NOT NULL,
    title      TEXT    NOT NULL,
    body_md    TEXT    NOT NULL DEFAULT '',
    sort_order INTEGER NOT NULL DEFAULT 0,
    created_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS subsections_section_slug_uq ON subsections (section_id, slug) WHERE deleted_at IS NULL;
CREATE INDEX IF NOT EXISTS subsections_section_idx ON subsections (section_id);

CREATE TABLE IF NOT EXISTS subsection_items (
    id            INTEGER PRIMARY KEY,
    subsection_id INTEGER NOT NULL REFERENCES subsections (id),
    kind          TEXT    NOT NULL CHECK (kind IN (
                      'objective', 'exercise', 'resource', 'done_criterion', 'checklist', 'point')),
    content       TEXT    NOT NULL,
    is_checkbox   INTEGER NOT NULL DEFAULT 0 CHECK (is_checkbox IN (0, 1)),
    sort_order    INTEGER NOT NULL DEFAULT 0,
    created_at    TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at    TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at    TEXT
);
CREATE INDEX IF NOT EXISTS subsection_items_subsection_idx ON subsection_items (subsection_id);

-- ─────────────────────────── users & status ───────────────────────────
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY,
    email         TEXT NOT NULL,
    username      TEXT NOT NULL,
    first_name    TEXT NOT NULL,
    last_name     TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    created_at    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at    TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS users_email_uq ON users (lower(email)) WHERE deleted_at IS NULL;
-- Deliberately NOT scoped to "WHERE deleted_at IS NULL": once a username is taken it stays
-- taken forever, even if the account is later soft-deleted, so it can never be reused.
CREATE UNIQUE INDEX IF NOT EXISTS users_username_uq ON users (lower(username));

CREATE TABLE IF NOT EXISTS user_section_status (
    id              INTEGER PRIMARY KEY,
    user_id         INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    section_id      INTEGER NOT NULL REFERENCES sections (id),
    status          TEXT    NOT NULL DEFAULT 'not_started' CHECK (status IN (
                        'not_started', 'in_progress', 'completed', 'skipped', 'needs_revisit')),
    knowledge_level INTEGER CHECK (knowledge_level BETWEEN 1 AND 5),
    created_at      TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at      TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at      TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS user_section_status_uq
    ON user_section_status (user_id, section_id) WHERE deleted_at IS NULL;
CREATE INDEX IF NOT EXISTS user_section_status_section_idx ON user_section_status (section_id);

CREATE TABLE IF NOT EXISTS user_subsection_status (
    id              INTEGER PRIMARY KEY,
    user_id         INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    subsection_id   INTEGER NOT NULL REFERENCES subsections (id),
    status          TEXT    NOT NULL DEFAULT 'not_started' CHECK (status IN (
                        'not_started', 'in_progress', 'completed', 'skipped', 'needs_revisit')),
    knowledge_level INTEGER CHECK (knowledge_level BETWEEN 1 AND 5),
    created_at      TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at      TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at      TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS user_subsection_status_uq
    ON user_subsection_status (user_id, subsection_id) WHERE deleted_at IS NULL;
CREATE INDEX IF NOT EXISTS user_subsection_status_subsection_idx ON user_subsection_status (subsection_id);

-- ─────────────────────────── AI-generated notes ───────────────────────────
CREATE TABLE IF NOT EXISTS generated_notes (
    id            INTEGER PRIMARY KEY,
    user_id       INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    subsection_id INTEGER NOT NULL REFERENCES subsections (id),
    content_md    TEXT    NOT NULL,
    model_used    TEXT    NOT NULL,
    generated_at  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    edited_at     TEXT,
    created_at    TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at    TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deleted_at    TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS generated_notes_uq
    ON generated_notes (user_id, subsection_id) WHERE deleted_at IS NULL;
CREATE INDEX IF NOT EXISTS generated_notes_subsection_idx ON generated_notes (subsection_id);

-- ──────────────── updated_at maintenance (skipped when the caller sets it) ────────────────
CREATE TRIGGER IF NOT EXISTS tracks_set_updated_at AFTER UPDATE ON tracks
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE tracks SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS sections_set_updated_at AFTER UPDATE ON sections
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE sections SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS subsections_set_updated_at AFTER UPDATE ON subsections
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE subsections SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS subsection_items_set_updated_at AFTER UPDATE ON subsection_items
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE subsection_items SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS users_set_updated_at AFTER UPDATE ON users
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE users SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS user_section_status_set_updated_at AFTER UPDATE ON user_section_status
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE user_section_status SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS user_subsection_status_set_updated_at AFTER UPDATE ON user_subsection_status
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE user_subsection_status SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS generated_notes_set_updated_at AFTER UPDATE ON generated_notes
FOR EACH ROW WHEN NEW.updated_at IS OLD.updated_at
BEGIN
    UPDATE generated_notes SET updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now') WHERE id = NEW.id;
END;
