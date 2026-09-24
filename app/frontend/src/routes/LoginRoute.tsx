import { Navigate, useLocation, useNavigate } from "react-router";
import LoginForm from "../features/auth/components/LoginForm";
import { useSession } from "../features/auth/hooks/useSession";

export default function LoginRoute() {
  const location = useLocation();
  const navigate = useNavigate();
  const registeredIdentifier = (location.state as { registeredIdentifier?: string } | null)?.registeredIdentifier;
  const { session, signIn } = useSession();

  if (session) return <Navigate to="/tracks" replace />;

  return (
    <main className="auth-page">
      <LoginForm
        initialIdentifier={registeredIdentifier}
        showRegisteredNotice={Boolean(registeredIdentifier)}
        onSuccess={(login) => {
          signIn(login);
          navigate("/tracks");
        }}
      />
    </main>
  );
}
