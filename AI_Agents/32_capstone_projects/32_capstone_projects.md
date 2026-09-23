# 32 — Capstone Projects

> **Goal:** Build portfolio-grade projects that demonstrate real agent engineering, not only a chatbot. Pick **at least 2** (ideally one from 1–2 and one from 3–5).

**Level:** Portfolio · **Time:** 6–10 weeks · **Prerequisites:** All core + production sections

---

## Required for EVERY Capstone
- [ ] Architecture document written first (Section 31)
- [ ] Eval dataset (≥ 50 cases) + CI eval gate (Section 22)
- [ ] Tracing + cost/latency dashboard (Section 23)
- [ ] Security: threat model, guardrails, injection tests (Section 21)
- [ ] Reliability: retries, fallbacks, checkpointing (Section 24)
- [ ] HITL for high-impact actions (Section 20)
- [ ] Deployed with Docker, CI/CD, and a live demo (Section 26)
- [ ] README with a diagram, a demo video, eval results and a limitations section

---

## Capstone 1 — Deep Research Agent
**Features:** web search, planning, **parallel research sub-agents**, source verification, citations, report generation (Markdown/PDF), follow-up questions, research memory.
**Stretch:** internal document + web mixed research; a report-quality LLM judge validated against human ratings.
**Shows:** multi-agent orchestration, context engineering, evaluation.

## Capstone 2 — Enterprise RAG Agent
**Features:** PDF, DOCX, SQL, web sources; vector DB; **hybrid retrieval + reranking**; agentic/corrective RAG; memory; citations; **document-level access control**; multi-tenant; admin ingestion UI.
**Stretch:** GraphRAG for cross-document questions; exposed as an MCP server.
**Shows:** data engineering, retrieval quality, security, multi-tenancy.

## Capstone 3 — Multi-Agent Developer
```
Manager
   ↓
Researcher → Coder → Reviewer → Tester
   ↓
Deployment (to a staging environment)
```
**Features:** issue → PR, sandboxed execution, test loops, PR review agent, GitHub integration, human merge approval.
**Stretch:** evaluated on a set of seeded bugs or SWE-bench Lite-style tasks.
**Shows:** agentic coding, multi-agent coordination, sandboxing.

## Capstone 4 — Enterprise Workflow Agent (Financial Document Processing)
```
Email
 ↓
Document extraction (vision + OCR)
 ↓
Validation (schema + business rules)
 ↓
Database verification (transaction lookup)
 ↓
Risk assessment (rules + LLM)
 ↓
Decision
 ↓
Human approval (threshold-based)
 ↓
Action (post to ledger / reply email)
 ↓
Audit log
```
**Features:** durable execution, idempotent actions, full audit trail, governance pack (Section 30).
**Shows:** production workflow engineering in a regulated domain. This is the kind of project that shows real agent engineering.

## Capstone 5 — Real-Time Voice Agent *(recommended for you, given your speech/TTS background)*
**Features:** phone or web voice interface, streaming STT/TTS, barge-in, tools (booking, order lookup), RAG, memory, human transfer, latency dashboard.
**Stretch:** multilingual (e.g. English + Malayalam/Hindi), emotion-aware responses.
**Shows:** real-time systems, latency engineering, voice UX.

---

## Portfolio Presentation
For each capstone publish:
1. GitHub repo (clean code, tests, CI badge)
2. 3–5 minute demo video
3. Technical blog post: architecture, trade-offs, eval results, lessons learned
4. Metrics table: task success, latency P95, cost per task, safety test pass rate

## Suggested Timeline
| Week | Activity |
|---|---|
| 1 | Architecture doc + eval dataset |
| 2–4 | Core build |
| 5 | Security + reliability hardening |
| 6 | Deployment + observability |
| 7 | Eval-driven iteration |
| 8 | Documentation, video, blog post |
