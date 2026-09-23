# 02 — Backend Fundamentals

> **Goal:** Serve an LLM-powered application as a real API with auth, persistence, streaming and background jobs, packaged in Docker.

**Level:** Foundation · **Time:** 2–3 weeks · **Prerequisites:** 01

---

## Learning Objectives
- Build REST and streaming APIs with FastAPI
- Persist data in PostgreSQL through SQLAlchemy, and cache in Redis
- Secure endpoints with JWT/OAuth2
- Run long tasks in background workers
- Containerize everything with Docker Compose

---

## 2.1 FastAPI
- Routing, path/query/body parameters
- Request/response models with Pydantic
- Dependency injection (`Depends`) for DB sessions, auth and config
- Async endpoints
- Middleware (CORS, request IDs, timing)
- Error handling and custom exception handlers
- OpenAPI docs (`/docs`), API versioning
- `lifespan` events (startup/shutdown for clients and DB pools)

## 2.2 REST API Design
- Resource naming, HTTP verbs, status codes
- Pagination, filtering, sorting
- Idempotency keys for POST requests
- Error response format (RFC 9457 Problem Details)
- Rate limiting basics

## 2.3 Authentication & Authorization
- Sessions vs tokens
- **JWT**: structure, signing, expiry, refresh tokens
- OAuth2 password flow and OAuth2/OIDC with external providers
- API keys for service-to-service calls
- Role-based access control (RBAC)
- Password hashing (`argon2`, `bcrypt`)

## 2.4 Streaming & Real-time
- **Streaming responses** (`StreamingResponse`, SSE) for token-by-token LLM output
- **WebSockets** for two-way communication (chat, voice)
- Handling client disconnects and cancellation
- Backpressure basics

## 2.5 Webhooks & Background Jobs
- Receiving webhooks: signature verification, retries, idempotency
- Sending webhooks
- FastAPI `BackgroundTasks` (small jobs only)
- Task queues: **Celery**, **RQ**, **Arq**, or **Dramatiq**
- Job status polling vs push notifications

## 2.6 Databases
- **PostgreSQL**: tables, indexes, joins, transactions, JSONB columns
- **SQLAlchemy 2.0** (async), ORM vs Core
- Migrations with **Alembic**
- Connection pooling
- **Redis**: caching, TTLs, pub/sub, rate limiting, simple queues, session storage
- (Preview) `pgvector` extension, which you'll use in Section 09

## 2.7 Docker
- Images, containers, layers, `Dockerfile` best practices (multi-stage builds, slim images)
- `docker compose` for API + Postgres + Redis
- Volumes, networks, environment variables
- Health checks

## 2.8 Testing the Backend
- `TestClient` / `httpx.AsyncClient` for API tests
- Test databases (fixtures, transactions rolled back per test)
- Mocking the LLM client

---

## Mini Project — FastAPI LLM Chat API

```
User
 ↓
FastAPI (JWT auth)
 ↓
LLM (streaming)
 ↓
Structured Response (Pydantic)
 ↓
PostgreSQL (conversations, messages) + Redis (rate limit, cache)
```

**Features**
- `POST /auth/login`, returns a JWT
- `POST /chat`, streams the answer over SSE
- `GET /conversations/{id}`, returns the full history
- Per-user rate limit in Redis
- Token usage and cost stored per message
- Runs with `docker compose up`

## Common Pitfalls
- Running blocking DB drivers in async endpoints
- Storing JWT secrets in code
- No pagination on history endpoints
- Doing LLM calls longer than 30s inside the request instead of a background job

## Definition of Done
- [ ] API documented at `/docs`
- [ ] Auth-protected endpoints with tests
- [ ] Streaming works in the browser or with `curl -N`
- [ ] One-command startup with Docker Compose
