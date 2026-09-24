import { useEffect, useState } from "react";
import { Link, useParams } from "react-router";
import AppShell from "../components/AppShell";
import StatusIcon from "../components/StatusIcon";
import { getTrack, type TrackDetail } from "../features/syllabus/api/syllabusApi";

export default function TrackRoute() {
  const { trackSlug } = useParams<{ trackSlug: string }>();
  const [track, setTrack] = useState<TrackDetail | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!trackSlug) return;
    getTrack(trackSlug)
      .then(setTrack)
      .catch((err) => setError(err instanceof Error ? err.message : "Couldn't load track"));
  }, [trackSlug]);

  if (error) {
    return (
      <AppShell crumbs={[{ label: "Tracks", to: "/tracks" }]}>
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      </AppShell>
    );
  }

  if (!track) return <AppShell crumbs={[{ label: "Tracks", to: "/tracks" }]}>{null}</AppShell>;

  const completed = track.sections.filter((s) => s.status === "completed").length;
  const pct = track.sections.length > 0 ? Math.round((completed / track.sections.length) * 100) : 0;

  return (
    <AppShell crumbs={[{ label: "Tracks", to: "/tracks" }, { label: track.title }]}>
      <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", marginBottom: 22 }}>
        <div>
          <div className="page-eyebrow">Track</div>
          <h1 className="page-title" style={{ marginBottom: 0 }}>
            {track.title}
          </h1>
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
          <div className="progress-bar" style={{ width: 120 }}>
            <div className="progress-bar-fill" style={{ width: `${pct}%` }} />
          </div>
          <span className="muted mono">
            {completed} of {track.sections.length} complete
          </span>
        </div>
      </div>

      <div className="row-list">
        {track.sections.map((section) => (
          <Link
            key={section.id}
            to={`/tracks/${track.slug}/${section.slug}`}
            className="row-item"
            style={section.status === "in_progress" ? { background: "var(--accent-soft-bg)" } : undefined}
          >
            <StatusIcon status={section.status} />
            <div className="row-number">{section.number}</div>
            <div style={{ flexGrow: 1 }}>
              <div className="row-title">{section.title}</div>
              <div className="row-sub">
                {section.level ?? "—"}
                {section.est_time ? ` · ${section.est_time}` : ""}
              </div>
            </div>
            <span className={`pill pill-${section.status}`}>{section.status.replace("_", " ")}</span>
          </Link>
        ))}
      </div>
    </AppShell>
  );
}
