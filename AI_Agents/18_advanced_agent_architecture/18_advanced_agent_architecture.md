# 18 — Advanced Agent Architecture

> **Goal:** Senior-level design of planning, reasoning, verification and coordination in agents.

**Level:** Advanced · **Time:** 2 weeks · **Prerequisites:** 12, 14, 16

---

## Learning Objectives
- Implement planning strategies and replanning
- Use reasoning models and verification loops effectively
- Coordinate agents with shared state and message passing
- Design long-running, autonomous agents

---

## 18.1 Planning
- **Task decomposition**
- **Hierarchical planning** (goals → sub-goals → actions)
- Plan-and-execute vs interleaved ReAct
- **Dynamic planning** (planning as you go)
- **Replanning** on failure or new information
- **Plan validation** (checking feasibility, tools available, constraints)
- Plans as structured output (DAG of steps with dependencies)
- LLMCompiler-style parallel plan execution
- To-do lists as a planning tool (the agent maintains and updates a checklist)

## 18.2 Reasoning
- **Chain-of-thought** concepts
- **Reasoning models**: thinking budgets / effort levels, interleaved thinking between tool calls
- When to use a reasoning model (planning, hard analysis) vs a fast model (execution)
- **Reflection** and **self-critique**
- **Verification**: external checks beat self-judgment (tests, calculators, schema checks, source lookup)
- **Tree search** concepts: Tree-of-Thoughts, LATS (Language Agent Tree Search), MCTS
- Best-of-N sampling + verifier
- Limits of self-correction without external feedback

## 18.2b Test-Time Compute / Inference Scaling *(added)*
- The idea: spend more compute **at inference** to get better answers, instead of using a bigger model
- Ways to scale it:
  - **Sequential**: longer thinking (thinking budgets, reasoning effort levels), more agent steps, self-refinement rounds
  - **Parallel**: best-of-N sampling, self-consistency voting, several agents attempting the same task in parallel
  - **Search**: tree search guided by a verifier or reward model
- A **verifier** makes parallel scaling useful (tests, graders, a judge model), because you need a way to pick the best attempt
- Scaling curves: accuracy vs compute; diminishing returns; where extra compute stops helping
- Economics: when 5 attempts with a small model beat 1 attempt with a large model
- Adaptive compute: spend more only on hard queries (ties into routing, Section 25)
- Exercise: on 20 hard tasks, plot success rate vs (a) thinking budget and (b) N parallel attempts with a verifier, against cost

## 18.3 Agent Coordination
- **Shared state** (blackboard, graph state)
- **Message passing** (event-driven, actor model)
- **Agent communication** formats (structured handoff payloads)
- **Conflict resolution**
- **Task delegation** (clear contracts between agents)
- Concurrency control (two agents editing the same resource)

## 18.4 Long-Running & Autonomous Agents
- Agents that run for hours: checkpointing, progress files, resumption
- Background/ambient agents (triggered by events, not chat)
- Scheduled agents (cron)
- Asynchronous human check-ins
- Guarding against goal drift

## 18.5 Learning & Adaptation
- Learning from feedback (storing successful trajectories as examples)
- Skill libraries (reusable procedures, e.g. Voyager-style skills, agent "skills" folders)
- Prompt optimization from traces (DSPy, automated prompt tuning)
- When fine-tuning for agents makes sense (Section 25)

## 18.6 Context Engineering at Scale
- Review Section 12 applied to multi-agent and long-horizon systems
- Context budgets per agent
- Summarization contracts between agents

## 18.7 Architecture Trade-offs
- Autonomy vs control
- Latency vs quality
- Generality vs reliability
- Cost vs thoroughness

---

## Key Papers & Reading
- ReAct (Yao et al., 2022)
- Reflexion (Shinn et al., 2023)
- Tree of Thoughts (Yao et al., 2023)
- LATS (Zhou et al., 2023)
- Plan-and-Solve, LLMCompiler
- Voyager (Wang et al., 2023)
- Anthropic, "Building Effective Agents"

## Project — Self-Correcting Planner Agent
A data-analysis agent that:
- Receives a business question + a CSV/SQL database
- Produces a structured plan (DAG), validated before execution
- Executes steps in parallel where possible (Python sandbox)
- Verifies results with code-based checks
- Replans on failure
- **Eval:** 20 analysis questions; compare with and without planning/verification

## Definition of Done
- [ ] A measured accuracy gain from verification
- [ ] Replanning demonstrated in traces
