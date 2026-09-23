# 15 — Other Agent Frameworks & SDKs  *(NEW section)*

> **Goal:** Know the main agent frameworks well enough to compare them and pick the right one. Learn them as *different implementations of the same concepts*, not as separate tutorials.
> **Why added:** Job requirements and real projects use many frameworks besides LangChain/LangGraph.

**Level:** Frameworks · **Time:** 2–3 weeks · **Prerequisites:** 08, 13, 14

---

## Learning Objectives
- Map every framework onto the core concepts (loop, tools, state, memory, handoffs, HITL, tracing)
- Build the same small agent in 3 frameworks and compare them
- Write a framework-selection guide

---

## 15.1 Frameworks to Study

| Framework | Key ideas | Best for |
|---|---|---|
| **OpenAI Agents SDK** | Agents, tools, handoffs, guardrails, sessions, built-in tracing | Lightweight multi-agent apps; OpenAI ecosystem (supports other models via LiteLLM) |
| **Claude Agent SDK** | The agent harness behind Claude Code: file/shell tools, sub-agents, hooks, skills, MCP, permissions, context compaction | Coding agents, file-heavy and long-running autonomous agents |
| **Google ADK (Agent Development Kit)** | Agents, workflow agents (Sequential/Parallel/Loop), sessions, A2A support | Gemini / Vertex AI ecosystem |
| **CrewAI** | Role-based agents, crews, tasks, flows | Quick role-based multi-agent prototypes |
| **AutoGen / AG2 / Microsoft Agent Framework** | Conversational multi-agent, event-driven actors | Research, multi-agent conversation patterns, Azure ecosystem |
| **LlamaIndex** (Workflows, agents) | Data connectors, indexing, event-driven workflows | RAG-heavy agents |
| **Pydantic AI** | Type-safe agents, dependency injection, structured outputs | Python developers who want strong typing |
| **smolagents** (Hugging Face) | Code agents (actions written as Python code) | Open models, minimal code |
| **Semantic Kernel** | Plugins, planners, .NET/Python/Java | Enterprise Microsoft stacks |
| **DSPy** | Programming (not prompting) LMs, prompt optimization | Optimizing pipelines against metrics |

Also know about: Vercel AI SDK (TypeScript), Mastra (TypeScript), Haystack, Agno.

## 15.2 Comparison Dimensions
- Control vs convenience (low-level graph vs high-level agent)
- State and persistence model
- Multi-agent primitives (handoffs, supervisor, group chat)
- Human-in-the-loop support
- Tracing and observability integration
- Model and provider flexibility
- MCP support
- Production maturity, community, docs
- Language support (Python/TypeScript/.NET)
- Lock-in risk

## 15.3 Concept Mapping Exercise
Fill in a table for each framework:

| Concept | LangGraph | OpenAI Agents SDK | Claude Agent SDK | CrewAI | Pydantic AI |
|---|---|---|---|---|---|
| Agent loop | | | | | |
| Tool definition | | | | | |
| State / memory | | | | | |
| Multi-agent | | | | | |
| HITL | | | | | |
| Guardrails | | | | | |
| Tracing | | | | | |

## 15.4 CrewAI Deep-Dive *(added)*
CrewAI is one of the most popular role-based multi-agent frameworks, and it appears often in job postings. Learn it hands-on, not only as a row in the comparison table.

### Core building blocks
- **Agent**: `role`, `goal`, `backstory`, `tools`, `llm`, `allow_delegation`, `max_iter`, `memory`, `verbose`
  - Writing role/goal/backstory well: it's prompt engineering in a structured form
- **Task**: `description`, `expected_output`, `agent`, `context` (outputs of other tasks), `output_pydantic` / `output_json`, `output_file`, `async_execution`, `human_input`, task guardrails (validating output before it's accepted)
- **Crew**: `agents`, `tasks`, `process`, `memory`, `planning`, `manager_llm` / `manager_agent`, `verbose`
- **Processes**:
  - **Sequential**: tasks run in order, with each output passed as context
  - **Hierarchical**: a manager agent delegates and validates (the supervisor pattern from Section 16)

### Project structure
- `crewai create crew <name>` scaffold
- YAML config: `agents.yaml`, `tasks.yaml`; `@CrewBase`, `@agent`, `@task`, `@crew` decorators
- Inputs and interpolation (`{topic}` placeholders), `crew.kickoff(inputs=...)`, `kickoff_for_each`, async kickoff

### Tools
- `crewai_tools` package (search, scraping, file, RAG tools)
- Custom tools: `BaseTool` subclass or `@tool` decorator
- Tool caching
- MCP tools in CrewAI
- LangChain tools inside CrewAI

### Memory & knowledge
- Memory types: short-term, long-term, entity memory, and how they're stored
- **Knowledge sources** (files, PDFs, strings) for agent-level or crew-level RAG
- Embedder configuration

### Flows (production orchestration)
- **Flows** = event-driven workflows around crews: `@start`, `@listen`, `@router`, `and_` / `or_`
- Structured flow **state** (Pydantic), state persistence
- Combining deterministic steps + LLM calls + whole crews inside one Flow
- Crews vs Flows: crews for autonomy, flows for control; production apps usually use Flows that call crews

### Models, testing & operations
- LLM configuration (many providers via LiteLLM; local models via Ollama)
- `crewai test` (running a crew N times and scoring it), `crewai train` (training from human feedback)
- Observability integrations (Langfuse, AgentOps, OpenTelemetry-based tools, and others)
- CrewAI's managed/enterprise platform (awareness)

### Strengths & weaknesses
- ✅ Very fast to prototype role-based teams; readable; strong community
- ⚠️ Less fine-grained control than LangGraph; hierarchical mode can loop or over-delegate; token cost grows quickly with many agents
- Rule: use Flows for anything production-bound, and keep crews small (2–4 agents)

### CrewAI Project — Content Research & Publishing Crew
```
Flow
 ├── @start: fetch topic + audience (inputs)
 ├── Crew: Researcher → Analyst → Writer → Editor (sequential)
 ├── @router: quality score ≥ 8? → publish : revise (max 2)
 ├── human_input approval before publishing
 └── output: Markdown article + sources (Pydantic output)
```
- Custom tools + one MCP server
- Knowledge source with a brand style guide
- `crewai test` over 10 topics; compare sequential vs hierarchical on quality, tokens and time

## 15.5 No-code / Low-code Platforms
Covered in depth in **Section 35 — Low-Code Agent Platforms** (n8n, Flowise, Langflow, Dify, Make, Zapier, Copilot Studio, OpenAI Agent Builder).

---

## Project — Same Agent, Three Frameworks
Build a "Travel Planner Agent" (search, weather, budget calculator, itinerary output) in:
1. OpenAI Agents SDK
2. Claude Agent SDK **or** Google ADK
3. CrewAI **or** Pydantic AI

Run the same 15-case eval on each. Compare lines of code, eval score, latency, cost and debugging experience.

## Deliverable
`framework_selection_guide.md`: your own decision tree for choosing a framework.

## Definition of Done
- [ ] 3 working implementations with the same eval
- [ ] A written, evidence-based comparison
