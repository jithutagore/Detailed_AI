# 10 — Capstone Projects

> **Goal:** Build portfolio-grade LLM engineering projects that demonstrate you can take a base model through the full pipeline — fine-tuning, alignment, evaluation, compression, and serving — and justify every decision with measured trade-offs, not just working code.

**Level:** Portfolio · **Time:** 3–5 weeks · **Prerequisites:** All of Sections 01–09

---

## Required for EVERY Capstone
- [ ] A written justification for every major technique choice: why this fine-tuning method, this alignment approach, this quantization format, over the alternatives, for this problem
- [ ] At least one component implemented from a lower level than "just call the library function" (e.g. LoRA's forward pass, DPO's loss, a from-scratch tokenizer)
- [ ] A rigorous evaluation suite (Section 06): standard benchmark subset where applicable, a custom task-specific eval set, and LLM-as-judge with bias mitigations where relevant
- [ ] A baseline comparison (the base model prompted, and/or a simpler technique) with real numbers, not assumptions
- [ ] Measured compute/memory/cost trade-offs for every technique applied (LoRA vs. full fine-tune, quantized vs. full precision, serving configuration)
- [ ] README with a pipeline diagram, training/eval curves, a results table, and sample outputs

---

## Capstone 1 — Full Fine-Tuning Pipeline: Base to Aligned, Served
**Domain:** pick a concrete task or assistant persona of your choice.
**Features:** take an open-weight base model through the complete pipeline — SFT (Section 03) with a hand-built dataset, PEFT via LoRA/QLoRA (Section 04), preference alignment via DPO (Section 05), a full evaluation suite (Section 06) at every stage, quantization for deployment (Section 07), and serving with a production engine (Section 08).
**Stretch:** serve multiple task variants as swappable LoRA adapters against one shared quantized base model.
**Shows:** the complete, real-world LLM engineering pipeline end-to-end, with every stage measured.

## Capstone 2 — Domain or Low-Resource-Language Specialist Model
**Domain:** pick one — a specialized professional domain (legal, medical, financial) or an underrepresented language.
**Features:** tokenizer adaptation and efficiency measurement (Section 01, 09.2), continued pretraining if justified (Section 02.6), SFT and DPO on domain/language-specific data, an expert- or native-speaker-reviewed evaluation suite (Section 09.4), and a retrieval-aware fine-tuning component (Section 09.5) integrated with a small RAG pipeline (link to `AI_Agents\09`).
**Stretch:** publish the adapted model and dataset with a model card documenting known limitations.
**Shows:** the full domain/language adaptation decision process, applied honestly, including where it didn't fully close the gap.

## Capstone 3 — Small Model From Scratch: Pretrain Through Deployment
**Domain:** language modeling on a corpus of your choice.
**Features:** extend `Deep_Learning\09`'s and this folder's Section 02 from-scratch pretraining project into a fully productionized small model — proper tokenizer (Section 01), modern architecture (RoPE/RMSNorm/SwiGLU/GQA, Section 02.2), scaling-law-informed sizing (Section 02.3), SFT and lightweight alignment on top of your own pretrained base, and quantized deployment.
**Stretch:** compare your from-scratch small model against an equivalently-sized open-weight model on your eval suite, and explain the gap.
**Shows:** genuine end-to-end ownership of an LLM's lifecycle, from raw text to a served, aligned model.

## Capstone 4 — Efficient Serving and Compression Benchmark Suite
**Domain:** systems/performance engineering for LLM inference.
**Features:** take a fine-tuned model (yours or a public one) and build a rigorous compression-and-serving benchmark: multiple quantization formats and bit-widths (Section 07), continuous batching and PagedAttention-based serving (Section 08), speculative decoding, and multi-LoRA serving. Produce a full latency/throughput/cost/accuracy trade-off matrix across configurations.
**Stretch:** build a small auto-selection system that picks a serving configuration given a target SLA (max latency, min throughput) and cost budget.
**Shows:** production-grade systems thinking about the cost and performance side of LLM engineering — directly useful for `AI_Agents\25`'s cost-optimization decisions.

## Capstone 5 — Alignment and Evaluation Deep Dive
**Domain:** preference alignment research/engineering.
**Features:** build a preference dataset (human-annotated or synthetically generated with documented caveats, Section 01.6/05.6), train and compare a reward model + RLHF-with-PPO pipeline against a DPO pipeline on the *same* base model and data, and build a thorough evaluation suite including contamination checks (Section 6.3) and bias-mitigated LLM-as-judge win-rates (Section 6.4).
**Stretch:** implement a GRPO-style verifiable-reward training loop on a narrow task with checkable correctness (e.g. math or a simple tool-use task), bridging into `AI_Agents\34`.
**Shows:** deep, empirical understanding of the alignment landscape and rigorous evaluation practice — the strongest possible preparation for `AI_Agents\34_agent_environments_and_agentic_rl`.

---

## Portfolio Presentation
For each capstone, publish:
1. GitHub repo (clean code, tests where applicable, clear README)
2. A pipeline diagram (the actual stages your model went through, not just a system diagram)
3. Training/eval curves and a results table, including your required baseline comparison and measured trade-offs
4. A short write-up: what technique choice mattered most, what you'd change with more time/compute, and how the project connects forward to `AI_Agents\`

## Suggested Timeline (per capstone)
| Week | Activity |
|---|---|
| 1 | Pipeline design, data/tokenizer preparation, baseline |
| 2 | Core training (SFT/pretraining/PEFT) |
| 3 | Alignment and/or the capstone's specialized focus area |
| 4 | Evaluation suite, compression/serving pass |
| 5 | Stretch goals, write-up, diagrams, polish |

## How This Connects Forward
- Every capstone here assumes and extends `Deep_Learning\09` (GPT from scratch) and `Deep_Learning\17` (training at scale)
- Capstone 4 connects directly to `AI_Agents\25_cost_optimization_and_model_selection`
- Capstone 5 is the most direct, deliberate bridge into `AI_Agents\34_agent_environments_and_agentic_rl` — build it before or alongside that folder
- The domain-adaptation and RAG-integration work in Capstone 2 connects directly to `AI_Agents\09-10`
- Everything in this folder is what's actually running beneath the APIs taught in `AI_Agents\04_llm_apis_and_providers` — revisit that section after finishing these capstones and notice how much more of the API's behavior now makes sense
