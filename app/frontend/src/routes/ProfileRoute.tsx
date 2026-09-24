import AppShell from "../components/AppShell";
import ProfileForm from "../features/profile/components/ProfileForm";

export default function ProfileRoute() {
  return (
    <AppShell crumbs={[{ label: "Profile" }]}>
      <ProfileForm />
    </AppShell>
  );
}
