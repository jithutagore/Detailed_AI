# 24 — Reliability Engineering

> **Goal:** Keep agents working when models, tools and networks fail, which they will.
> **Change from original:** Added **durable execution** for long-running agents.

**Level:** Production · **Time:** 1–2 weeks · **Prerequisites:** 02, 14, 23

---

## Learning Objectives
- Apply classic reliability patterns to LLM and tool calls
- Recover state after crashes
- Run long-running agents durably
- Degrade gracefully instead of failing silently

---

## 24.1 Failure Modes in Agents
- LLM API outages, rate limits, overload errors
- Slow responses and timeouts
- Invalid structured output
- Tool failures (API down, bad data)
- Infinite loops and stuck agents
- Partial completion (half the actions done)
- Process crashes mid-run
- Silent quality degradation (model update, data drift)

## 24.2 Patterns
- **Retries** (only for retryable errors)
- **Exponential backoff** with jitter
- **Timeouts** (per call, per step, per run)
- **Circuit breakers** (stop calling a failing dependency)
- **Fallback models** (different provider or model size)
- **Tool fallback** (alternative data source)
- **Structured error handling** (typed errors, errors as observations for the LLM)
- **State recovery** (checkpoints, resume from the last good step)
- **Idempotency** (idempotency keys for write tools, so a retry doesn't double-refund)
- **Dead-letter queues** (failed jobs kept for inspection)
- **Rate limiting** (client-side token buckets per provider)
- Bulkheads (isolating resources per tenant or feature)
- Hedged requests (race two providers on latency-critical paths)
- Compensation / saga pattern (undoing earlier steps when a later step fails)

## 24.3 Durable Execution *(added)*
- Why long-running agents need durability (hours-long tasks, human approvals that take days)
- **Temporal**, Restate, Inngest, DBOS; AWS Step Functions (concept)
- LangGraph durable execution + Postgres checkpointer
- Queues: Celery, Redis Streams, SQS, Kafka
- Exactly-once vs at-least-once semantics

## 24.4 Graceful Degradation
- Partial answers with clear disclaimers
- "I couldn't complete X; here's what I did"
- Human escalation as the final fallback
- Feature flags / kill switches for agent capabilities

## 24.5 Reliability Testing
- Fault injection (mock 429s, timeouts, bad JSON)
- Chaos testing tool dependencies
- Load testing (Locust, k6)
- SLOs for agents (availability, latency, task success)

---

## Example
```
Agent
 ↓
Primary LLM
 ↓ failure (retry ×3 with backoff)
Fallback LLM (other provider)
 ↓ failure
Human escalation + DLQ entry + alert
```

## Project — Hardened Agent Service
- Wrap your agent with retries, circuit breakers and a provider fallback
- Idempotent write tools with idempotency keys
- Long-running report generation using Temporal **or** a LangGraph + Postgres checkpointer, surviving a `kill -9` mid-run
- Fault-injection test suite
- SLO document

## Definition of Done
- [ ] The agent survives a primary-provider outage
- [ ] No duplicate side effects on retry (tested)
- [ ] Crash recovery demonstrated
