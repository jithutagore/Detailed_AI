import type { ReactNode } from "react";
import { Link } from "react-router";
import { loadSession } from "../lib/session";

type Crumb = { label: string; to?: string };

type Props = {
  crumbs?: Crumb[];
  children: ReactNode;
};

export default function AppShell({ crumbs, children }: Props) {
  const session = loadSession();
  const initials = session
    ? `${session.user.first_name[0] ?? ""}${session.user.last_name[0] ?? ""}`.toUpperCase()
    : "";

  return (
    <div className="app-shell">
      <div className="app-nav">
        <div className="app-nav-left">
          <Link to="/tracks" className="app-brand">
            Detailed AI
          </Link>
          {crumbs && crumbs.length > 0 && (
            <div className="breadcrumbs">
              {crumbs.map((crumb, i) => (
                <span key={i} className="breadcrumb-item">
                  {i > 0 && <span className="breadcrumb-sep">/</span>}
                  {crumb.to ? <Link to={crumb.to}>{crumb.label}</Link> : <span>{crumb.label}</span>}
                </span>
              ))}
            </div>
          )}
        </div>
        <Link to="/profile" className="app-avatar" aria-label="Profile">
          {initials}
        </Link>
      </div>
      <div className="app-content">{children}</div>
    </div>
  );
}
