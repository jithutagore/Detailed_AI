# AI Agent / Agentic AI Engineering — Syllabus Overview

This folder is the index for the whole curriculum. Each numbered folder has its own `.md` file with the detailed syllabus for that section.

**Not in scope here:** training, fine-tuning, aligning, or serving LLMs yourself (SFT, LoRA/QLoRA, RLHF/DPO, quantization, vLLM-style serving) — see `LLM_Engineering\`, which this folder's Sections 04 and 25 assume you've at least skimmed.

---

## 1. Evaluation of the Original Syllabus

### What was already strong
- **It teaches concepts before frameworks.** You build the agent loop by hand before you use LangChain or LangGraph. That's the right order.
- **It covers production topics.** Security, evaluation, observability, reliability, cost and human-in-the-loop are all included. Most syllabi skip them.
- **It's project-driven.** Every phase has a project, and the capstones are realistic.
- **Agentic RAG is its own phase**, separate from basic RAG.
- **Context engineering** and **agentic coding** are included. Both are current, high-value skills.

### What was missing (added in this version)
| Gap | Why it matters | Where it is now |
|---|---|---|
| **LLM APIs & providers** (OpenAI, Anthropic, Gemini, open-weight models, Ollama/vLLM) | The learning order listed "LLM APIs", but no phase taught them | `04_llm_apis_and_providers` |
| **Streaming, token counting, rate limits, prompt caching at the API level** | Every agent depends on them | `04` |
| **Other agent frameworks**: OpenAI Agents SDK, Claude Agent SDK, Google ADK, CrewAI, AutoGen/AG2, LlamaIndex, Pydantic AI, smolagents | Job postings ask for more than LangChain, and knowing several helps you choose the right one | `15_other_agent_frameworks` |
| **Agent-to-agent protocols (A2A)** | MCP connects agents to tools; A2A connects agents to each other | `17_mcp_and_agent_protocols` |
| **Multimodal, browser and computer-use agents** | Vision, document understanding, web automation and GUI control are major agent categories | `19_multimodal_browser_and_computer_use_agents` |
| **Guardrails** as a dedicated topic (input/output rails, PII redaction) | The original listed threats but had no dedicated guardrails topic | `21_agent_security_and_guardrails` |
| **Document parsing** (OCR, tables, layout) and **GraphRAG / knowledge graphs** | Most RAG failures are parsing failures | `09_rag_fundamentals`, `10_advanced_and_agentic_rag` |
| **Testing agents** (unit tests with mocked LLMs, prompt versioning, CI for prompts) | Evaluation isn't the same as software testing; you need both | `22_agent_evaluation_and_testing` |
| **Durable execution / long-running agents** (Temporal, queues, scheduled agents) | Real agents run for minutes to hours and must survive crashes | `24_reliability_engineering` |
| **Agent UX** (streaming UIs, showing progress, generative UI) | Users judge agents by how they feel to use | `26_production_deployment` |
| **Responsible AI, governance, compliance** (PII, GDPR, EU AI Act, audit) | Required for enterprise and regulated domains (finance, health) | `30_responsible_ai_and_governance` |
| **Fine-tuning & small models for agents** (when to fine-tune vs prompt vs RAG) | You need it for cost optimization and for choosing between approaches | `25_cost_optimization_and_model_selection` |
| **Math intuition** (vectors, cosine similarity, probability) | Needed to understand embeddings and sampling | `03_llm_foundations` |
| **Agent harness engineering**: the runtime around the model (loop, tools, ACI, context manager, permissions, hooks, skills, sub-agents, sandboxes, code-as-action) | Agent = Model + Harness. The harness affects results about as much as the model | `33_agent_harness_engineering` |
| **Agent environments & agentic RL** (environments, verifiers, rewards, GRPO, reward hacking) | How agents are trained to use tools; lets you train small, cheap specialist models | `34_agent_environments_and_agentic_rl` |
| **Test-time compute / inference scaling** | Choosing between more thinking, more attempts or a bigger model | `18_advanced_agent_architecture` (18.2b) |
| **CrewAI in depth** (agents, tasks, crews, processes, Flows, memory, knowledge, testing) | One of the most popular multi-agent frameworks; the original only named it in a warning | `15_other_agent_frameworks` (15.4) |
| **Low-code agent platforms**: n8n in depth (AI Agent node, RAG, MCP, HITL, self-hosting in queue mode), plus Flowise, Langflow, Dify, Make, Zapier, Copilot Studio, OpenAI Agent Builder | Many AI-automation jobs and freelance projects are built on these; hybrid low-code + code is a common production architecture | `35_low_code_agent_platforms` |
| **LangSmith & LangChain ecosystem**: LangSmith tracing, datasets, experiments, CI testing, annotation queues, online evals, Prompt Hub, LangGraph deployment (Agent Server, Studio), Deep Agents, LangMem, MCP adapters, LangChain.js/LangGraph.js, LangSmith vs Langfuse | LangSmith was named in 8 sections but never taught; professional LangGraph work uses it every day | `36_langsmith_and_langchain_ecosystem` |
| **Agent identity & delegated authorization** (non-human identities, OAuth token exchange, revocation) | Agents acting on behalf of users need scoped, auditable, revocable credentials | `21_agent_security_and_guardrails` (21.6b) |

### What was corrected or restructured
1. **Voice agents were duplicated** (Phase 20.6 and Phase 21). They're merged into `28_voice_agents`.
2. **Specialized agents (Phase 20) overlapped with the capstones.** Phase 20 is now a set of short build-labs with defined patterns, and the capstones are the large portfolio projects.
3. **Evaluation and observability came too late.** You're told to "not skip" them, but they appeared in Phases 14–15. The fix is to **start lightweight evals (from Section 06) and tracing (from Section 08)** as a habit in every project, and study them in depth in Sections 22–23. Every section file now has a "Definition of done" that includes a small eval.
4. **Context engineering** was buried inside "Advanced Architecture". It's now its own section right after Memory, because it's the core skill behind RAG, memory and multi-agent design.
5. **Phase 0 mixed two different skill sets.** Python and backend are now separate sections (01, 02).
6. **Advanced retrieval** (4.3) is merged with Agentic RAG, so basic RAG stays focused and all the techniques that improve quality live in one place.
7. **The MCP claim about a "July 2026 specification"** couldn't be verified here. The MCP spec versions I can confirm are dated `2024-11-05`, `2025-03-26`, `2025-06-18` and `2025-11-25`. The spec changes fast, so always check the latest version at modelcontextprotocol.io rather than relying on a date written in a syllabus.
8. **The CrewAI/AutoGen framework-tutorial warning** is kept, but frameworks are now taught as *comparisons of the same concepts*, which is the point the original was making.

---

## 2. Final Section Map

| # | Folder | Level | Suggested time |
|---|---|---|---|
| 01 | `01_python_for_ai_engineering` | Foundation | 2–3 weeks |
| 02 | `02_backend_fundamentals` | Foundation | 2–3 weeks |
| 03 | `03_llm_foundations` | Foundation | 1–2 weeks |
| 04 | `04_llm_apis_and_providers` | Foundation | 1 week |
| 05 | `05_prompt_engineering` | Foundation | 1 week |
| 06 | `06_structured_outputs` | Foundation | 1 week |
| 07 | `07_function_calling_and_tools` | Core | 2 weeks |
| 08 | `08_agent_loop` | Core | 1–2 weeks |
| 09 | `09_rag_fundamentals` | Core | 2 weeks |
| 10 | `10_advanced_and_agentic_rag` | Core | 2–3 weeks |
| 11 | `11_memory` | Core | 1–2 weeks |
| 12 | `12_context_engineering` | Core | 1 week |
| 13 | `13_langchain` | Frameworks | 1–2 weeks |
| 14 | `14_langgraph` | Frameworks | 2–3 weeks |
| 15 | `15_other_agent_frameworks` | Frameworks | 2–3 weeks |
| 16 | `16_multi_agent_systems` | Advanced | 2 weeks |
| 17 | `17_mcp_and_agent_protocols` | Advanced | 1–2 weeks |
| 18 | `18_advanced_agent_architecture` | Advanced | 2 weeks |
| 19 | `19_multimodal_browser_and_computer_use_agents` | Advanced | 1–2 weeks |
| 20 | `20_human_in_the_loop` | Production | 1 week |
| 21 | `21_agent_security_and_guardrails` | Production | 2 weeks |
| 22 | `22_agent_evaluation_and_testing` | Production | 2 weeks |
| 23 | `23_observability` | Production | 1 week |
| 24 | `24_reliability_engineering` | Production | 1–2 weeks |
| 25 | `25_cost_optimization_and_model_selection` | Production | 1 week |
| 26 | `26_production_deployment` | Production | 2 weeks |
| 27 | `27_agentic_coding` | Specialization | 2 weeks |
| 28 | `28_voice_agents` | Specialization | 2 weeks |
| 29 | `29_specialized_agents` | Specialization | 2–3 weeks |
| 30 | `30_responsible_ai_and_governance` | Architect | 1 week |
| 31 | `31_agent_architecture_design` | Architect | 2 weeks |
| 32 | `32_capstone_projects` | Portfolio | 6–10 weeks |
| 33 | `33_agent_harness_engineering` | Advanced (study after 27) | 2–3 weeks |
| 34 | `34_agent_environments_and_agentic_rl` | Advanced / ML, optional (study after 25) | 2–3 weeks |
| 35 | `35_low_code_agent_platforms` | Frameworks / Practical (study after 15) | 2 weeks |
| 36 | `36_langsmith_and_langchain_ecosystem` | Frameworks / Production (study after 14; revisit with 22–23) | 2 weeks |

> Sections 33–36 were added later, so their numbers don't match their place in the learning path. Follow the path below.

**Total:** about 12–15 months part-time (10–15 hrs/week), or 7 months full-time. Section 34 is optional.

---

## 3. Learning Path

```
Python → Backend → LLM Foundations → LLM APIs → Prompting → Structured Outputs
   ↓
