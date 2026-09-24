import { useState, type FormEvent } from "react";
import { Link } from "react-router";
import { registerUser, type User } from "../api/authApi";

type Props = {
  onSuccess: (user: User) => void;
};

const USERNAME_PATTERN = "[a-zA-Z0-9_]+";

export default function RegisterForm({ onSuccess }: Props) {
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (password !== confirmPassword) {
      setError("Passwords don't match");
      return;
    }
    setError(null);
    setSubmitting(true);
    try {
      onSuccess(await registerUser(username, firstName, lastName, email, password));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
      setSubmitting(false);
    }
  }

  return (
    <form className="auth-card" onSubmit={handleSubmit}>
      <h1>Create account</h1>
      {error && (
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      )}
      <div className="field">
        <label>
          Username
          <input
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            autoComplete="username"
            aria-describedby="username-hint"
            pattern={USERNAME_PATTERN}
            minLength={3}
            maxLength={30}
            required
          />
        </label>
        <span id="username-hint" className="hint">
          3–30 characters: letters, numbers, underscores. Cannot be changed later.
        </span>
      </div>
      <div className="name-row">
        <label>
          First name
          <input
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            autoComplete="given-name"
            maxLength={100}
            required
          />
        </label>
        <label>
          Last name
          <input
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            autoComplete="family-name"
            maxLength={100}
            required
          />
        </label>
      </div>
      <label>
        Email
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} autoComplete="email" required />
      </label>
      <div className="field">
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="new-password"
            aria-describedby="password-hint"
            minLength={8}
            maxLength={128}
            required
          />
        </label>
        <span id="password-hint" className="hint">
          At least 8 characters
        </span>
      </div>
      <label>
        Confirm password
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          autoComplete="new-password"
          minLength={8}
          maxLength={128}
          required
        />
      </label>
      <button type="submit" disabled={submitting}>
        {submitting ? "Creating account…" : "Create account"}
      </button>
      <p className="switch">
        Already have an account? <Link to="/login">Sign in</Link>
      </p>
    </form>
  );
}
