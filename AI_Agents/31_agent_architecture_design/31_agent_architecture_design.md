# 31 — Agent Architecture Design

> **Goal:** Move from developer to AI architect: choose the simplest architecture that meets the requirements, and justify it with trade-offs.

**Level:** Architect · **Time:** 2 weeks · **Prerequisites:** Most previous sections

---

## Learning Objectives
- Choose between workflows, single agents and multi-agent systems
- Produce architecture documents with non-functional requirements
- Run design reviews and system-design interviews for agent systems

---

## 31.1 Architecture Ladder (use the lowest rung that works)
| Level | Architecture | Components | Use when |
|---|---|---|---|
| 0 | Single LLM call | Prompt + structured output | Classification, extraction |
| 1 | Workflow / chain | Fixed steps | The process is known and stable |
| 2 | **Simple Agent** | LLM + tools | Open-ended tasks, few tools |
| 3 | **RAG Agent** | LLM + retriever + tools | Knowledge-heavy tasks |
| 4 | **Workflow Agent** | State + nodes + routing (graph) | Mix of fixed process + agentic steps, HITL |
| 5 | **Multi-Agent** | Supervisor + specialists | Parallelizable or clearly separable domains |
| 6 | **Enterprise Agent Platform** | Gateway, many agents, MCP, memory, governance | Organization-wide |

## 31.2 Enterprise Agent Reference Architecture
```
                           ┌── RAG (vector + graph)
                           ├── SQL / data warehouse
User → Gateway → Agent ────┼── MCP servers (internal tools)
  (auth, rate limit,       ├── External APIs
   guardrails)             ├── Memory (short + long term)
                           ├── Sub-agents / A2A agents
                           └── Human (approvals, escalation)
                                  ↓
             Policy engine · Secrets · Audit log
                                  ↓
                  Observability (traces, metrics, cost)
                                  ↓
             Evaluation (offline CI + online scoring) → Feedback loop
```

## 31.3 Design Dimensions
- **Functional**: tasks, tools, data sources, users
- **Autonomy**: what the agent may do alone vs with approval
- **State**: what persists, where, and for how long
- **Context strategy**: retrieval, memory, compaction
- **Model strategy**: which model per step, fallbacks, routing
- **Non-functional**: latency SLOs, throughput, availability, cost per task, data residency, compliance
- **Security**: trust boundaries, the lethal trifecta check, permissions
- **Evaluation**: success metrics, datasets, release gates
- **Operations**: monitoring, incident response, versioning

## 31.4 Common Design Decisions
- Workflow vs agent
- Single vs multi-agent
- Framework choice (or none)
- Vector DB choice (pgvector vs dedicated)
- Build vs buy (managed agent platforms)
- Sync vs async (chat vs background jobs)
- Hosted vs self-hosted models

## 31.5 Documentation
- Architecture Decision Records (ADRs)
- C4 diagrams (context, container, component)
- Threat model
- Eval plan
- Cost model (monthly estimate at expected traffic)

## 31.6 System Design Practice
Practice designing these (45-minute interview format):
1. A customer support agent for 1M users
2. An internal enterprise knowledge assistant with document-level permissions
3. An autonomous coding agent for a 500-engineer company
4. A voice agent for a hospital appointment line
5. A financial document processing pipeline with compliance requirements
6. A multi-tenant agent SaaS platform

For each: requirements → architecture → data flow → risks → evals → cost estimate.

---

## Deliverable
An architecture document (with ADRs, C4 diagrams, threat model, eval plan and cost model) for one of your capstone projects, **written before building it**.

## Definition of Done
- [ ] 3 system designs practiced and written up
- [ ] One full architecture package peer-reviewed
