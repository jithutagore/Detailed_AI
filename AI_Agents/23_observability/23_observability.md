# 23 — Observability

> **Goal:** See exactly what your agent did, why, how long it took and what it cost, in development and in production.
> **Note:** Tracing should be switched on from Section 08 onward. This section covers it in depth.

**Level:** Production · **Time:** 1 week · **Prerequisites:** 08, 22

---

## Learning Objectives
- Instrument agents with traces and spans
- Monitor latency, tokens, cost, errors and quality
- Build dashboards and alerts
- Use traces for debugging and for building eval datasets

---

## 23.1 What to Trace
```
Request
 ↓
LLM call (prompt, response, model, tokens, latency, cost)
 ↓
Tool call (name, args, duration, status)
 ↓
Tool response (size, truncated?)
 ↓
RAG retrieval (query, doc IDs, scores)
 ↓
Another LLM call
 ↓
Final response (+ user feedback)
```
- Traces, spans, parent/child relationships
- Session / thread / user IDs linking traces together
- Metadata: prompt version, model version, environment, tenant

## 23.2 What to Monitor
- **Latency** (TTFT, total, per step; P50/P95/P99)
- **Tokens** (input, output, cached)
- **Cost** (per request, user, tenant, feature)
- **Errors** (LLM API errors, tool failures, validation failures)
- **Tool calls** (frequency, failure rate)
- **Retrieval quality** (score distributions, empty results)
- **Agent trajectory** (steps per task, loops, max-step hits)
- Quality scores from online evals
- User feedback

## 23.3 Standards
- **OpenTelemetry** (traces, metrics, logs)
- **OpenTelemetry GenAI semantic conventions**
- OpenInference / OpenLLMetry instrumentation libraries

## 23.4 Tools & Ecosystems
- **LangSmith** (LangChain/LangGraph native, also framework-agnostic)
- **Langfuse** (open source, self-hostable)
- **Arize Phoenix**
- Braintrust, Helicone, W&B Weave, Datadog LLM Observability
- **Prometheus** (metrics) + **Grafana** (dashboards)
- Structured logs → Loki / ELK

## 23.5 Practices
- Sampling strategies (100% in dev, sampled in production, 100% of errors)
- PII redaction in traces
- Data retention
- Alerts: error rate, cost spikes, latency, quality drops
- Trace-to-dataset: turning failing production traces into eval cases
- Debugging workflow: find the bad trace → locate the step → reproduce → fix → add to evals

---

## Project — Full Observability Stack
- Instrument the Customer Support Agent with OpenTelemetry + Langfuse (or LangSmith)
- Grafana dashboard: requests, P95 latency, cost/day, error rate, tool failure rate
- Alert when cost/hour > threshold or error rate > 5%
- PII-redacted traces
- One documented debugging session: bug found through a trace, then fixed

## Definition of Done
- [ ] Every production request is traceable end to end
- [ ] Cost per tenant visible
- [ ] Alerts configured and tested
