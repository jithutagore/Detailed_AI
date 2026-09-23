# 16 — Multi-Agent Systems

> **Goal:** Design systems where specialized agents cooperate, and know when multiple agents are worth their extra cost and complexity.

**Level:** Advanced · **Time:** 2 weeks · **Prerequisites:** 14, 15

---

## Learning Objectives
- Implement the major multi-agent architectures
- Manage shared state, handoffs and communication
- Decide when a single agent is better
- Evaluate and debug multi-agent systems

---

## 16.1 When to Use Multiple Agents
- Benefits: specialization, parallelism, context isolation, separation of permissions
- Costs: many more tokens, coordination errors, harder debugging
- Rule of thumb: start with a single agent plus good tools; split only when you can measure a gain
- Tasks that parallelize well (broad research) vs tasks that don't (tightly coupled coding)

## 16.2 Architectures

**Supervisor**
```
             Supervisor
          /      |       \
     Research   SQL    Coding
```

**Handoff / Swarm**
```
Agent A → Agent B → Agent C   (control passes; the active agent talks to the user)
```

**Hierarchical**
```
Manager
   ↓
Team Leads
   ↓
Specialized Agents
```

**Network / peer-to-peer**: any agent can call any other agent

**Sub-agents as tools**: the main agent calls sub-agents like tools; each has an isolated context and returns a summary

## 16.3 Patterns
- **Supervisor / orchestrator-worker**
- **Router** (a classifier sends the task to one specialist)
- **Handoff** (transfer of control plus context)
- **Debate** (agents argue; a judge decides)
- **Critic / reviewer** (generator + critic loop)
- **Planner / executor**
- **Parallel agents** (fan-out, then aggregate)
- **Hierarchical agents**
- **Blackboard** (shared workspace that agents read and write)
- Skills (loading specialized instructions on demand instead of creating new agents)

## 16.4 Coordination Mechanics
- Shared state vs message passing
- What context to pass on handoff (full history vs a summary)
- Agent descriptions for routing
- Task delegation instructions (clear objective, output format, boundaries, tool guidance)
- Conflict resolution (voting, a judge agent, rules)
- Avoiding duplicated work and infinite delegation
- Budget allocation per sub-agent

## 16.5 Implementation
- LangGraph: supervisor library, swarm library, custom graphs, `Send` for parallel workers
- OpenAI Agents SDK handoffs
- Claude Agent SDK sub-agents
- CrewAI crews and hierarchical process
- AutoGen group chat

## 16.6 Evaluating Multi-Agent Systems
- End-to-end task success
- Per-agent quality
- Routing / delegation accuracy
- Token multiplier vs a single-agent baseline
- Tracing across agents (nested spans)

## 16.7 Failure Modes
- Agents misunderstanding delegated tasks
- Lost context at handoffs
- Coordination loops
- Error propagation (one bad sub-result corrupts the final output)
- Over-engineering

---

## Project — AI Software Development Team
```
Manager Agent
      ↓
 ┌────┼─────────┐
 ↓    ↓         ↓
PM   Coder   Researcher
      ↓
   Reviewer
      ↓
    Tester
```
- PM writes the spec, Researcher looks up library docs, Coder writes code in a sandbox, Reviewer critiques, Tester runs pytest
- Loop back to Coder on test failure (max 3)
- **Compare** against a single-agent baseline on 10 small coding tasks (success rate, tokens, time)

## Recommended Reading
- Anthropic: "How we built our multi-agent research system"
- Cognition: "Don't Build Multi-Agents" (the counter-argument)
- LangChain multi-agent docs

## Definition of Done
- [ ] Measured comparison against a single agent
- [ ] Trace shows the full delegation tree
