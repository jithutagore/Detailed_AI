# 21 — Agent Security & Guardrails

> **Goal:** Build agents that stay safe even when users, documents, websites or tools are malicious. This matters a great deal in production.
> **Change from original:** Added a dedicated **guardrails** section, the OWASP frameworks, red-teaming and the "lethal trifecta" model.

**Level:** Production · **Time:** 2 weeks · **Prerequisites:** 07, 17, 20

---

## Learning Objectives
- Identify agent-specific threats and attack paths
- Apply defense-in-depth: policy, permissions, sandboxing, guardrails, monitoring
- Red-team your own agents
- Handle secrets, PII and multi-tenant isolation correctly

---

## 21.1 Threat Landscape
- **Prompt injection** (direct)
- **Indirect prompt injection** (via documents, web pages, emails, tool results, memories)
- **Data leakage / exfiltration** (e.g. via rendered markdown image URLs, links, tool calls)
- **Tool poisoning** (malicious MCP tool descriptions)
- **Malicious documents** in RAG corpora
- **Excessive permissions / excessive agency**
- **Credential leakage** (secrets in prompts, logs or outputs)
- **SSRF** (the agent fetches internal URLs)
- **Unauthorized tool execution**
- **Cross-user / cross-tenant data leakage**
- Jailbreaks
- Denial of wallet (cost-exhaustion attacks)
- Supply-chain risks (malicious packages, models, MCP servers)
- Memory poisoning

## 21.2 Frameworks & References
- **OWASP Top 10 for LLM Applications**
- **OWASP guidance for agentic AI threats**
- MITRE ATLAS
- NIST AI Risk Management Framework
- **The "lethal trifecta"** (Simon Willison): private data + untrusted content + the ability to communicate externally. Never combine all three without strong controls.

## 21.3 Security Architecture
```
User
 ↓
Input Guardrails (injection detection, PII, policy)
 ↓
Agent
 ↓
Policy Layer (what is this agent allowed to do, for this user?)
 ↓
Permission Check (user-scoped auth, approval if high risk)
 ↓
Tool (sandboxed, least privilege, validated args)
 ↓
External System
 ↓
Output Guardrails (PII, secrets, groundedness, content policy)
 ↓
Audit Log
```

## 21.4 Core Defenses
- **Least privilege** (tools and credentials scoped per user and task)
- **Sandboxing** code execution (Docker, gVisor, Firecracker, E2B, Modal)
- **Tool allowlists** and domain allowlists (egress control)
- **Input validation** (schemas, URL checks against private IP ranges for SSRF)
- **Output validation** (schemas, no secrets, safe markdown rendering)
- **Secrets management** (Vault, cloud secret managers; secrets never enter the LLM context)
- **Rate limiting** and cost caps per user
- **Audit logging** (immutable, complete)
- Separating trusted instructions from untrusted data (spotlighting, delimiters, data marking)
- Design patterns for injection resistance: dual-LLM pattern, plan-then-execute with a fixed plan, CaMeL-style capability tracking
- Human approval for sensitive actions (Section 20)

## 21.5 Guardrails *(added)*
- Input rails: topic restriction, jailbreak/injection classifiers, PII detection
- Output rails: toxicity, PII, hallucination/groundedness, format validation
- Tool rails: argument validation, policy checks before execution
- Tools: **NVIDIA NeMo Guardrails**, **Guardrails AI**, **Llama Guard / Prompt Guard**, Microsoft Presidio (PII), provider moderation APIs, OpenAI Agents SDK guardrails, LangChain middleware
- Trade-offs: latency, false positives, cost

## 21.6 Multi-Tenancy & Data Security
- Tenant-scoped vector search (filters enforced server-side, never chosen by the LLM)
- Row-level security in Postgres
- Per-tenant encryption keys (concept)
- Data retention and deletion

## 21.6b Agent Identity & Delegated Authorization *(added)*
- Agents as **non-human identities** (NHIs): each agent or agent instance should have its own identity, not a shared admin key
- **Acting on behalf of a user**: the agent's permissions = the intersection of the user's permissions and the agent's allowed scope, never more
- OAuth patterns:
  - Authorization code flow for the user to consent to the agent accessing their data
  - **Token exchange** (RFC 8693) for downscoped, delegated tokens
  - Client credentials for agent-only (no user) tasks
  - Short-lived tokens, refresh handling, per-tool scopes
- Credential brokering: the harness/tool layer holds tokens; **the LLM never sees them**
- Token vaults / managed agent-auth services (e.g. from identity providers and agent platforms)
- MCP authorization (Section 17) as one concrete instance
- Just-in-time and time-bound access for high-risk actions
- Revocation: kill switch per agent, per user, per tool
- Attribution in audit logs: *which agent*, *on behalf of which user*, *with which approval*, did what
- Multi-agent chains: propagating (and narrowing) authority through sub-agents without privilege escalation
- Exercise: give your Personal Productivity Agent (29, Lab 9) per-user Google OAuth with minimal scopes, token storage outside the LLM, and a revocation endpoint

## 21.7 Red-Teaming & Testing
- Manual red-teaming playbook
- Automated tools: **Promptfoo** red-team, **Garak**, **PyRIT**
- Injection test suites in CI
- Bug bounty mindset

---

## Hands-on Exercises
1. Attack your Section 09 RAG agent with a poisoned document that tries to exfiltrate data via a markdown image link. Then fix it.
2. Add SSRF protection to your web-fetch tool.
3. Run Promptfoo red-teaming against your Customer Support Agent.

## Project — Secure the Customer Support Agent
- Threat model document (assets, threats, mitigations)
- Input and output guardrails
- Policy layer + per-user permissions
- Sandboxed tools, secrets in a secret manager
- Red-team report (before/after)

## Definition of Done
- [ ] A written threat model
- [ ] Injection test suite in CI
- [ ] No secrets in prompts or logs (verified)
