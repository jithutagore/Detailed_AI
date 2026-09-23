# 20 — Human-in-the-Loop (HITL)

> **Goal:** Make sure production agents never blindly perform high-impact actions. Design approval, escalation and review flows that keep humans in control without slowing everything down.

**Level:** Production · **Time:** 1 week · **Prerequisites:** 14

---

## Learning Objectives
- Classify actions by risk and set permission levels
- Implement interrupt/resume approval workflows
- Design escalation paths and review UIs
- Use human feedback to improve the agent

---

## 20.1 Why HITL
- Irreversible actions (payments, emails, deletions, deployments)
- Regulatory requirements (finance, healthcare, HR decisions)
- Low model confidence or ambiguous input
- Building trust gradually (moving from suggesting to acting)

## 20.2 Risk Classification
| Level | Example | Policy |
|---|---|---|
| Read-only | Search, lookup | Auto |
| Low-impact write | Draft email, create a note | Auto + log |
| Medium | Send email to a customer, update CRM | Approval, or auto above a confidence threshold |
| High | Refund > $500, delete data, production deploy | Always requires approval (possibly two people) |

## 20.3 Patterns
- **Approval workflows** (approve / reject)
- **Edit before execute** (the human modifies tool arguments)
- **Interrupt/resume** (pause the graph and persist state; resume hours later)
- **Permission levels** per user, tool and amount
- **Escalation** (hand the conversation to a human agent)
- **Human review** (post-hoc sampling of completed actions)
- **Action confirmation** in chat ("I'm about to send X. Confirm?")
- Ask-for-clarification (the agent asks instead of guessing)
- Human as a tool (the agent can call `ask_human`)

## 20.4 Implementation
- LangGraph `interrupt()` + checkpointer + `Command(resume=...)`
- LangChain HITL middleware
- OpenAI Agents SDK / Claude Agent SDK permission modes and hooks
- Async approvals: Slack/Teams/email notifications with approve buttons, approval queues in a web UI
- Timeouts on pending approvals (auto-reject or escalate)
- Audit trail: who approved what, when, and with which edits

## 20.5 UX for Approvals
- Show the reviewer exactly what will happen (diff, amount, recipient)
- Show the agent's reasoning and sources
- Batch approvals
- Avoid approval fatigue (rubber-stamping)

## 20.6 Learning from Humans
- Capture approvals, edits and rejections as labeled data
- Feed corrections into eval sets and few-shot examples
- Gradually raise auto-approval thresholds as accuracy is proven

---

## Example
```
Agent
 ↓
Generate refund
 ↓
Amount > $500?  ── NO ──→ Execute + log
 ↓ YES
Human Approval (Slack button, 24h timeout)
 ↓ approved / edited / rejected
Execute (idempotent) → Audit log
```

## Project — Refund Approval Agent
- LangGraph agent processes refund requests
- Policy engine decides auto vs approval
- Approval UI (simple web page or Slack) with edit capability
- Resumes correctly after a server restart
- Full audit log table

## Definition of Done
- [ ] No high-risk action can execute without an approval record
- [ ] Pending approvals survive restarts
- [ ] Edits and rejections are stored as feedback data
