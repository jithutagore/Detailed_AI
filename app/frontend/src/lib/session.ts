import type { LoginResponse, User } from "../features/auth/api/authApi";

export type Session = {
  token: string;
  expiresAt: number;
  user: User;
};

const STORAGE_KEY = "session";

export function saveSession(login: LoginResponse): Session {
  const session = {
    token: login.access_token,
    expiresAt: Date.now() + login.expires_in * 1000,
    user: login.user,
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(session));
  return session;
}

export function loadSession(): Session | null {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return null;
  const session = JSON.parse(raw) as Session;
  if (session.expiresAt <= Date.now()) {
    clearSession();
    return null;
  }
  return session;
}

export function clearSession() {
  localStorage.removeItem(STORAGE_KEY);
}
