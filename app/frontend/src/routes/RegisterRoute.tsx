import { useNavigate } from "react-router";
import RegisterForm from "../features/auth/components/RegisterForm";
import type { User } from "../features/auth/api/authApi";

export default function RegisterRoute() {
  const navigate = useNavigate();

  function handleSuccess(user: User) {
    navigate("/login", { state: { registeredIdentifier: user.username } });
  }

  return (
    <main className="auth-page">
      <RegisterForm onSuccess={handleSuccess} />
    </main>
  );
}
