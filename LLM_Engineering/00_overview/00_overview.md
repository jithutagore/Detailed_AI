# LLM Engineering — Syllabus Overview

This folder is the index for the **LLM Engineering** curriculum: how large language models are actually trained, aligned, evaluated, compressed, and served — the layer between "I understand how a Transformer/GPT works" and "I can build products on top of an LLM API."

**Scope:** tokenizer design, pretraining pipelines and scaling laws in practice, supervised fine-tuning, parameter-efficient fine-tuning (LoRA/QLoRA and friends), alignment (RLHF/DPO/GRPO), LLM-specific evaluation, quantization, and inference serving.
**Not in scope here:** how attention/Transformers/GPT work mechanically from primitives — see `Deep_Learning\07-09`; building agents, RAG, tools, and orchestration on top of a served model — see `AI_Agents\`.

---

## Why This Folder Exists

`Deep_Learning\09_gpt_and_decoder_models` teaches you to build a small GPT from scratch and mentions LoRA and scaling laws in passing. `AI_Agents\04_llm_apis_and_providers` and `AI_Agents\25_cost_optimization_and_model_selection` teach you to *consume* an already-trained, already-served model through an API. Neither folder teaches the middle layer: what it actually takes to turn a base Transformer into a deployed, aligned, efficient LLM. That's this folder.

```
Deep_Learning (architecture: how a Transformer/GPT is built)
        ↓
LLM ENGINEERING (this folder): tokenize → pretrain → fine-tune (SFT/PEFT) → align (RLHF/DPO) → evaluate → compress → serve
        ↓
AI_Agents (application: build agents/RAG/tools on top of a served model)
```

## Relationship to Your Other Folders
| Topic | Where it lives |
|---|---|
| Transformer/attention mechanics, GPT architecture from scratch | `Deep_Learning\07_attention_and_transformers`, `Deep_Learning\09_gpt_and_decoder_models` (this folder assumes both) |
| A first pass at LoRA, scaling laws | `Deep_Learning\09_gpt_and_decoder_models` (Section 09.5/09.3) — this folder goes much deeper on both |
| Mixed precision, distributed training mechanics (DDP, ZeRO, FSDP) | `Deep_Learning\17_training_at_scale` (this folder's Section 02 applies those techniques specifically to LLM pretraining) |
| Inference-time quantization/pruning basics | `Deep_Learning\16_model_optimization_and_efficiency` (this folder's Section 07 goes deeper, LLM-specific: GPTQ/AWQ/GGUF, KV-cache quantization) |
| Consuming LLM APIs, providers, rate limits, prompt caching | `AI_Agents\04_llm_apis_and_providers` (this folder teaches what's happening behind that API) |
| Cost optimization, choosing a model, when to fine-tune vs. prompt vs. RAG | `AI_Agents\25_cost_optimization_and_model_selection` (this folder gives you the fine-tuning mechanics that decision assumes you understand) |
| Agentic RL, GRPO, reward hacking, environments | `AI_Agents\34_agent_environments_and_agentic_rl` (this folder's Section 05 on RLHF/DPO/PPO is the prerequisite foundation) |
| Deep RL foundations (PPO mechanics) | `Deep_Learning\12_deep_reinforcement_learning` (prerequisite for this folder's Section 05) |

---

## Section Map

| # | Folder | Level | Suggested time |
|---|---|---|---|
| 01 | `01_tokenization_and_data_pipelines` | Foundation | 1–2 weeks |
| 02 | `02_pretraining_llms` | Foundation | 2–3 weeks |
| 03 | `03_supervised_fine_tuning` | Core | 2 weeks |
| 04 | `04_parameter_efficient_fine_tuning` | Core | 2 weeks |
| 05 | `05_alignment_rlhf_dpo` | Core | 2–3 weeks |
| 06 | `06_llm_evaluation_and_benchmarking` | Core | 1–2 weeks |
| 07 | `07_quantization_and_compression` | Production | 2 weeks |
| 08 | `08_inference_serving_and_optimization` | Production | 2 weeks |
| 09 | `09_domain_and_multilingual_adaptation` | Applied | 1–2 weeks |
| 10 | `10_capstone_projects` | Portfolio | 3–5 weeks |

**Total:** about 4–5 months part-time (10–15 hrs/week).

**Prerequisites for this folder as a whole:** `Deep_Learning\07` (Attention/Transformers), `Deep_Learning\09` (GPT/decoder models), `Deep_Learning\17` (Training at Scale) — at least skimmed, since Sections 01–02 here build directly on them.

---

## Learning Path

```
Tokenization & Data Pipelines → Pretraining LLMs
   ↓
Supervised Fine-Tuning → Parameter-Efficient Fine-Tuning (LoRA/QLoRA)
   ↓
Alignment (RLHF / DPO / GRPO) → LLM Evaluation & Benchmarking
   ↓
Quantization & Compression → Inference Serving & Optimization
   ↓
Domain & Multilingual Adaptation → Capstones
   ↓
                                            forward into AI_Agents\25 (cost/model selection)
                                            and AI_Agents\34 (agentic RL, GRPO)
```

### Core track (if time is short)
01 → 03 → 04 → 05 → 06 → 08. Section 02 (full pretraining) is the most resource-heavy and least commonly needed hands-on — most practitioners fine-tune, never pretrain from scratch (same point `Deep_Learning\17.8` makes). Read it for understanding even if your hands-on project only does the small-scale version.

### Why Sections 03–05 matter most
Given that most real-world LLM engineering work is fine-tuning and aligning an existing base model rather than pretraining one, **Section 03 (SFT) → 04 (PEFT/LoRA/QLoRA) → 05 (RLHF/DPO)** is the single most practically useful arc in this folder — it's what "fine-tune a model for X" means in an actual job.

---

## Habits to Keep Throughout
- **Always work with small models first** (e.g. GPT-2-small, a 1–3B open-weight model) so experiments are fast and cheap; scale up only once the pipeline is correct.
- **Track every training run** (Weights & Biases or equivalent) — loss curves, learning rate schedule, eval metrics over time.
- **Keep a held-out eval set from day one** — don't just watch training loss; watch task performance.
- **Measure compute/memory/cost explicitly** for every technique (LoRA vs. full fine-tune, quantized vs. full precision) — the trade-off is the point.
- **Publish each project on GitHub** with a README, training curves, and a before/after comparison.

---

## Guiding Principle

> A pretrained base model is a general-purpose next-token predictor, not a product. Every technique in this folder — SFT, PEFT, RLHF/DPO, quantization, serving optimization — exists to close a specific, nameable gap between "predicts plausible text" and "is a usable, affordable, aligned, deployable system." Learn each technique by learning exactly which gap it closes.
