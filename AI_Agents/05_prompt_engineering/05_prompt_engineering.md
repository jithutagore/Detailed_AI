# 05 — Prompt Engineering

> **Goal:** Write clear, testable prompts that produce reliable behavior, and treat prompts as versioned code.

**Level:** Foundation · **Time:** 1 week · **Prerequisites:** 04

---

## Learning Objectives
- Write effective system prompts for agents
- Use examples, delimiters and decomposition to improve reliability
- Iterate on prompts with evals instead of by feel
- Recognize prompt-injection risks early

---

## 5.1 Prompt Anatomy
- **System instructions**: role, goals, constraints, tone, output rules
- **User instructions**: the task and its inputs
- Assistant prefill (where supported)
- Separating instructions from data

## 5.2 Core Techniques
- Be explicit and specific: say what you want, not only what to avoid
- Provide context and motivation ("why"), since modern models use it
- **Role prompting**
- **Zero-shot vs few-shot prompting**, and choosing diverse, representative examples
- **Constraint prompting**: length, format, scope, forbidden actions
- **Output formatting** instructions
- **XML/JSON-style delimiters** (`<document>`, `<instructions>`) to separate sections
- Placing long documents at the top and the question at the end

## 5.3 Reasoning Techniques
- Chain-of-thought ("think step by step") and when it helps
- Structured thinking tags vs native reasoning models
- Self-consistency (sample several answers, then vote)
- Asking the model to quote evidence before answering (grounding)
- Letting the model say "I don't know"

## 5.4 Complex Tasks
- **Prompt decomposition**: split a big task into sub-tasks
- **Prompt chaining**: output of step A becomes input of step B
- Routing prompts (classify, then use a specialized prompt)
- Map-reduce over long documents

## 5.5 Prompts for Agents
- Writing agent system prompts: role, available tools, when to use each, stop conditions
- Tool-use guidance ("search before answering questions about X")
- Handling ambiguity: ask a clarifying question or make an assumption
- Persona and style consistency

## 5.6 Prompt Management
- Prompts as code: templates (Jinja2, f-strings), versioning in Git
- Prompt registries (LangSmith, Langfuse prompt management)
- A/B testing prompts
- **Evaluate every prompt change** against a test set (preview of Section 22)
- Prompt generators/optimizers (e.g. DSPy) — introduction

## 5.7 Prompt Injection Basics
- Direct injection ("ignore previous instructions")
- Indirect injection (instructions hidden inside documents or web pages)
- Why delimiters help but don't fully solve it
- Preview of the full treatment in Section 21

## 5.8 Model-Specific Differences
- Reading each provider's prompting guide
- Differences between reasoning and non-reasoning models (less "step by step" needed for reasoning models)
- Prompts written for one model often need tuning for another

---

## Hands-on Exercises
1. Write a support-bot system prompt. Improve it over 3 versions and score each against 15 test inputs.
2. Build a 3-step chain: extract facts → verify facts → write summary.
3. Hide a prompt injection inside a document and see whether your summarizer follows it.

## Project — Prompt Lab
A small tool that stores prompt versions in YAML, runs each version against a CSV of test cases, and outputs a comparison table (pass rate, tokens, latency).

## Resources
- Anthropic prompt engineering guide
- OpenAI prompt engineering guide
- Google Gemini prompting strategies

## Definition of Done
- [ ] Prompts live in version-controlled files, not scattered strings
- [ ] Every prompt change is measured on a test set
