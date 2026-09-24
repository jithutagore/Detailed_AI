# App

Website on top of `db/syllabus.db`, structured feature-by-feature for growth.

- `backend/` — FastAPI, layered (config → core → db → models → schemas → services → api/routes)
- `frontend/` — React + TypeScript (Vite), feature-oriented (`features/<name>/{api,hooks,components}`)

## Backend

```
cd backend
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.txt   # -r requirements.txt for prod-only
copy .env.example .env                                        # then edit SECRET_KEY at minimum
.venv/Scripts/python -m uvicorn app.main:app --reload --port 8000
```

Runs tests: `.venv/Scripts/python -m pytest`

### Layout
```
app/
  core/       config (env-driven Settings), logging, security (hashing/JWT), exceptions, middleware
  db/         SQLAlchemy engine/session, schema init (applies ../../db/schema.sql, the syllabus
              importer's source of truth for table shape)
  models/     SQLAlchemy ORM models (one file per table)
  schemas/    Pydantic request/response models, one file per feature
  services/   business logic — routes call services, services touch the db
  api/routes/ one file per feature; api/router.py wires them together
  main.py     app factory: middleware, CORS, exception handlers, router
tests/        pytest, one test file per feature
```
Adding a feature = one file in each of `models/` (if it needs a table), `schemas/`, `services/`,
`api/routes/`, plus a line in `api/router.py`.

Config comes from `app/core/config.py` (`Settings`, pydantic-settings) reading `.env`. All logging
goes through `app/core/logging.py`; every request gets a correlation id (see `X-Request-ID` response
header and log lines) via `app/core/middleware.py`. Domain errors are `AppError` subclasses in
`app/core/exceptions.py`, translated to HTTP responses by the handler in `main.py` — raise them from
services, not `HTTPException`, so services stay framework-agnostic.

Uses `db/syllabus.db` by default (override with `DATABASE_PATH` in `.env`). Creates the `users` table
on startup if missing — the rest of the syllabus schema is untouched.

## Frontend

```
cd frontend
npm install
copy .env.example .env.local    # optional, defaults work for local dev against the backend above
npm run dev
```
Opens on http://localhost:5173. Requests to `/api/*` are proxied to the backend (`vite.config.ts`;
override the target with `VITE_PROXY_TARGET`), so run both at once.

### Layout
```
src/
  config/env.ts     typed access to import.meta.env
  lib/               cross-feature infrastructure (fetch wrapper, session/localStorage)
  features/<name>/
    api/             calls to the backend for this feature
    hooks/           feature-local React state/logic
    components/      feature-local UI, takes data/callbacks as props (no routing/fetching)
  routes/            one thin file per route: reads the URL, composes a feature's components
  styles/global.css  shared styles, design tokens (light/dark) as CSS custom properties
```
Adding a feature = a new `features/<name>/` folder (mirroring `features/auth/`) plus a route in
`routes/` and `App.tsx`.

## What's here today

- `POST /api/auth/register` — name, email, password (min 8 chars) → creates a user
- `POST /api/auth/login` — email, password → a bearer token (1 hour) + the user
- Login page and Create account page, wired to those two endpoints. A signed-in session is kept in
  `localStorage` and cleared on sign-out or expiry.

Passwords are hashed with Argon2 (`pwdlib`), never stored in plain text.
