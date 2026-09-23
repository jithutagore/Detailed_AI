# 36 — LangSmith & the LangChain Ecosystem  *(NEW section)*

> **Goal:** Get hands-on with LangSmith (tracing, evaluation, monitoring, prompts, deployment) and the other LangChain-ecosystem libraries you'll meet in professional LangGraph work.
> **Why added:** The syllabus named LangSmith in 8 places but never taught it. Deep Agents, LangMem, LangGraph deployment and the JS versions were only mentioned or missing.
> **When to study:** Part A right after 14 (LangGraph), then revisit it with 22 (Evaluation) and 23 (Observability). Its number is 36 only because it was added later.
> **Note:** LangChain renames and repackages products fairly often (e.g. "LangGraph Platform" is now part of **LangSmith Deployment**, and LangGraph Studio lives inside LangSmith). Check docs.langchain.com for current names.

**Level:** Frameworks / Production · **Time:** 2 weeks · **Prerequisites:** 13, 14; ideally 22, 23

---

## Who Makes What (avoid the naming confusion)
| Product | Company | What it is |
|---|---|---|
| LangChain | LangChain Inc. | Agent + component framework (Section 13) |
| LangGraph | LangChain Inc. | Graph orchestration runtime (Section 14) |
| **LangSmith** | LangChain Inc. | Observability, evals, prompt management, deployment platform (**framework-agnostic**) |
| Deep Agents, LangMem, langgraph-supervisor/swarm, langchain-mcp-adapters, openevals, agentevals | LangChain Inc. | Ecosystem libraries |
| **Langfuse** | Separate company (open source) | An alternative to LangSmith's observability and eval features |
| **Langflow** | Separate project | Visual flow builder (Section 35) |

---

## Part A — LangSmith Deep-Dive

### 36.1 Setup & Tracing
- Account, API key, workspaces, **projects** (tracing projects per app/environment)
- Enabling tracing: environment variables (`LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT`); LangChain/LangGraph trace automatically
- **Tracing without LangChain**: `@traceable` decorator, `wrap_openai` / SDK wrappers, OpenTelemetry ingestion. LangSmith works with any framework or plain SDK code.
- Run tree: runs, child runs, run types (llm, tool, retriever, chain)
- **Threads** (grouping multi-turn conversations)
- Metadata and tags (user ID, prompt version, model, environment), filtering and search
- Token and **cost tracking**
- Masking inputs/outputs (PII), sampling rates, data retention settings
- Sharing traces and comparing runs side by side

### 36.2 Datasets
- Examples: inputs, reference outputs, metadata
- Creating datasets from code, CSV, or **directly from production traces**
- Splits (e.g. `train`, `test`, `edge-cases`), versions and tags (evaluating against a fixed version)
- Dataset schemas
- Synthetic example generation (review before using)

### 36.3 Evaluation & Experiments
- `evaluate()` / `aevaluate()`: target function + dataset + evaluators → **experiment**
- **Evaluator types**:
  - Custom code evaluators (exact match, schema checks, SQL result comparison)
  - **LLM-as-judge** evaluators (with the `openevals` library, or configured in the UI)
  - **Trajectory evaluators** for agents (the `agentevals` library: tool-call sequence match, trajectory LLM judge)
  - Summary evaluators (dataset-level metrics like F1, precision/recall)
- **Pairwise experiments** (A vs B comparison judged by an LLM or humans)
- Repetitions (running each example N times to measure non-determinism)
- Comparison view: regressions and improvements per example
- Evaluating intermediate steps of a LangGraph (single node, routing decision, retrieval)
- Calibrating judges: align LLM-judge scores with human labels (connects to Section 22.3)

### 36.4 Testing in CI
- **pytest integration** (`@pytest.mark.langsmith`, logging inputs/outputs/feedback from tests) and the Vitest/Jest equivalents for JS
- Running experiments in GitHub Actions, and failing the build on metric regression
- Deciding what runs on every PR (fast, cheap subset) vs nightly (full dataset)

### 36.5 Human Feedback & Annotation
- **Annotation queues**: sending runs for human review with a rubric
- Feedback keys and scores, collecting user feedback (thumbs up/down) from your app via the SDK
- Turning corrected annotations into dataset examples (feedback loop → Section 22)

### 36.6 Production Monitoring
- **Online evaluators** (LLM-judge or code evaluators running automatically on sampled production traces)
- **Automation rules**: filter runs, then add to a dataset, send to an annotation queue, or trigger a webhook
- Monitoring dashboards: latency, error rate, cost, feedback scores, tool usage
- **Alerts** (error rate, latency, feedback thresholds)
- Trace clustering / insight features for finding common failure patterns (check the current feature set)

### 36.7 Prompt Engineering in LangSmith
- **Prompt Hub**: versioned prompts, commits, tags (`prod`, `staging`)
- Pulling prompts in code by tag, so you can change a prompt without redeploying (and run evals before promoting a tag)
- **Playground**: testing prompts against models and datasets; running experiments from the UI
- Prompt canvas / prompt-improvement assistants

### 36.8 Administration & Privacy
- Organizations, workspaces, roles/RBAC, API keys (personal vs service keys)
- Regions (US/EU), data retention tiers
- Self-hosted / hybrid options (enterprise) for regulated data (ties into Section 30)
- Pricing model: seats + trace volume; estimating cost at scale

---

## Part B — LangGraph Deployment (LangSmith Deployment / Agent Server)

### 36.9 Local Development
- `langgraph.json` config (graphs, dependencies, env)
- `langgraph dev` (local Agent Server with hot reload) + **Studio** (visual graph debugging: step through, edit state, rerun from a node, interrupts)
- Connecting Studio to your local server

