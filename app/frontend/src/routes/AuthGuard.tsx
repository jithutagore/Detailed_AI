import type { ReactNode } from "react";
import { Navigate } from "react-router";
import { loadSession } from "../lib/session";

export default function AuthGuard({ children }: { children: ReactNode }) {
  const session = loadSession();
  if (!session) return <Navigate to="/login" replace />;
  return children;
}
