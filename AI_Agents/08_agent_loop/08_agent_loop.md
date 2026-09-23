# 08 — The Agent Loop

> **Goal:** Move from "LLM application" to "agent" by building the agent loop by hand, with no framework, so you understand exactly what the frameworks do for you.

**Level:** Core · **Time:** 1–2 weeks · **Prerequisites:** 07

---

## Learning Objectives
- Define what an agent is, and when a workflow is better than an agent
- Implement a robust tool-calling loop from scratch
- Design termination conditions, state and error handling
- Start tracing every run

---

## 8.1 What Is an Agent?
```
Observe → Reason → Plan → Act → Observe result → Continue / Finish
```
- Definition: an LLM that uses tools in a loop and decides its own next step
- **Workflows vs agents** (Anthropic's "Building Effective Agents"):
  - Workflows: predefined code paths (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer)
  - Agents: the model directs its own process
- **When NOT to use an agent**: if a fixed pipeline works, use the pipeline
- Autonomy levels: from assistant (suggests) up to autonomous (acts)

## 8.2 The Core Loop
```python
messages = [system, user]
for step in range(MAX_STEPS):
    response = llm(messages, tools)
    messages.append(response)

    if not response.tool_calls:
        break  # final answer

    for call in response.tool_calls:
        result = execute_tool(call)          # validate, permission-check, timeout
        messages.append(tool_result(call.id, result))
else:
    handle_max_steps_reached()
```

## 8.3 Agent Patterns
- **ReAct** (Reason + Act): the thought → action → observation loop
- Plan-and-execute
- Reflexion (self-reflection after failure)
- Evaluator-optimizer loops
- Routing and orchestrator-workers (as workflows)

## 8.4 Agent Components
| Component | Responsibility |
|---|---|
| **Agent** | LLM + instructions + tools |
| **Tools** | Actions in the world |
| **State** | Messages, variables, intermediate results |
| **Context** | What is sent to the model on each step |
| **Memory** | What persists across turns and sessions |
| **Planner** | Breaks the goal into steps |
| **Executor** | Runs the steps and tools |
| **Critic / Verifier** | Checks the quality of results |
| **Router** | Chooses a path or specialist |
| **Human approval** | Gates risky actions |
| **Termination conditions** | Final answer, max steps, max cost, max time, stuck detection |

## 8.5 Robustness in the Loop
- Max iterations, token and cost budgets, wall-clock timeout
- Detecting loops (the same tool called with the same args repeatedly)
- Tool errors fed back as observations
- Malformed tool calls
- Graceful degradation (a partial answer plus an explanation)
- Streaming intermediate steps to the user

## 8.6 Async & Parallel Execution
- Executing parallel tool calls concurrently with `asyncio.gather`
- Cancellation when the user aborts

## 8.7 Tracing from Day One
- Log each step: prompt, response, tool calls, results, tokens, latency
- Use a tracer (Langfuse / LangSmith / OpenTelemetry). See Section 23.

---

## Project — Research Agent (framework-free)
```
User Question
      ↓
Planner (structured plan: list of sub-questions)
      ↓
Search Web (per sub-question, in parallel)
      ↓
Extract Information (fetch + summarize pages)
      ↓
Analyze (compare, find conflicts)
      ↓
Verify (check every claim has a source)
      ↓
Generate Report (markdown with citations)
```
- Written only in Python + an LLM SDK, with no agent framework
- Budget limits: max 15 steps, max $0.50 per run
- Trace viewer (even a JSON log file is fine)
- **Eval:** 10 research questions, graded for citation accuracy and completeness

## Common Pitfalls
- No max-step limit (infinite loops, runaway cost)
- Passing whole web pages into context
- Treating tool output as trusted instructions

## Definition of Done
- [ ] You can explain every line of your loop
- [ ] Budgets and termination conditions are enforced
- [ ] Every run produces a trace
