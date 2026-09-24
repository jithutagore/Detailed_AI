import type { Status, StatusUpdate } from "../api/progressApi";

const STATUS_OPTIONS: { value: Status; label: string }[] = [
  { value: "in_progress", label: "In progress" },
  { value: "completed", label: "Completed" },
  { value: "needs_revisit", label: "Needs revisit" },
  { value: "skipped", label: "Skipped" },
];

type Props = {
  status: Status;
  knowledgeLevel: number | null;
  saving: boolean;
  error: string | null;
  onChange: (update: StatusUpdate) => void;
};

export default function StatusControl({ status, knowledgeLevel, saving, error, onChange }: Props) {
  return (
    <div className="status-control">
      <div className="status-control-group">
        <div className="status-control-label">Status</div>
        <div className="status-buttons">
          {STATUS_OPTIONS.map((option) => (
            <button
              key={option.value}
              type="button"
              className={`status-btn${status === option.value ? " status-btn-active" : ""}`}
              disabled={saving}
              onClick={() => onChange({ status: option.value, knowledge_level: knowledgeLevel })}
            >
              {option.label}
            </button>
          ))}
        </div>
      </div>

      <div className="status-control-group">
        <div className="status-control-label">Confidence</div>
        <div className="confidence-meter">
          {[1, 2, 3, 4, 5].map((level) => (
            <button
              key={level}
              type="button"
              aria-label={`Confidence ${level} of 5`}
              className={`confidence-cell${knowledgeLevel !== null && level <= knowledgeLevel ? " confidence-cell-filled" : ""}`}
              disabled={saving}
              onClick={() => onChange({ status, knowledge_level: level === knowledgeLevel ? null : level })}
            />
          ))}
        </div>
      </div>

      {error && (
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
