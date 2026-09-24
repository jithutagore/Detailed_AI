import { useState } from "react";
import type { LoginResponse } from "../api/authApi";
import { clearSession, loadSession, saveSession, type Session } from "../../../lib/session";

export function useSession() {
  const [session, setSession] = useState<Session | null>(loadSession);

  function signIn(login: LoginResponse) {
    setSession(saveSession(login));
  }

  function signOut() {
    clearSession();
    setSession(null);
  }

  return { session, signIn, signOut };
}
