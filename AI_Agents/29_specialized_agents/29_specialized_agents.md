# 29 — Specialized Agents (Build Labs)

> **Goal:** Practice domain-specific agent patterns as short, focused build labs (3–5 days each).
> **Change from original:** Phase 20 overlapped with the capstones and earlier projects. It's now a set of labs, each teaching a specific pattern. Voice and coding moved to Sections 27–28. The capstones (Section 32) are the big portfolio projects.

**Level:** Specialization · **Time:** 2–3 weeks (pick 4+ labs) · **Prerequisites:** 14, 22

---

## Lab 1 — Deep Research Agent
```
Search → Read → Compare → Verify → Report
```
**Pattern taught:** parallel sub-agents + source verification
- Breadth-first search planning, parallel readers
- Claim–source mapping, conflict detection
- Report with inline citations
- Eval: citation precision, coverage

## Lab 2 — SQL / Data Analyst Agent
```
Question → Schema discovery → SQL generation → SQL validation → Execution → Analysis (+ chart)
```
**Pattern taught:** safe code generation against real systems
- Schema retrieval for large databases (relevant tables only)
- Few-shot examples of domain queries, semantic layer / metric definitions
- Validation: read-only user, `EXPLAIN`, row limits, allowlisted tables
- Self-correction from SQL errors
- Eval: execution accuracy on 30 questions (compare result sets, not SQL text)

## Lab 3 — Customer Support Agent (Omnichannel)
```
Email/Chat → Classification → RAG → Action (tools) → Human escalation
```
**Pattern taught:** policy-constrained actions
- Policy documents as retrieval sources
- Action tools with limits (refund caps)
- Sentiment-based escalation
- Eval: τ-bench style (policy adherence + correct final DB state)

## Lab 4 — Finance Workflow Agent
```
Documents → Extraction → Validation → Transaction lookup → Risk rules → Human approval
```
**Pattern taught:** deterministic rules + LLM judgment
- Vision extraction of invoices/statements (Section 19)
- Cross-validation against ledger or transaction data
- Rule engine for hard rules; the LLM only for fuzzy judgment
- Full audit trail (Section 30)

## Lab 5 — DevOps / SRE Agent
**Pattern taught:** read-heavy investigation with gated remediation
- Tools: logs (Loki/CloudWatch), metrics (Prometheus), Kubernetes (read-only), runbooks via RAG
- Incident summary + root-cause hypothesis
- Remediation actions behind approval

## Lab 6 — Sales / CRM Agent
**Pattern taught:** personalization + external data enrichment
- Lead research (web + CRM), drafting outreach, updating the CRM
- Per-user OAuth tokens for CRM access

## Lab 7 — Document Workflow Agent (Legal/HR/Compliance)
**Pattern taught:** long-document analysis + structured comparison
- Contract clause extraction, comparison against a playbook, risk flagging
- Redlining suggestions with citations to clauses

## Lab 8 — Data Pipeline / ETL Agent
**Pattern taught:** code-writing agent for data tasks
- Generates and runs pandas/SQL transformations in a sandbox
- Data-quality checks and a validation report

## Lab 9 — Personal Productivity Agent (Email + Calendar)
**Pattern taught:** multi-tool orchestration with user-scoped OAuth
- Inbox triage, meeting scheduling, drafting replies, a daily brief
- Background/scheduled execution

---

## Each Lab Must Include
- [ ] Architecture diagram
- [ ] A small eval set (10–20 cases)
- [ ] Tracing
- [ ] Safety controls appropriate to the domain
- [ ] A short write-up: what worked, what failed, next steps
