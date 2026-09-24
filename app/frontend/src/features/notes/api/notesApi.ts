import { apiDownload, apiGet, apiPost, apiPut } from "../../../lib/apiClient";

export type Notes = {
  id: number;
  subsection_id: number;
  content_md: string;
  model_used: string;
  generated_at: string;
  edited_at: string | null;
};

function basePath(trackSlug: string, sectionSlug: string, subsectionSlug: string) {
  return `/tracks/${trackSlug}/sections/${sectionSlug}/subsections/${subsectionSlug}/notes`;
}

export const getNotes = (trackSlug: string, sectionSlug: string, subsectionSlug: string) =>
  apiGet<Notes>(basePath(trackSlug, sectionSlug, subsectionSlug));

export const generateNotes = (trackSlug: string, sectionSlug: string, subsectionSlug: string) =>
  apiPost<Notes>(`${basePath(trackSlug, sectionSlug, subsectionSlug)}/generate`);

export const updateNotes = (
  trackSlug: string,
  sectionSlug: string,
  subsectionSlug: string,
  contentMd: string,
) => apiPut<Notes>(basePath(trackSlug, sectionSlug, subsectionSlug), { content_md: contentMd });

export const downloadNotes = (trackSlug: string, sectionSlug: string, subsectionSlug: string) =>
  apiDownload(`${basePath(trackSlug, sectionSlug, subsectionSlug)}/download`);
