import { useEffect, useState } from "react";
import { ApiError } from "../../../lib/apiClient";
import { downloadNotes, generateNotes, getNotes, updateNotes, type Notes } from "../api/notesApi";

type Params = { trackSlug: string; sectionSlug: string; subsectionSlug: string };

export function useNotes({ trackSlug, sectionSlug, subsectionSlug }: Params) {
  const [notes, setNotes] = useState<Notes | null>(null);
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    getNotes(trackSlug, sectionSlug, subsectionSlug)
      .then((result) => {
        if (!cancelled) setNotes(result);
      })
      .catch((err) => {
        if (cancelled) return;
        if (err instanceof ApiError && err.status === 404) {
          setNotes(null);
        } else {
          setError(err instanceof Error ? err.message : "Couldn't load notes");
        }
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [trackSlug, sectionSlug, subsectionSlug]);

  async function generate() {
    setBusy(true);
    setError(null);
    try {
      setNotes(await generateNotes(trackSlug, sectionSlug, subsectionSlug));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Generation failed");
    } finally {
      setBusy(false);
    }
  }

  async function save(contentMd: string) {
    setBusy(true);
    setError(null);
    try {
      setNotes(await updateNotes(trackSlug, sectionSlug, subsectionSlug, contentMd));
      return true;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Couldn't save");
      return false;
    } finally {
      setBusy(false);
    }
  }

  async function download() {
    setError(null);
    try {
      const { blob, filename } = await downloadNotes(trackSlug, sectionSlug, subsectionSlug);
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = filename;
      link.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Download failed");
    }
  }

  return { notes, loading, busy, error, generate, save, download };
}
