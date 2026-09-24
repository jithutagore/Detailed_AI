import { useState } from "react";
import type { Status, StatusUpdate } from "../api/progressApi";

export function useStatus(initialStatus: Status, initialKnowledgeLevel: number | null) {
  const [status, setStatus] = useState(initialStatus);
  const [knowledgeLevel, setKnowledgeLevel] = useState(initialKnowledgeLevel);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function update(next: StatusUpdate, save: (update: StatusUpdate) => Promise<{ status: Status; knowledge_level: number | null }>) {
    setSaving(true);
    setError(null);
    try {
      const result = await save(next);
      setStatus(result.status);
      setKnowledgeLevel(result.knowledge_level);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Couldn't save");
    } finally {
      setSaving(false);
    }
  }

  return { status, knowledgeLevel, saving, error, update };
}
