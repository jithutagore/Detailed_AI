import type { Status } from "../features/progress/api/progressApi";

const COLORS: Record<Status, string> = {
  completed: "#4b3fb0",
  in_progress: "#4b3fb0",
  needs_revisit: "#d8b23a",
  skipped: "#8a8371",
  not_started: "#c9c0ac",
};

export default function StatusIcon({ status }: { status: Status }) {
  const color = COLORS[status];

  if (status === "completed") {
    return (
      <svg className="status-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z" fill={color} />
      </svg>
    );
  }
  if (status === "in_progress") {
    return (
      <svg className="status-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <circle cx="12" cy="12" r="9" stroke={color} strokeWidth="2" strokeDasharray="34 22" />
      </svg>
    );
  }
  if (status === "needs_revisit") {
    return (
      <svg className="status-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <circle cx="12" cy="12" r="9" stroke={color} strokeWidth="2" strokeDasharray="4 3" />
      </svg>
    );
  }
  return (
    <svg className="status-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <circle cx="12" cy="12" r="9" stroke={color} strokeWidth="2" />
    </svg>
  );
}
