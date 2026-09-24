import { useEffect, useState } from "react";
import { Link } from "react-router";
import { ApiError } from "../../../lib/apiClient";
import { getNotes } from "../api/notesApi";

type Props = {
  trackSlug: string;
  sectionSlug: string;
  subsectionSlug: string;
};

export default function NotesCta({ trackSlug, sectionSlug, subsectionSlug }: Props) {
  const [hasNotes, setHasNotes] = useState<boolean | null>(null);

  useEffect(() => {
    let cancelled = false;
    getNotes(trackSlug, sectionSlug, subsectionSlug)
      .then(() => !cancelled && setHasNotes(true))
      .catch((err) => {
        if (cancelled) return;
        setHasNotes(err instanceof ApiError && err.status === 404 ? false : null);
      });
    return () => {
      cancelled = true;
    };
  }, [trackSlug, sectionSlug, subsectionSlug]);

  return (
    <Link to={`/tracks/${trackSlug}/${sectionSlug}/${subsectionSlug}/notes`} className="notes-cta">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true" style={{ flexShrink: 0 }}>
        <path d="M12 2 9.5 9.5 2 12l7.5 2.5L12 22l2.5-7.5L22 12l-7.5-2.5z" fill="currentColor" />
      </svg>
      <div>
        <div className="notes-cta-title">{hasNotes ? "View detailed notes" : "Generate detailed notes"}</div>
        <div className="notes-cta-sub">AI-written, editable, yours to keep</div>
      </div>
    </Link>
  );
}
