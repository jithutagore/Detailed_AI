# 22 — Agent Evaluation & Testing

> **Goal:** Prove your agent works, and keep proving it after every change. A demo that works once is not success.
> **Change from original:** Added **software testing of agents** (mocks, CI) alongside evaluation. Evaluation should also start early: you've been building small eval sets since Section 06. This section formalizes them.

**Level:** Production · **Time:** 2 weeks · **Prerequisites:** 06, 08, 09

---

## Learning Objectives
- Evaluate responses, tool use, retrieval and trajectories
- Build datasets, evaluators and regression tests
- Use LLM-as-judge correctly (and validate the judge)
- Run evals in CI

---

## 22.1 Evaluation Types
| Type | Question |
|---|---|
| **Response evaluation** | Was the final answer correct and helpful? |
| **Tool evaluation** | Did the agent select the right tool with the right arguments? |
| **Retrieval evaluation** | Did retrieval return useful documents? |
| **Trajectory evaluation** | Did the agent take a sensible sequence of actions? |
| **Safety evaluation** | Did it resist injection and refuse harmful actions? |
| **Outcome / state evaluation** | Is the final state of the world correct (DB row updated, file fixed, tests pass)? |

## 22.2 Metrics
**RAG**
- Recall@K, Precision@K, MRR, NDCG
- Context relevance, context precision
- Faithfulness / groundedness
- Answer relevance

**Agent**
- Task success rate
- Tool-call accuracy (selection + arguments)
- Tool-call count / steps (efficiency)
- Completion rate, failure rate
- Latency (P50/P95), cost per task
- pass@k (succeeds at least once in k tries) vs pass^k (succeeds every time in k tries)

**LLM output**
- Correctness, relevance, groundedness
- Hallucination rate
- Format compliance
- Tone and policy compliance

## 22.3 Evaluators
- Code-based (exact match, regex, schema, unit tests, SQL result comparison)
- **LLM-as-judge**: rubrics, pairwise comparison, reference-based vs reference-free
- Validating the judge against human labels (agreement rate)
- Judge biases: position, verbosity, self-preference
- Human evaluation: annotation queues, labeling guidelines
- Simulated users (a user-simulator LLM for multi-turn agents)

## 22.4 Datasets
- Golden datasets (hand-labeled)
- Synthetic data generation (and its risks)
- Collecting real failures from production traces
- Coverage: happy path, edge cases, adversarial, multi-turn
- Dataset versioning
- Error analysis: read traces, categorize failures, then fix the largest category first

## 22.5 Evaluation Framework
```
Dataset
   ↓
Agent (versioned: prompt + model + tools)
   ↓
Trace
   ↓
Evaluators (code + LLM judge + human)
   ↓
Metrics
   ↓
Regression Test (compare against the baseline; fail CI on regression)
```

## 22.6 Software Testing for Agents *(added)*
- Unit tests for tools, parsers, routing (no LLM)
- Mocked-LLM tests (fake model returning scripted tool calls)
- Recorded-response tests (VCR-style cassettes)
- Integration tests with real models (small, scheduled)
- Snapshot tests for prompts
- Flaky-test management (the model is non-deterministic, so run N times and set thresholds)
- CI/CD: evals on every PR that touches prompts or models

## 22.7 Tools
- **LangSmith** evaluations
- **Langfuse** datasets and scores
- **Ragas**, **DeepEval**, **Promptfoo**, **Braintrust**, **Arize Phoenix**, **Inspect AI** (UK AISI)
- OpenAI Evals
- Public agent benchmarks for context: SWE-bench, τ-bench (tau-bench), GAIA, WebArena, OSWorld, BFCL (Berkeley Function Calling Leaderboard)

## 22.8 Online Evaluation
- Evaluating production traffic (sampled LLM-judge scoring)
- User feedback signals (thumbs, edits, escalations)
- A/B testing agent versions
- Drift detection

---

## Project — Evaluation Harness for Your Customer Support Agent
- 100-case dataset (including 20 adversarial cases)
- Code evaluators + a validated LLM judge (≥ 85% agreement with your labels)
- Trajectory eval (expected tool sequence)
- GitHub Action that runs evals on every PR and posts a metrics table
- A dashboard showing metric trends over versions

## Definition of Done
- [ ] Every future change is measured against the baseline
- [ ] Judge validated against human labels
- [ ] Error-analysis doc with failure categories
