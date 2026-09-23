# 25 — Cost Optimization & Model Selection

> **Goal:** Deliver the same quality at a fraction of the cost and latency.
> **Change from original:** Added **fine-tuning / distillation** and a **model-selection method**.

**Level:** Production · **Time:** 1 week · **Prerequisites:** 04, 22, 23

---

## Learning Objectives
- Measure cost per task and find the biggest cost drivers
- Route tasks to the cheapest model that passes your evals
- Use caching, batching and context reduction
- Decide between prompting, RAG and fine-tuning

---

## 25.1 Cost Anatomy
- Input vs output vs cached token pricing
- Reasoning/thinking tokens (billed, often invisible)
- Cost multipliers in agents (each step re-sends the whole context)
- Tool and infrastructure costs (search APIs, vector DB, sandboxes)
- Cost per successful task (the real metric)

## 25.2 Techniques
- **Model routing**
- **Small vs large models** (and when a small model is enough)
- **Prompt caching** (stable prefixes; cache-friendly prompt layout)
- **Semantic caching** (reusing answers to similar questions; GPTCache, Redis semantic cache) and its correctness risks
- **Context reduction** (Section 12)
- **Tool-call reduction** (better tool design, batching lookups)
- **Batch processing** (batch APIs for offline work)
- **Token budgeting** (per-request and per-user caps)
- Output length control
- Reasoning effort / thinking budget tuning
- Early exit (stopping when confident)
- Self-hosting open models: when the maths favors it (GPU cost, utilization)

## 25.3 Routing Architecture
```
Incoming task
  ↓
Router (rules, a classifier, or a small LLM)
  ├── Easy task    → Small / fast model
  ├── Medium task  → Mid-tier model
  └── Complex task → Frontier / reasoning model
  ↓
Quality check → escalate to a bigger model if it fails (cascade)
```
- Routers: RouteLLM concepts, LiteLLM routing, custom classifiers
- Cascading (try cheap first, escalate on low confidence)

## 25.4 Model Selection Method
1. Define the task and a success metric
2. Build an eval set (Section 22)
3. Test 3–5 candidate models
4. Plot quality vs cost vs latency (Pareto frontier)
5. Choose, and re-evaluate when new models are released

## 25.5 Fine-tuning & Distillation *(added)*
- **When to fine-tune** vs prompt engineering vs RAG
- Fine-tuning for format, style, tool-use reliability and domain classification
- **Distillation**: a large model's outputs train a small model
- Techniques: LoRA / QLoRA, full fine-tuning (concept), preference tuning (DPO)
- Tools: Hugging Face TRL, Unsloth, Axolotl, provider fine-tuning APIs
- Data preparation from production traces
- Evaluating fine-tuned models against the base model

---

## Project — Cut Costs by 50%+ Without Losing Quality
Take your Enterprise Research Agent (10) or Support Agent (14):
- Baseline: cost/task, latency, quality
- Apply routing, caching, context reduction and batching
- Optional: fine-tune a small model for the classifier step
- Report: before/after table plus a Pareto chart

## Definition of Done
- [ ] Cost per successful task reduced, with quality within 2% of baseline
- [ ] The routing decision is logged per request
