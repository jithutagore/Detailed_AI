import { useState, type FormEvent } from "react";
import { Link } from "react-router";
import { loginUser, type LoginResponse } from "../api/authApi";

type Props = {
  initialIdentifier?: string;
  showRegisteredNotice?: boolean;
  onSuccess: (login: LoginResponse) => void;
};

export default function LoginForm({ initialIdentifier = "", showRegisteredNotice, onSuccess }: Props) {
  const [identifier, setIdentifier] = useState(initialIdentifier);
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);
    setSubmitting(true);
    try {
      const login = await loginUser(identifier, password);
      setPassword("");
      onSuccess(login);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form className="auth-card" onSubmit={handleSubmit}>
      <h1>Sign in</h1>
      {showRegisteredNotice && !error && (
        <p className="alert alert-success" role="status">
          Account created. Sign in to continue.
        </p>
      )}
      {error && (
        <p className="alert alert-error" role="alert">
          {error}
        </p>
      )}
      <label>
        Email or username
        <input
          value={identifier}
          onChange={(e) => setIdentifier(e.target.value)}
          autoComplete="username"
          required
        />
      </label>
      <label>
        Password
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          autoComplete="current-password"
          maxLength={128}
          required
        />
      </label>
      <button type="submit" disabled={submitting}>
        {submitting ? "Signing in…" : "Sign in"}
      </button>
      <p className="switch">
        New here? <Link to="/register">Create an account</Link>
      </p>
    </form>
  );
}
