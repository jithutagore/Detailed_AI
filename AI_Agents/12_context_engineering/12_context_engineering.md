# 12 — Context Engineering  *(promoted to its own section)*

> **Goal:** Decide what information enters the model's context at each step, and in what form. This is the central skill behind RAG, memory, tools and multi-agent design.
> **Change from original:** This was a sub-topic of "Advanced Architecture". It's now its own section, placed right after RAG and memory, because they're context engineering problems.

**Level:** Core · **Time:** 1 week · **Prerequisites:** 08, 09, 11

---

## Learning Objectives
- Treat the context window as a scarce, curated resource
- Apply selection, compression, isolation and ordering strategies
- Diagnose failures caused by bad context (poisoning, distraction, confusion, clash)

---

## 12.1 Prompt Engineering vs Context Engineering
- Prompt engineering: how to phrase instructions
- Context engineering: the full set of tokens the model sees (system prompt, tools, examples, history, retrieved data, memory, tool results) at every step of a long-running agent
- "Context rot": performance degrades as context grows

## 12.2 What Goes Into Context?
- System prompt (the right altitude: not too rigid, not too vague)
- Tool definitions (fewer, clearer tools)
- Few-shot examples (canonical, diverse)
- Conversation history
- Retrieved documents
- Memories
- Tool results
- Current task state / plan / scratchpad

## 12.3 What Should Stay Outside Context?
- Raw large data: keep it in files or a DB, and give the model references and tools to query it
- Old tool outputs
- Irrelevant history
- Secrets and credentials (never in context)

## 12.4 Core Strategies
| Strategy | Techniques |
|---|---|
| **Write** (persist outside) | Scratchpads, notes files, to-do lists, memory stores |
| **Select** (pull in what's relevant) | RAG, memory retrieval, tool selection / tool search |
| **Compress** | Summarization, compaction, trimming, tool-result clearing |
| **Isolate** | Sub-agents with their own context windows, sandboxed state |

## 12.5 Techniques
- **Context selection** (relevance scoring)
- **Context compression** (summaries, extractive compression)
- **Context prioritization** and ordering (important info at the start and end)
- **Tool-result filtering** (return summaries and IDs, not raw dumps)
- **Dynamic context construction** (building the prompt per step from state)
- Just-in-time retrieval (the agent explores with tools, e.g. `grep`/`read_file`, instead of preloading everything)
- Compaction for long-running agents
- Structured note-taking (the agent maintains a `NOTES.md` / progress file)
- Sub-agent summarization (sub-agents return condensed results)
- Prompt-cache-friendly layout (stable prefix, variable suffix)

## 12.6 Context Failure Modes
- **Context poisoning**: a hallucination enters context and gets repeated
- **Context distraction**: too much history overwhelms the instructions
- **Context confusion**: irrelevant tools or documents mislead the model
- **Context clash**: contradictory information in context
- Lost-in-the-middle

## 12.7 Measuring Context
- Token budget per component
- Tracking context size per step in traces
- Ablation tests (remove a component and measure the effect on evals)

---

## Hands-on Exercises
1. Instrument your Section 08 agent to log the token breakdown per step (system, tools, history, tool results).
2. Add tool-result clearing and summarization, then compare cost and accuracy.
3. Give the agent 40 tools vs 8 relevant tools and measure tool-selection accuracy.

## Project — Long-Horizon Task Agent
An agent that completes a 30+ step task (e.g. audit a folder of 100 documents and produce a report) using:
- A notes/progress file as external memory
- Compaction when context reaches 70% of the limit
- Sub-agents for per-document analysis, returning summaries only

## Recommended Reading
- Anthropic: "Effective context engineering for AI agents"
- LangChain: "Context Engineering for Agents"
- Chroma research: "Context Rot"

## Definition of Done
- [ ] The agent finishes long tasks without hitting context limits
- [ ] A token-breakdown dashboard or log exists
