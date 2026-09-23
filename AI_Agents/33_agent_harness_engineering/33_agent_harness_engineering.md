# 33 — Agent Harness Engineering  *(NEW section)*

> **Goal:** Design and build the **harness**: the runtime around a model that turns it into an agent. Covers the loop, tools, context management, permissions, hooks, skills, sub-agents, sandboxes and code-as-action.
> **Why added:** The harness affects agent quality about as much as the model does. The same model scores very differently depending on its harness. Earlier sections teach the pieces separately; this section puts them together as one engineering discipline.
> **When to study:** after 27 (Agentic Coding), before the capstones. Its number is 33 only because it was added later.

**Level:** Advanced · **Time:** 2–3 weeks · **Prerequisites:** 07, 08, 12, 20, 21, 27

---

## Learning Objectives
- Explain what a harness is and list its components
- Build a Claude Code–style harness from scratch
- Design the Agent-Computer Interface (ACI): tools, outputs and errors built for a model
- Implement skills, hooks, sub-agents, permissions and compaction
- Use code execution as an action format
- Measure the harness separately from the model

---

## 33.1 What a Harness Is
> **Agent = Model + Harness**

- The model only maps text to text. The harness decides what the model sees, what it can do, and what happens to its output.
- Synonyms: scaffold, scaffolding, agent runtime, agent framework (loosely)
- Harness vs framework: a framework is a library for *building* harnesses (LangGraph); a harness is a complete runtime (Claude Code)
- Harness vs **evaluation harness** (Inspect, lm-evaluation-harness, SWE-bench's harness): a different meaning; see Section 22
- Why benchmark scores always need "model + harness" reported together

```
┌──────────────────────── HARNESS ────────────────────────┐
│  Instructions (system prompt, CLAUDE.md / AGENTS.md)     │
│  Agent loop + stop conditions + budgets                  │
│  Tool registry & execution (built-in, custom, MCP)       │
│  Context manager (compaction, clearing, notes files)     │
│  Permission system + sandbox                             │
│  Hooks (lifecycle events)                                │
│  Skills (on-demand instructions & scripts)               │
│  Sub-agents (isolated contexts)                          │
│  Session persistence (resume, checkpoints)               │
│  Streaming, tracing, UI                                  │
│                        ┌───────┐                         │
│                        │ MODEL │                         │
│                        └───────┘                         │
└──────────────────────────────────────────────────────────┘
```

## 33.2 Reference Harnesses to Study
- **Coding harnesses:** Claude Code, OpenAI Codex CLI, Gemini CLI, OpenHands, Aider, Cline, SWE-agent, mini-SWE-agent (a very small harness, good for reading)
- **Harness SDKs:** Claude Agent SDK, OpenAI Agents SDK, LangChain **Deep Agents**
- Exercise: read the source of one open-source harness and draw its architecture

## 33.3 Instructions Layer
- System prompt design for a general-purpose agent
- Project instruction files (`CLAUDE.md`, `AGENTS.md`): hierarchy (global → project → folder), what belongs there and what doesn't
- Dynamic instructions (environment info, date, OS, git status, injected per session)
- Reminders injected mid-conversation (for example, keeping the to-do list visible)

## 33.4 Agent-Computer Interface (ACI)
- From the **SWE-agent** paper: an agent's tools are its user interface, so design them for a model the way you'd design a UI for a person
- Principles:
  - Few, powerful, well-documented actions
  - Compact, informative output (line numbers, truncation notices, "N more results")
  - Errors that tell the model what to do next
  - Guardrails built into tools (e.g. a linter check before saving an edit)
  - Consistent formats across tools
- File viewing (windowed reading), searching (`grep`/`glob`), editing (exact string replace vs diff vs whole file)
- Shell tool design: timeouts, output limits, background processes
- **Measure ACI changes with evals.** Small tool-format changes can move success rates a lot.

## 33.5 Tool Layer
- Built-in tool set of a general agent: read, write, edit, glob, grep, bash, web fetch/search, to-do list, task/sub-agent
- Loading MCP tools into the harness
- **Tool search / deferred tools**: load tool schemas only when needed so large tool sets don't fill the context
- Parallel tool execution
- Tool result formatting and truncation

## 33.6 Code Execution as Action (CodeAct / "code mode")
- The problem: one JSON tool call per model turn means many round trips, and every intermediate result goes through the context
- The pattern: the agent writes a short program that calls tools as functions and handles loops, filtering and joins **in code**, returning only the final result
- **CodeAct** paper (Wang et al., 2024); Hugging Face **smolagents** code agents
- Code execution with MCP (MCP tools exposed as code APIs inside a sandbox)
- Provider features: programmatic tool calling, code-execution tools
- Trade-offs: large token savings and more expressive actions, but it needs a solid sandbox and is harder to audit
- When to use JSON tool calls vs code actions

## 33.7 Context Manager
- Applying Section 12 inside a harness:
  - **Compaction** (summarizing the conversation near the context limit, then continuing)
  - **Tool-result clearing** (dropping old bulky outputs)
  - **Notes / progress files** (e.g. `progress.md`, to-do lists) as external memory
  - Just-in-time file reading instead of preloading
- Prompt-cache-friendly message layout (stable prefix)
- Harness design for **long-running agents**: initializer + incremental sessions, a progress log, git commits as checkpoints, a feature/test checklist the agent works through

## 33.8 Permission System & Sandbox
- Permission modes: ask every time → allow-listed commands → auto-accept edits → fully autonomous (in a sandbox only)
- Rules: allow/deny patterns per tool (`Bash(git status)`, `Edit(src/**)`)
- Dangerous-command detection
- **Sandboxes as the agent's workspace**:
  - Local: Docker containers, devcontainers, OS-level sandboxing (filesystem + network isolation)
  - Cloud: E2B, Modal, Daytona, Cloudflare Sandbox, Vercel Sandbox, and others
  - Persistent vs throwaway sandboxes; file syncing; network egress allowlists
- Checkpoints and rewind (undoing the agent's file changes)

## 33.9 Hooks (Lifecycle Events)
- Events: session start, user prompt submitted, **pre-tool-use**, **post-tool-use**, stop, sub-agent stop, before compaction, notification
- Uses:
  - Block dangerous commands (pre-tool-use policy)
  - Auto-format / lint after edits (post-tool-use)
  - Inject context at session start
  - Audit logging
  - Require tests to pass before the agent can stop
- Hooks are deterministic: use them for rules that **must** always happen instead of hoping the model remembers
- Same idea in other ecosystems: LangChain middleware, OpenAI Agents SDK guardrails/lifecycle hooks

## 33.10 Skills
- A **skill** is a folder with a `SKILL.md` (name + description + instructions), plus optional scripts, templates and reference files
- **Progressive disclosure**: only name + description sit in context; the full skill loads when relevant; bundled files load only if needed
- Writing good skills: clear trigger description, concise steps, scripts for deterministic work, examples
- Skills vs tools vs sub-agents vs MCP servers:

| Mechanism | Gives the agent | Use for |
|---|---|---|
| Tool | An action | Doing one thing |
| MCP server | A set of tools/resources from an external system | Integrations |
| Skill | Know-how + scripts, loaded on demand | Procedures, domain expertise |
| Sub-agent | A separate context window + role | Isolation, parallel work |

- Testing and evaluating skills (does it trigger when it should? does it improve outcomes?)

## 33.11 Sub-agents
- Sub-agent as a tool: task description in, condensed result out
- Context isolation (the main context stays clean)
- Per-sub-agent tools, permissions and models (e.g. a cheap model for search)
- Parallel sub-agents
- Avoiding over-delegation (see Section 16)

## 33.12 Sessions, Persistence & Headless Mode
- Saving and resuming sessions
- Forking conversations
- Headless / non-interactive mode for CI and automation
- Structured output from headless runs
- Running a harness as a service (SDK embedding)

## 33.13 Measuring the Harness
- Keep the model fixed and vary the harness (tools, prompts, context strategy), and the reverse
- Metrics: task success, steps, tokens, cost, time, permission prompts per task
- Ablation studies: remove one harness feature at a time
- Harness regression suite in CI

---

## Hands-on Exercises
1. Read mini-SWE-agent or a similar minimal harness end to end and write a one-page architecture summary.
2. Change only your `edit` tool's error messages and measure the change in success rate on 10 tasks.
3. Rewrite a 6-tool-call workflow as a single code action and compare tokens and latency.
4. Write a pre-tool-use hook that blocks `rm -rf` and any command touching `.env`.
5. Write 2 skills and test that each triggers on the right requests and not on the wrong ones.

## Project — Build Your Own Mini Coding Harness ("mini Claude Code")
- CLI agent loop with streaming output
- Tools: read (windowed), write, edit (exact replace), glob, grep, bash (timeout + output cap), to-do list, sub-agent
- `AGENTS.md` loading (global + project)
- Permission system with allow/deny rules and 3 modes
- Hooks: pre-tool-use policy + post-edit formatter
- Skills folder with progressive disclosure
- Compaction at 70% context + a progress file
- Docker sandbox mode
- Session save/resume + headless mode
- **Eval:** 20 coding tasks. Run (a) your harness with 2 different models, (b) one model with your harness vs a baseline minimal loop. Report which matters more: model or harness.

## Recommended Reading
- SWE-agent: "Agent-Computer Interfaces Enable Automated Software Engineering" (Yang et al., 2024)
- CodeAct: "Executable Code Actions Elicit Better LLM Agents" (Wang et al., 2024)
- Anthropic engineering blog: building agents with the Claude Agent SDK, Agent Skills, code execution with MCP, harnesses for long-running agents, writing tools for agents
- LangChain Deep Agents docs
- Claude Code documentation (hooks, skills, sub-agents, permissions, settings)

## Definition of Done
- [ ] Your harness completes real multi-file coding tasks in a sandbox
- [ ] Every harness feature has an ablation result
- [ ] You can explain why a given agent product succeeds or fails in terms of its harness, not only its model