Tools → Agent Loop → RAG → Agentic RAG → Memory → Context Engineering
   ↓
LangChain → LangGraph → 36 LangSmith & Ecosystem → Other Frameworks (incl. CrewAI) → 35 Low-Code (n8n)
   ↓
Multi-Agent → MCP/A2A → Advanced Architecture → Multimodal/Computer-Use
   ↓
HITL → Security → Evaluation → Observability → Reliability → Cost → [34 Agentic RL, optional] → Deployment
   ↓
Agentic Coding → 33 Harness Engineering → Voice / Specialized Agents
   ↓
Governance → Architecture Design → Capstones
```

### Habits to keep throughout (don't postpone these to the end)
- **Trace everything** from Section 08 onward (Langfuse, LangSmith or plain OpenTelemetry).
- **Write a 10–20 case eval set** for every project from Section 06 onward.
- **Track cost and latency** for every project.
- **Treat every tool input and retrieved document as untrusted**, starting in Section 07.
- **Publish each project on GitHub** with a README, an architecture diagram and eval results.

---

## 4. Guiding Principle

> Agent fundamentals → tools → state → RAG → memory → context → orchestration → multi-agent → protocols → evaluation → security → production → architecture.
>
> Frameworks (LangChain, LangGraph, CrewAI, OpenAI Agents SDK, Claude Agent SDK, MCP) are **implementations** of these concepts. Learn the concept first, then the framework.
