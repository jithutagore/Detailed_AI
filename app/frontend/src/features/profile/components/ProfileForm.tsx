import { useEffect, useState, type FormEvent } from "react";
import { getProfile, updateProfile, type Profile } from "../api/profileApi";

export default function ProfileForm() {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    getProfile().then((p) => {
      setProfile(p);
      setFirstName(p.first_name);
      setLastName(p.last_name);
    });
  }, []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setSaving(true);
    setError(null);
    setSaved(false);
    try {
      setProfile(await updateProfile(firstName, lastName));
      setSaved(true);
      setTimeout(() => setSaved(false), 2000);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Couldn't save");
    } finally {
      setSaving(false);
    }
  }

  if (!profile) return null;

  return (
    <form className="auth-card" onSubmit={handleSubmit} style={{ maxWidth: 480 }}>
      <h1>Profile</h1>
      {error && (
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      )}
      {saved && (
        <p className="alert alert-success" role="status">
          Saved
        </p>
      )}
      <div className="name-row">
        <label>
          First name
          <input value={firstName} onChange={(e) => setFirstName(e.target.value)} maxLength={100} required />
        </label>
        <label>
          Last name
          <input value={lastName} onChange={(e) => setLastName(e.target.value)} maxLength={100} required />
        </label>
      </div>
      <label>
        Username
        <input value={profile.username} disabled />
      </label>
      <label>
        Email
        <input value={profile.email} disabled />
      </label>
      <button type="submit" disabled={saving}>
        {saving ? "Saving…" : "Save changes"}
      </button>
      <p className="hint">
        Username and email can't be changed once set — usernames stay permanently reserved, even if an
        account is deleted.
      </p>
    </form>
  );
}