### 36.10 Agent Server Concepts
- **Assistants** (a graph + a config, versioned; many assistants per graph)
- **Threads** (persistent state), **runs** (executions), background runs
- **Streaming** API modes over HTTP
- **Double-texting** strategies when a user sends a new message mid-run: reject, enqueue, interrupt, rollback
- **Cron jobs** (scheduled agents), **webhooks** (run completion callbacks)
- Built-in **Store** (long-term memory) and checkpointer (Postgres)
- Custom **authentication & authorization** handlers (per-user thread access)
- The LangGraph SDK client (Python/JS) for calling deployed agents

### 36.11 Deployment Options
- Cloud (managed by LangChain), hybrid (your data plane), self-hosted, standalone container (`langgraph build` → Docker image)
- Comparison with the do-it-yourself stack (FastAPI + Postgres checkpointer, Section 26): what you get for free (queues, streaming, double-texting, cron, Studio) vs lock-in and cost
- Frontends: **Agent Chat UI** (a ready-made chat UI for any LangGraph server), `useStream` React hook for custom UIs, generative UI with LangGraph

---

## Part C — Ecosystem Libraries

### 36.12 Deep Agents
- `create_deep_agent`: a ready-made **harness** (Section 33) on LangGraph
- Built-in pieces: planning/to-do tool, virtual or real **file system** (context offloading), **sub-agents**, a detailed system prompt, pluggable backends
- When to use it: long, multi-step research/coding/analysis tasks
- Deep Agents CLI (a coding-agent harness) — awareness
- Exercise: rebuild your Section 12 long-horizon agent with Deep Agents and compare

### 36.13 LangMem
- Memory tools for agents (`manage_memory`, `search_memory`) backed by the LangGraph Store
- Background memory manager (extracting and consolidating memories after conversations)
- Semantic, episodic and procedural memory (prompt optimization from feedback)
- Exercise: add LangMem to your Section 11 assistant; compare with your hand-built memory

### 36.14 Multi-Agent & Integration Libraries
- **langgraph-supervisor** and **langgraph-swarm** (prebuilt supervisor and handoff patterns), and when to build these patterns yourself with tool-calling for more control
- **langchain-mcp-adapters** (loading MCP server tools into LangChain/LangGraph agents; multi-server client)
- **openevals** / **agentevals** (prebuilt evaluators, usable with or without LangSmith)
- LangGraph templates / starter projects

### 36.15 LangChain.js & LangGraph.js (TypeScript track)
- Why it matters: full-stack and Next.js teams build agents in TypeScript
- `langchain` / `@langchain/core` / `@langchain/langgraph` packages; API parity with Python and the differences
- Zod schemas for tools and structured output (instead of Pydantic)
- Streaming to a Next.js frontend, `useStream`
- Deploying JS graphs to the same Agent Server
- Alternative in TS: Vercel AI SDK, Mastra (Section 15)
- Exercise: port your Section 14 support-agent router to LangGraph.js with a Next.js chat UI

---

## Part D — LangSmith vs Langfuse (hands-on comparison)
| Dimension | LangSmith | Langfuse |
|---|---|---|
| License / hosting | Commercial SaaS; self-hosting on enterprise plans | Open source (MIT core); easy self-hosting (Docker/K8s) |
| LangChain/LangGraph integration | Native, zero config | Callback handler / OpenTelemetry |
| Framework-agnostic | Yes (`@traceable`, OTel) | Yes (`@observe`, OTel, many integrations) |
| Evals | Datasets, experiments, pairwise, online evaluators, pytest | Datasets, experiments, LLM-as-judge, scores |
| Prompt management | Prompt Hub + Playground | Prompt management + Playground |
| Human review | Annotation queues | Annotation queues |
| Deployment | LangSmith Deployment (Agent Server) | None (observability only) |
| Choose when | You're all-in on LangGraph and want managed deployment | You need open source, self-hosting or data control, or a non-LangChain stack |

**Exercise:** instrument the same agent with both (or use OpenTelemetry to send to both), run the same dataset experiment in each, and write a one-page recommendation.

---

## Project — Full LangSmith Lifecycle for the Customer Support Agent (Section 14)
1. **Trace**: full tracing with metadata (user, prompt version, model), PII masking
2. **Dataset**: 100 examples from traces + hand-written edge cases, versioned with splits
3. **Evaluate**: code evaluators (routing accuracy) + calibrated LLM judge (response quality) + trajectory evaluator (tool sequence)
4. **Compare**: pairwise experiment between two prompt versions pulled from Prompt Hub
5. **CI**: pytest + LangSmith in GitHub Actions; the PR fails on regression
6. **Deploy**: `langgraph build` → Agent Server with Postgres; Agent Chat UI frontend; custom auth
7. **Monitor**: online evaluator on 10% of traffic, dashboard, alert on error-rate spike, automation rule sending low-scored runs to an annotation queue
8. **Close the loop**: reviewed annotations → new dataset examples → re-run the experiment

## Recommended Resources
- docs.langchain.com (LangSmith, LangGraph, Deep Agents, LangMem)
- **LangChain Academy** (free courses: Intro to LangGraph, LangSmith evaluation, Deep Agents, ambient agents)
- LangChain blog (context engineering, evaluation guides)
- Langfuse docs (for the comparison)

## Definition of Done
- [ ] Every run of your agent is traced with useful metadata
- [ ] Versioned dataset + experiment history showing improvement over time
- [ ] CI blocks regressions
- [ ] Agent deployed on an Agent Server (local container is fine) with auth
- [ ] Online evaluation + alerting running
- [ ] A written LangSmith vs Langfuse recommendation
