# 35 — Low-Code Agent Platforms (n8n & others)  *(NEW section)*

> **Goal:** Build production-grade AI agents and automations on visual platforms, especially **n8n**, and know when low-code beats custom code and when it doesn't.
> **Why added:** Many AI-automation jobs, freelance projects and small-business deployments run on n8n, Make, Zapier or similar platforms, not Python. Engineers who can do both are in high demand.
> **When to study:** after 15 (Other Frameworks). You'll recognize every node as a concept you already built in code. Its number is 35 only because it was added later.

**Level:** Frameworks / Practical · **Time:** 2 weeks · **Prerequisites:** 07, 08, 09, 11, 15

---

## Learning Objectives
- Build AI agents in n8n with tools, memory, RAG, structured outputs and human approval
- Self-host n8n for production (Docker, Postgres, queue mode)
- Connect low-code platforms with code (webhooks, code nodes, MCP, custom APIs)
- Compare the major platforms and choose between low-code and code

---

## Part A — n8n (main focus)

### 35.1 n8n Fundamentals
- What n8n is: a workflow automation platform (open source with a "fair-code" license) with 400+ integrations and native AI nodes
- Cloud vs self-hosted
- **License**: the Sustainable Use License. Understand what it allows before building a commercial product or reselling hosted n8n.
- Core concepts: workflows, nodes, connections, executions, **items** (n8n's data model: arrays of JSON items)
- **Triggers**: Manual, Webhook, Schedule (cron), Chat Trigger, app triggers (Gmail, Slack, Telegram, forms)
- Data transformation: expressions (`{{ $json.field }}`), Edit Fields (Set), IF, Switch, Merge, Loop Over Items, Split Out, Aggregate
- **Code node** (JavaScript / Python) for custom logic
- HTTP Request node (calling any API)
- **Credentials** management (OAuth2, API keys), stored encrypted
- Sub-workflows (Execute Workflow), reusable modules

### 35.2 AI Nodes in n8n
n8n's AI nodes are built on LangChain (JS), so the concepts from Sections 07–13 map onto them directly.

| n8n node type | Concept you already know |
|---|---|
| **AI Agent** node (tools agent) | Agent loop (Section 08) |
| Chat Model sub-nodes (OpenAI, Anthropic, Gemini, Ollama, OpenRouter, …) | LLM APIs (Section 04) |
| **Memory** sub-nodes (Simple/window buffer, Postgres, Redis, others) | Short-term memory (Section 11) |
| **Tool** sub-nodes (HTTP Request tool, Code tool, Call n8n Workflow tool, app tools) | Tools (Section 07) |
| **Structured Output Parser** | Structured outputs (Section 06) |
| Basic LLM Chain, Summarization Chain, Q&A Chain | Chains (Section 05) |
| Text Classifier, Information Extractor, Sentiment Analysis | Classification / extraction (Section 06) |
| **Vector Store** nodes (Qdrant, Pinecone, PGVector, Supabase, in-memory) + Embeddings + Document Loader + Text Splitter | RAG (Section 09) |
| **MCP Client Tool** node / **MCP Server Trigger** | MCP (Section 17) |

- Writing the agent system prompt and tool descriptions in n8n (the same rules as code: specific, with when-to-use guidance)
- `$fromAI()` for letting the model fill tool parameters
- Using a **whole workflow as a tool** (the main pattern for complex, reliable tools)
- Multi-agent in n8n: agents calling other agent workflows as tools (the supervisor pattern)

### 35.3 RAG in n8n
- Ingestion workflow: trigger (Google Drive / folder / form) → Document Loader → Text Splitter → Embeddings → Vector Store (insert)
- Query workflow: Chat Trigger → AI Agent → Vector Store tool (retrieve) → answer with sources
- Metadata filtering, updating and deleting documents (avoiding duplicates on re-ingest)
- Limitations vs code: advanced retrieval (reranking, hybrid, agentic RAG) often needs a Code node or an external retrieval API

### 35.4 Human-in-the-Loop in n8n
- **Wait** node (resume on webhook, form submission or time)
- "Send and wait for response" approval steps (Slack, email, Telegram, and others)
- Human review for tool calls before execution
- Approval-with-edit using n8n Forms

### 35.5 Reliability, Errors & Evaluation
- Node settings: retry on fail, continue on error, timeouts
- **Error workflows** (Error Trigger → alert to Slack/email)
- Execution logs and debugging with pinned data
- Idempotency for webhooks (deduplicating repeated events)
- Rate limits of connected apps and batching
- n8n evaluation features (datasets and metrics for AI workflows); otherwise, send traces to Langfuse/LangSmith via HTTP
- Versioning workflows: export JSON to Git, source-control features (enterprise tiers), dev/prod environments

### 35.6 Self-Hosting for Production
- Docker / Docker Compose deployment
- **PostgreSQL** instead of SQLite for production
- **Queue mode**: main instance + Redis + worker instances, for scaling
- Webhook processors, and reverse proxy + HTTPS (Caddy, Nginx, Traefik)
- Environment variables, the encryption key (back it up, or credentials are lost)
- Backups, upgrades, monitoring (Prometheus metrics endpoint)
- Security: auth/SSO, restricting Code node capabilities, network egress, keeping n8n updated (it's a high-value target since it stores many credentials)

### 35.7 Code ↔ n8n Integration
- n8n calling your FastAPI agent (HTTP Request node): n8n for integrations, Python for complex reasoning
- Your code triggering n8n (webhooks)
- n8n as an MCP server exposing workflows as tools to Claude/other agents
- n8n consuming your custom MCP server (Section 17)
- Custom community nodes (TypeScript), awareness level

### n8n Projects
1. **AI Email Triage Agent**: Gmail trigger → classify (structured output) → RAG over FAQ → draft reply → Slack approval → send → log to Postgres/Sheets.
2. **Company Knowledge Chatbot**: Google Drive ingestion → Qdrant → Chat Trigger agent with memory (Postgres) → cited answers; embeddable chat widget.
3. **Multi-Agent Lead Research**: supervisor agent → research sub-workflow (web search + scraping) → CRM enrichment sub-workflow → personalized outreach draft → human approval.
4. **Production deployment**: self-hosted n8n in queue mode with Postgres + Redis + 2 workers, HTTPS, error workflow alerts, and daily backups.

---

## Part B — Other Platforms

### 35.8 Visual LLM/Agent Builders
| Platform | What it is | Notes |
|---|---|---|
| **Flowise** | Visual builder for LangChain/LlamaIndex-style chains and agents (Agentflows) | Node.js; self-hostable; quick RAG/chatbot prototypes |
| **Langflow** | Visual builder with Python components, exposes flows as APIs and MCP servers | Easy to drop into custom Python code |
| **Dify** | Full LLMOps platform: chatflows, workflows, agents, knowledge bases (RAG), prompt management, logs | Strong built-in RAG and app publishing |
| **OpenAI Agent Builder (AgentKit)** | OpenAI's visual canvas for agent workflows, with ChatKit for embedding | OpenAI-ecosystem focused |

### 35.9 Business Automation Platforms with AI
| Platform | AI capabilities | Notes |
|---|---|---|
| **Make** (formerly Integromat) | AI modules, AI agents, huge app library | Visual, popular with agencies; priced per operation |
| **Zapier** | AI steps, Zapier Agents, Zapier MCP (exposes thousands of app actions to agents) | Easiest for non-technical users; can get expensive at scale |
| **Microsoft Copilot Studio + Power Automate** | Agents inside Microsoft 365, Teams, Dataverse | Dominant in Microsoft enterprises; governance built in |
| **Google (Vertex AI Agent Builder / Gemini enterprise agents)** | Agents inside Google Cloud / Workspace | Google-ecosystem enterprises |
| **Others** | Relevance AI, Voiceflow (conversational/voice), Botpress, Lindy, Gumloop | Niche strengths; check current status |

### 35.10 Choosing Low-Code vs Code
| Choose low-code when | Choose code when |
|---|---|
| Mostly integrations between SaaS apps | Complex reasoning, custom retrieval, fine control of context |
| The client or business team must maintain it | You need unit tests, evals in CI and code review |
| Speed to first version matters most | High volume: per-execution pricing becomes costly |
| Standard patterns (triage, RAG chatbot, enrichment) | Strict security, data residency, or multi-tenant SaaS |
| | Long-running, stateful, multi-agent systems |

**The best architecture is often a hybrid:** n8n or Make for triggers, integrations and approvals, and a Python/LangGraph service (called over HTTP or MCP) for the hard agent logic.

### 35.11 Freelance / Agency Skills (practical)
- Scoping automation projects, estimating operation and token costs for clients
- Building reusable workflow templates
- Handover: documentation, credential ownership (the client owns the accounts), maintenance plans
- Monitoring client workflows (error workflows → your alert channel)

---

## Hands-on Exercises
1. Rebuild your Section 07 Personal Assistant in n8n and compare build time and behavior with the Python version.
2. Expose one n8n workflow as an MCP tool and call it from Claude Desktop or your Section 33 harness.
3. Build the same RAG chatbot in n8n, Flowise and Dify, then compare setup time, retrieval quality and control.
4. Break a workflow on purpose (bad credentials, API timeout) and make sure your error workflow alerts you.

## Definition of Done
- [ ] 4 n8n projects working, one of them self-hosted in queue mode
- [ ] One hybrid system: n8n orchestration + a Python agent service
- [ ] A written low-code vs code decision guide with cost estimates
- [ ] Workflows exported to Git with a README each
