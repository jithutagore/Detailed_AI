import { useParams } from "react-router";
import AppShell from "../components/AppShell";
import { useNotes } from "../features/notes/hooks/useNotes";
import NotesPanel from "../features/notes/components/NotesPanel";
import NotesEmptyState from "../features/notes/components/NotesEmptyState";

export default function NotesRoute() {
  const { trackSlug, sectionSlug, subsectionSlug } = useParams<{
    trackSlug: string;
    sectionSlug: string;
    subsectionSlug: string;
  }>();

  const { notes, loading, busy, error, generate, save, download } = useNotes({
    trackSlug: trackSlug ?? "",
    sectionSlug: sectionSlug ?? "",
    subsectionSlug: subsectionSlug ?? "",
  });

  if (!trackSlug || !sectionSlug || !subsectionSlug) return null;

  return (
    <AppShell
      crumbs={[
        { label: `${sectionSlug} / ${subsectionSlug}`, to: `/tracks/${trackSlug}/${sectionSlug}/${subsectionSlug}` },
        { label: "Notes" },
      ]}
    >
      {error && (
        <p className="alert alert-error" role="alert" style={{ marginBottom: 20 }}>
          {error}
        </p>
      )}

      {!loading && !notes && (
        <NotesEmptyState subsectionTitle={subsectionSlug.replace(/-/g, " ")} busy={busy} onGenerate={generate} />
      )}

      {notes && <NotesPanel notes={notes} busy={busy} onSave={save} onDownload={download} onRegenerate={generate} />}
    </AppShell>
  );
}
