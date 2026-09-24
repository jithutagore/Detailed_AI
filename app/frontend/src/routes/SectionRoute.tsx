import { useEffect, useState } from "react";
import { Link, useParams } from "react-router";
import AppShell from "../components/AppShell";
import { getSection, type SectionDetail } from "../features/syllabus/api/syllabusApi";
import { setSectionStatus } from "../features/progress/api/progressApi";
import { useStatus } from "../features/progress/hooks/useStatus";
import StatusControl from "../features/progress/components/StatusControl";

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

function SectionBody({ trackSlug, sectionSlug, section }: { trackSlug: string; sectionSlug: string; section: SectionDetail }) {
  const status = useStatus(section.status, section.knowledge_level);

  return (
    <AppShell
      crumbs={[
        { label: "Tracks", to: "/tracks" },
        { label: trackSlug, to: `/tracks/${trackSlug}` },
        { label: `${section.number} ${section.title}` },
      ]}
    >
      <div className="detail-layout">
        <div className="detail-main">
          <div className="page-eyebrow">
            Section {section.number} · {section.level ?? "—"}
            {section.est_time ? ` · ${section.est_time}` : ""}
          </div>
          <h1 className="page-title">{section.title}</h1>
          {section.goal && <p className="page-subtitle">{section.goal}</p>}

          <div className="status-control-label" style={{ marginBottom: 14 }}>
            Subsections
          </div>
          <div className="row-list">
            {section.subsections.map((sub) => (
              <Link key={sub.id} to={`/tracks/${trackSlug}/${sectionSlug}/${sub.slug}`} className="row-item">
                <div style={{ flexGrow: 1 }}>
                  <div className="row-title">
                    {sub.number ? `${sub.number} ` : ""}
                    {sub.title}
                  </div>
                </div>
                <span className="pill">{KIND_LABELS[sub.kind] ?? sub.kind}</span>
              </Link>
            ))}
          </div>
        </div>

        <div className="detail-sidebar">
          <div className="sidebar-card">
            <StatusControl
              status={status.status}
              knowledgeLevel={status.knowledgeLevel}
              saving={status.saving}
              error={status.error}
              onChange={(update) => status.update(update, (u) => setSectionStatus(trackSlug, sectionSlug, u))}
            />
          </div>
        </div>
      </div>
    </AppShell>
  );
}

export default function SectionRoute() {
  const { trackSlug, sectionSlug } = useParams<{ trackSlug: string; sectionSlug: string }>();
  const [section, setSection] = useState<SectionDetail | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!trackSlug || !sectionSlug) return;
    setSection(null);
    getSection(trackSlug, sectionSlug)
      .then(setSection)
      .catch((err) => setError(err instanceof Error ? err.message : "Couldn't load section"));
  }, [trackSlug, sectionSlug]);

  if (error) {
    return (
      <AppShell crumbs={[{ label: "Tracks", to: "/tracks" }]}>
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      </AppShell>
    );
  }
  if (!section || !trackSlug || !sectionSlug) {
    return <AppShell crumbs={[{ label: "Tracks", to: "/tracks" }]}>{null}</AppShell>;
  }

  // Keyed so the status control resets when navigating between sections.
  return <SectionBody key={section.id} trackSlug={trackSlug} sectionSlug={sectionSlug} section={section} />;
}
