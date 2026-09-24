import { useEffect, useState } from "react";
import { Link } from "react-router";
import AppShell from "../components/AppShell";
import { listTracks, type TrackSummary } from "../features/syllabus/api/syllabusApi";

const BADGE_LABELS: Record<string, string> = {
  ml: "ML",
  deep_learning: "DL",
  llm_engineering: "LE",
  ai_agents: "AG",
};

export default function TracksRoute() {
  const [tracks, setTracks] = useState<TrackSummary[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    listTracks()
      .then(setTracks)
      .catch((err) => setError(err instanceof Error ? err.message : "Couldn't load tracks"));
  }, []);

  return (
    <AppShell>
      <div className="page-eyebrow">Your curriculum</div>
      <h1 className="page-title">Tracks</h1>
      <p className="page-subtitle">Pick a track to see its sections and your progress.</p>

      {error && (
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      )}

      {tracks && (
        <div className="track-grid">
          {tracks.map((track) => {
            const pct = track.section_count > 0 ? Math.round((track.completed_count / track.section_count) * 100) : 0;
            return (
              <Link key={track.id} to={`/tracks/${track.slug}`} className="track-card">
                <div className="track-card-head">
                  <div className="track-badge">{BADGE_LABELS[track.slug] ?? track.slug.slice(0, 2).toUpperCase()}</div>
                  <div className="track-fraction">
                    {track.completed_count} / {track.section_count}
                  </div>
                </div>
                <div className="track-card-title">{track.title}</div>
                <div className="track-card-desc">{track.description ?? ""}</div>
                <div className="progress-bar">
                  <div className="progress-bar-fill" style={{ width: `${pct}%` }} />
                </div>
              </Link>
            );
          })}
        </div>
      )}
    </AppShell>
  );
}
