import { apiGet } from "../../../lib/apiClient";
import type { Status } from "../../progress/api/progressApi";

export type TrackSummary = {
  id: number;
  slug: string;
  title: string;
  description: string | null;
  section_count: number;
  completed_count: number;
};

export type SectionSummary = {
  id: number;
  number: string;
  slug: string;
  title: string;
  level: string | null;
  est_time: string | null;
  status: Status;
  knowledge_level: number | null;
};

export type TrackDetail = {
  id: number;
  slug: string;
  title: string;
  description: string | null;
  sections: SectionSummary[];
};

export type SubsectionSummary = {
  id: number;
  kind: string;
  number: string | null;
  slug: string;
  title: string;
  status: Status;
  knowledge_level: number | null;
};

export type SectionDetail = {
  id: number;
  number: string;
  slug: string;
  title: string;
  goal: string | null;
  level: string | null;
  est_time: string | null;
  intro_md: string | null;
  subsections: SubsectionSummary[];
  status: Status;
  knowledge_level: number | null;
};

export type SubsectionItem = {
  id: number;
  kind: string;
  content: string;
  is_checkbox: boolean;
};

export type SubsectionDetail = {
  id: number;
  kind: string;
  number: string | null;
  slug: string;
  title: string;
  body_md: string;
  items: SubsectionItem[];
  status: Status;
  knowledge_level: number | null;
};

export const listTracks = () => apiGet<TrackSummary[]>("/tracks");

export const getTrack = (trackSlug: string) => apiGet<TrackDetail>(`/tracks/${trackSlug}`);

export const getSection = (trackSlug: string, sectionSlug: string) =>
  apiGet<SectionDetail>(`/tracks/${trackSlug}/sections/${sectionSlug}`);

export const getSubsection = (trackSlug: string, sectionSlug: string, subsectionSlug: string) =>
  apiGet<SubsectionDetail>(
    `/tracks/${trackSlug}/sections/${sectionSlug}/subsections/${subsectionSlug}`,
  );
