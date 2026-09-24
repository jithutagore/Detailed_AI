import { useState } from "react";
import MarkdownView from "./MarkdownView";
import type { Notes } from "../api/notesApi";

type Props = {
  notes: Notes;
  busy: boolean;
  onSave: (contentMd: string) => Promise<boolean>;
  onDownload: () => void;
  onRegenerate: () => void;
};

export default function NotesPanel({ notes, busy, onSave, onDownload, onRegenerate }: Props) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(notes.content_md);
  const [copied, setCopied] = useState(false);

  function startEditing() {
    setDraft(notes.content_md);
    setEditing(true);
  }

  async function handleSave() {
    if (await onSave(draft)) setEditing(false);
  }

  async function handleCopy() {
    await navigator.clipboard.writeText(notes.content_md);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  }

  const byline = notes.edited_at
    ? `Generated · ${notes.model_used} · edited`
    : `Generated · ${notes.model_used}`;

  return (
    <div className="notes-panel">
      <div className="notes-toolbar">
        <span className="notes-byline">{byline}</span>
        <div className="notes-actions">
          {editing ? (
            <>
              <button type="button" className="toolbar-btn" onClick={handleSave} disabled={busy}>
                Save
              </button>
              <button type="button" className="toolbar-btn" onClick={() => setEditing(false)} disabled={busy}>
                Cancel
              </button>
            </>
          ) : (
            <>
              <button type="button" className="toolbar-btn" onClick={startEditing}>
                Edit
              </button>
              <button type="button" className="toolbar-btn" onClick={handleCopy}>
                {copied ? "Copied" : "Copy"}
              </button>
              <button type="button" className="toolbar-btn" onClick={onDownload}>
                Download .md
              </button>
              <button type="button" className="toolbar-btn toolbar-btn-danger" onClick={onRegenerate} disabled={busy}>
                Regenerate
              </button>
            </>
          )}
        </div>
      </div>

      {editing ? (
        <textarea
          className="notes-editor"
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          disabled={busy}
        />
      ) : (
        <MarkdownView content={notes.content_md} />
      )}
    </div>
  );
}
