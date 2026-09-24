type Props = {
  subsectionTitle: string;
  busy: boolean;
  onGenerate: () => void;
};

export default function NotesEmptyState({ subsectionTitle, busy, onGenerate }: Props) {
  return (
    <div className="notes-empty">
      <div className="notes-empty-icon" aria-hidden="true">
        ✦
      </div>
      <h2>No notes yet for this topic</h2>
      <p>
        Generate detailed, worked-through notes for <strong>{subsectionTitle}</strong> — Markdown,
        LaTeX math, and code included. You can edit anything afterward.
      </p>
      <button type="button" className="generate-btn" onClick={onGenerate} disabled={busy}>
        {busy ? "Generating…" : "Generate notes"}
      </button>
    </div>
  );
}
