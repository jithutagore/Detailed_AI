# 26 — Production Deployment

> **Goal:** Ship agents as scalable, secure, observable services with a good user experience.
> **Change from original:** Added **CI/CD**, **infrastructure as code** and **agent UX** (streaming UIs, progress display).

**Level:** Production · **Time:** 2 weeks · **Prerequisites:** 02, 21, 23, 24

---

## Learning Objectives
- Deploy an agent stack to a cloud provider
- Scale workers, streaming connections and stateful components
- Automate deployment with CI/CD and infrastructure as code
- Build a frontend that makes agent behavior understandable

---

## 26.1 Backend Stack
- **FastAPI** agent service (async, streaming)
- **Docker** images (multi-stage, non-root)
- **PostgreSQL** (app data, checkpoints, pgvector)
- **Redis** (cache, rate limits, pub/sub)
- **Celery** / background workers / Temporal workers
- **WebSockets** and **SSE streaming**
- Object storage (S3/GCS/Azure Blob) for documents

## 26.2 Infrastructure
- **AWS** (ECS/Fargate, Lambda, Bedrock, RDS, ElastiCache, S3), **Azure** (Container Apps, AI Foundry, Azure OpenAI), **GCP** (Cloud Run, Vertex AI)
- **Kubernetes basics**: pods, deployments, services, ingress, HPA, secrets
- Serverless vs containers for agents (long runs vs cold starts)
- GPU serving for open models (vLLM on K8s, managed endpoints)
- Managed agent platforms (LangSmith Deployment, AWS Bedrock AgentCore, Vertex AI Agent Engine, Azure AI Foundry Agent Service) and their trade-offs
- **Infrastructure as Code**: Terraform / Pulumi *(added)*

## 26.3 Architecture
```
Frontend (web / mobile / Slack / voice)
   ↓
API Gateway (auth, rate limiting)
   ↓
Agent Service (stateless API)  ←→  Worker pool (long tasks)
   ↓
┌─────────────────────────────┐
│ LLM providers / model gateway│
│ Vector DB                    │
│ PostgreSQL (state, checkpoints)│
│ Redis                        │
│ MCP Servers                  │
│ Secret manager               │
└─────────────────────────────┘
   ↓
Observability (traces, metrics, logs) + Eval pipeline
```

## 26.4 CI/CD *(added)*
- GitHub Actions: lint → unit tests → eval suite → build image → deploy
- Environments: dev / staging / prod
- Prompt and model versioning as deployable config
- Canary releases and A/B tests for agent versions
- Rollback strategy

## 26.5 Scaling Concerns
- Horizontal scaling of stateless services
- Sticky sessions vs external state for WebSockets
- Connection limits for streaming
- Queue-based load leveling
- Per-tenant quotas
- Provider rate limits as the real bottleneck

## 26.6 Agent UX *(added)*
- Streaming tokens and **streaming intermediate steps** ("Searching…", "Reading 3 documents…")
- Showing sources and citations
- Approval UIs (Section 20)
- Stop/cancel buttons
- Displaying plans and to-do lists
- Error messages users understand
- Frameworks: Vercel AI SDK UI, CopilotKit, AG-UI protocol, Chainlit, Streamlit/Gradio (prototypes)
- Generative UI (the agent returns UI components)

## 26.7 Operations
- Health checks, readiness/liveness probes
- Secrets rotation
- Backups (Postgres, vector DB)
- Incident runbooks
- Cost monitoring and budgets

---

## Project — Deploy the Enterprise Agent to the Cloud
- Terraform-provisioned environment on AWS, Azure or GCP
- Agent API + workers + Postgres + Redis + vector DB
- CI/CD pipeline with eval gating
- React/Next.js (or Chainlit) frontend with streaming steps and citations
- Public demo URL (with auth) and an architecture diagram

## Definition of Done
- [ ] One-command infrastructure deployment
- [ ] PRs that fail evals can't deploy
- [ ] Dashboards and alerts live in production
