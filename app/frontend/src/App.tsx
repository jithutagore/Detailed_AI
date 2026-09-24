import { BrowserRouter, Navigate, Route, Routes } from "react-router";
import LoginRoute from "./routes/LoginRoute";
import RegisterRoute from "./routes/RegisterRoute";
import TracksRoute from "./routes/TracksRoute";
import TrackRoute from "./routes/TrackRoute";
import SectionRoute from "./routes/SectionRoute";
import SubsectionRoute from "./routes/SubsectionRoute";
import NotesRoute from "./routes/NotesRoute";
import ProfileRoute from "./routes/ProfileRoute";
import AuthGuard from "./routes/AuthGuard";
import { loadSession } from "./lib/session";

function RootRedirect() {
  return <Navigate to={loadSession() ? "/tracks" : "/login"} replace />;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginRoute />} />
        <Route path="/register" element={<RegisterRoute />} />

        <Route
          path="/tracks"
          element={
            <AuthGuard>
              <TracksRoute />
            </AuthGuard>
          }
        />
        <Route
          path="/tracks/:trackSlug"
          element={
            <AuthGuard>
              <TrackRoute />
            </AuthGuard>
          }
        />
        <Route
          path="/tracks/:trackSlug/:sectionSlug"
          element={
            <AuthGuard>
              <SectionRoute />
            </AuthGuard>
          }
        />
        <Route
          path="/tracks/:trackSlug/:sectionSlug/:subsectionSlug"
          element={
            <AuthGuard>
              <SubsectionRoute />
            </AuthGuard>
          }
        />
        <Route
          path="/tracks/:trackSlug/:sectionSlug/:subsectionSlug/notes"
          element={
            <AuthGuard>
              <NotesRoute />
            </AuthGuard>
          }
        />
        <Route
          path="/profile"
          element={
            <AuthGuard>
              <ProfileRoute />
            </AuthGuard>
          }
        />

        <Route path="/" element={<RootRedirect />} />
        <Route path="*" element={<RootRedirect />} />
      </Routes>
    </BrowserRouter>
  );
}
