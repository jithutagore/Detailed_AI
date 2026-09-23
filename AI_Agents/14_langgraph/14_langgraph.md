# 14 — LangGraph

> **Goal:** Model agents and workflows as explicit graphs over shared state, with cycles, persistence, interrupts, human approval and streaming. This is a key skill for professional agent engineering.

**Level:** Frameworks · **Time:** 2–3 weeks · **Prerequisites:** 08, 13

---

## Learning Objectives
- Design graph-based agents with state, nodes and (conditional) edges
- Add persistence, interrupts and human-in-the-loop
- Use streaming, subgraphs, parallelism and retry policies
- Deploy LangGraph apps

---

## 14.1 Core Concepts
- **State**: `TypedDict` / Pydantic state schemas
- **Nodes**: functions that read state and return updates
- **Edges**: normal and **conditional edges**
- **Reducers** (e.g. `add_messages`, `operator.add`) that decide how updates merge
- **Graph**: `StateGraph`, `START`, `END`, `compile()`
- **`Command`** (update state + route in one return)
- **`Send`** API (dynamic fan-out / map-reduce)
- Graph API vs **Functional API** (`@entrypoint`, `@task`)

## 14.2 Persistence
- **Checkpoints** and checkpointers (InMemory, SQLite, Postgres)
- **Threads** (`thread_id`) for conversations
- **Store** for cross-thread long-term memory
- State inspection: `get_state`, `get_state_history`

## 14.3 Human-in-the-Loop
- **Interrupts**: `interrupt()` inside nodes, then resume with `Command(resume=...)`
- Approve / edit / reject patterns
- Reviewing tool calls before execution
- Static breakpoints (debugging)

## 14.4 Advanced Features
- **Streaming** modes: `values`, `updates`, `messages` (tokens), `custom`, `debug`
- **Time travel**: replay and fork from past checkpoints
- **State management**: private state, input/output schemas
- **Subgraphs** (shared vs different state schemas)
- **Parallel execution** (fan-out / fan-in, supersteps)
- **Retry policies** per node
- Node caching
- Recursion limits
- Durable execution modes

## 14.5 Prebuilt Components
- Prebuilt ReAct agent / LangChain `create_agent` running on LangGraph
- `ToolNode`, `tools_condition`
- Supervisor and swarm libraries (preview of Section 16)

## 14.6 Deployment & Tooling
> Overview only. The hands-on version (LangSmith, Studio, Agent Server, Deep Agents, LangMem, LangGraph.js) is in **Section 36**.

- LangGraph Studio (visual debugging)
- LangGraph CLI and local server
- LangGraph Platform / LangSmith Deployment (concepts: assistants, threads, runs, cron jobs, double-texting)
- Self-hosting with FastAPI + a Postgres checkpointer

## 14.7 Testing Graphs
- Unit-test individual nodes
- Test routing logic with fixed state
- Integration tests with mocked LLMs

---

## Workflow Pattern
```
START
 ↓
Classifier
 ↓
Router
 ├── RAG Agent
 ├── SQL Agent
 └── Web Agent
        ↓
     Validator ── fail ──→ back to Router (max 2 retries)
        ↓ pass
      END
```

## Project — Customer Support Agent
```
Email
 ↓
Intent Classifier (structured output)
 ↓
Router
 ├── Billing
 ├── Technical
 ├── Account
 └── Sales
       ↓
Knowledge Retrieval (RAG)
       ↓
Response Generator
       ↓
Quality Check (LLM-as-judge)
       ↓
Human Approval (interrupt)
       ↓
Send Email (write tool)
```
- Postgres checkpointer, so a run survives a restart and resumes after approval
- Streaming progress to a simple UI
- Time travel to debug a bad response
- **Eval:** 30 emails; routing accuracy, response quality score, approval rate

## Definition of Done
- [ ] Graph diagram exported and included in the README
- [ ] Interrupt/resume works across a process restart
- [ ] Node-level unit tests
