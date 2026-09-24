import { useEffect, useState } from "react";
import { useParams } from "react-router";
import AppShell from "../components/AppShell";
import { getSubsection, type SubsectionDetail } from "../features/syllabus/api/syllabusApi";
import { setSubsectionStatus } from "../features/progress/api/progressApi";
import { useStatus } from "../features/progress/hooks/useStatus";
import StatusControl from "../features/progress/components/StatusControl";
import NotesCta from "../features/notes/components/NotesCta";

const KIND_LABELS: Record<string, string> = {
  topic: "Topic",
  objectives: "Objectives",
  exercises: "Exercises",
  project: "Project",
  resources: "Resources",
  definition_of_done: "Done",
  capstone: "Capstone",
  lab: "Lab",
  pitfalls: "Pitfalls",
  other: "Other",
};

function SubsectionBody({
  trackSlug,
  sectionSlug,
  subsectionSlug,
  subsection,
}: {
  trackSlug: string;
  sectionSlug: string;
  subsectionSlug: string;
  subsection: SubsectionDetail;
}) {
  const status = useStatus(subsection.status, subsection.knowledge_level);
  const bulletLines = subsection.body_md
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
  const checkboxItems = subsection.items.filter((item) => item.is_checkbox);

  return (
    <AppShell
      crumbs={[
        { label: "Tracks", to: "/tracks" },
        { label: trackSlug, to: `/tracks/${trackSlug}` },
        { label: sectionSlug, to: `/tracks/${trackSlug}/${sectionSlug}` },
        { label: `${subsection.number ?? ""} ${subsection.title}`.trim() },
      ]}
    >
      <div className="detail-layout">
        <div className="detail-main" style={{ maxWidth: 720 }}>
          <div className="page-eyebrow">
            {subsection.number ? `${subsection.number} · ` : ""}
            {KIND_LABELS[subsection.kind] ?? subsection.kind}
          </div>
          <h1 className="page-title">{subsection.title}</h1>

          {bulletLines.length > 0 && (
            <ul className="body-md" style={{ paddingLeft: 20, marginBottom: 28 }}>
              {bulletLines.map((line, i) => (
                <li key={i} style={{ marginBottom: 8 }}>
                  {line.replace(/^[-*+]\s*/, "")}
                </li>
              ))}
            </ul>
          )}

          {checkboxItems.length > 0 && (
            <>
              <div className="status-control-label" style={{ marginBottom: 12 }}>
                Checklist
              </div>
              <div className="checklist">
                {checkboxItems.map((item) => (
                  <div key={item.id} className="checklist-item">
                    <div className="checklist-box" />
                    <div>{item.content}</div>
                  </div>
                ))}
              </div>
            </>
          )}
        </div>

        <div className="detail-sidebar">
          <div className="sidebar-card">
            <StatusControl
              status={status.status}
              knowledgeLevel={status.knowledgeLevel}
              saving={status.saving}
              error={status.error}
              onChange={(update) =>
                status.update(update, (u) => setSubsectionStatus(trackSlug, sectionSlug, subsectionSlug, u))
              }
            />
          </div>
          <NotesCta trackSlug={trackSlug} sectionSlug={sectionSlug} subsectionSlug={subsectionSlug} />
        </div>
      </div>
    </AppShell>
  );
}

export default function SubsectionRoute() {
  const { trackSlug, sectionSlug, subsectionSlug } = useParams<{
    trackSlug: string;
    sectionSlug: string;
    subsectionSlug: string;
  }>();
  const [subsection, setSubsection] = useState<SubsectionDetail | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!trackSlug || !sectionSlug || !subsectionSlug) return;
    setSubsection(null);
    getSubsection(trackSlug, sectionSlug, subsectionSlug)
      .then(setSubsection)
      .catch((err) => setError(err instanceof Error ? err.message : "Couldn't load subsection"));
  }, [trackSlug, sectionSlug, subsectionSlug]);

  if (error) {
    return (
      <AppShell crumbs={[{ label: "Tracks", to: "/tracks" }]}>
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      </AppShell>
    );
  }
  if (!subsection || !trackSlug || !sectionSlug || !subsectionSlug) {
    return <AppShell crumbs={[{ label: "Tracks", to: "/tracks" }]}>{null}</AppShell>;
  }

  return (
    <SubsectionBody
      key={subsection.id}
      trackSlug={trackSlug}
      sectionSlug={sectionSlug}
      subsectionSlug={subsectionSlug}
      subsection={subsection}
    />
  );
}
