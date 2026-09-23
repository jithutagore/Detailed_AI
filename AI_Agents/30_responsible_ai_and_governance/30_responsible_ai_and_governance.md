# 30 — Responsible AI & Governance  *(NEW section)*

> **Goal:** Build agents that meet legal, ethical and organizational requirements, especially in regulated domains like finance, healthcare and HR.
> **Why added:** Enterprise and regulated deployments (e.g. your Finance Workflow capstone) need governance, and the original syllabus didn't cover it.

**Level:** Architect · **Time:** 1 week · **Prerequisites:** 20, 21, 22

---

## Learning Objectives
- Understand the main regulations and standards that affect AI agents
- Implement privacy, transparency and accountability controls
- Create governance documentation for an agent system

---

## 30.1 Regulations & Standards (overview, not legal advice)
- **EU AI Act**: risk categories, obligations for high-risk systems, transparency duties, general-purpose AI rules
- **GDPR / data protection**: lawful basis, data minimization, right to erasure, automated decision-making (Art. 22)
- India's **DPDP Act 2023**, and other regional laws relevant to you
- Sector rules: finance (model risk management, e.g. SR 11-7 style), healthcare (HIPAA), employment
- **NIST AI RMF**, **ISO/IEC 42001** (AI management systems)
- SOC 2 considerations for AI products

## 30.2 Privacy
- PII detection and redaction (Presidio)
- Data minimization in prompts, logs and memories
- Data residency, and provider data-retention settings (zero data retention)
- Consent and user notice
- Right to be forgotten across memory, vector stores, traces and backups

## 30.3 Transparency & Accountability
- Disclosing that users are talking to an AI
- Explaining agent decisions (reasoning summaries, sources)
- **Audit logs**: who/what/when/why for every action
- Decision records for high-impact actions
- Model cards / system cards for your agent
- Clear ownership (RACI) for agent behavior

## 30.4 Fairness & Harm
- Bias testing for decisions that affect people (loans, hiring, support prioritization)
- Content safety and misuse prevention
- Accessibility

## 30.5 Governance Processes
- AI use-case intake and risk assessment
- Pre-deployment review (evals, red-team, legal, security)
- Change management for prompts and models
- Incident response for AI failures
- Ongoing monitoring and periodic re-evaluation
- Vendor/model provider due diligence

---

## Deliverable — Governance Pack for Your Finance Workflow Agent
- Risk assessment (EU AI Act category + rationale)
- Data flow diagram with PII marked
- System card (purpose, limitations, eval results, known failure modes)
- Audit log schema
- Human oversight design
- Incident response runbook

## Definition of Done
- [ ] Governance pack completed for one capstone
- [ ] A PII erasure request executed end to end (demonstrated)
