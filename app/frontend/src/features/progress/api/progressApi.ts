import { apiPut } from "../../../lib/apiClient";

export type Status = "not_started" | "in_progress" | "completed" | "skipped" | "needs_revisit";

export type StatusUpdate = {
  status: Status;
  knowledge_level?: number | null;
};

export type StatusResult = {
  status: Status;
  knowledge_level: number | null;
  updated_at: string;
};

export const setSectionStatus = (trackSlug: string, sectionSlug: string, update: StatusUpdate) =>
  apiPut<StatusResult>(`/tracks/${trackSlug}/sections/${sectionSlug}/status`, update);

export const setSubsectionStatus = (
  trackSlug: string,
  sectionSlug: string,
  subsectionSlug: string,
  update: StatusUpdate,
) =>
  apiPut<StatusResult>(
    `/tracks/${trackSlug}/sections/${sectionSlug}/subsections/${subsectionSlug}/status`,
    update,
  );
