# 18 — Capstone Projects

> **Goal:** Build portfolio-grade deep learning projects that demonstrate architecture-level understanding, not just calling a pretrained model API. Each capstone should show you can justify every major design choice.

**Level:** Portfolio · **Time:** 4–6 weeks · **Prerequisites:** All core sections (01–09) + at least 2 applied sections (10–15)

---

## Required for EVERY Capstone
- [ ] A written architecture justification: why this architecture, not an alternative, for this problem
- [ ] At least one component implemented from a lower level than "just call the library function" (a custom layer, a from-scratch mechanism, or a from-scratch training loop)
- [ ] Full training diagnostics (Section 03's toolkit: loss curves, gradient monitoring, sanity checks)
- [ ] A baseline comparison (a simpler architecture or classical approach from `ML\`/`AI\`, per this folder's recurring theme)
- [ ] Model optimization applied and measured (Section 16), even if minimal
- [ ] README with architecture diagram, training curves, results table, and sample outputs

---

## Capstone 1 — Vision System End-to-End
**Domain:** pick one — defect detection, medical image classification, wildlife/species identification, or a domain of your choice.
**Features:** a from-scratch CNN (Section 04) compared against a transfer-learned model (Section 05), object detection or segmentation if the domain calls for it (Section 13), Grad-CAM explanations, and a quantization/pruning pass (Section 16) with a documented accuracy-efficiency trade-off.
**Stretch:** deploy as a small web demo (a FastAPI endpoint, link to `AI_Agents\02`'s backend skills).
**Shows:** the full CNN → transfer learning → application → optimization pipeline.

## Capstone 2 — Language Understanding System
**Domain:** pick one — a domain-specific text classifier, an NER/extraction system, or a semantic search engine.
**Features:** a classical baseline (`ML\16`), an LSTM baseline (Section 06), and a fine-tuned Transformer encoder (Section 08) — a genuine three-way comparison with real numbers. Include a sentence-embedding-based retrieval component (Section 08.5).
**Stretch:** distill the fine-tuned model into a smaller, faster student (Section 16.4) and measure the trade-off.
**Shows:** understanding of the full NLP architecture progression and honest empirical comparison across it.

## Capstone 3 — Build a Small GPT, Fully From Scratch
**Domain:** language modeling / text generation.
**Features:** implement a complete decoder-only Transformer from primitives (extending Section 07's and 09's projects) — embeddings, positional encoding, multi-head causal self-attention, feed-forward blocks, and the full training loop with mixed precision (Section 17) and gradient accumulation if needed. Train on a text corpus of your choice, implement multiple decoding strategies, and (optionally) fine-tune with LoRA for a specific style or instruction-following behavior (Section 09.5).
**Stretch:** implement your own simplified KV cache for faster inference and benchmark the speedup.
**Shows:** the deepest possible understanding of exactly what an LLM is, mechanically — this project is the strongest possible preparation for everything in `AI_Agents\`.

## Capstone 4 — Generative Model Portfolio
**Domain:** image generation.
**Features:** train a VAE, a GAN, and a (small, conditional) diffusion model (Sections 10–11) on the same dataset, with a rigorous comparison (sample quality via FID, training stability, mode coverage, controllability). Optionally fine-tune a pretrained Stable Diffusion pipeline with LoRA or DreamBooth-style personalization on a custom small dataset.
**Shows:** the full landscape of generative modeling approaches and hands-on understanding of why diffusion models became dominant.

## Capstone 5 — Speech System (recommended given your background)
**Domain:** ASR or TTS for a specific language, accent, or domain.
**Features:** fine-tune a pretrained model (Whisper-family for ASR, or a Tacotron/FastSpeech-family model for TTS, Section 15) on domain-specific or low-resource data; report WER (ASR) or a structured quality assessment (TTS); apply model optimization (Section 16) for a latency-sensitive deployment target.
**Stretch:** wire the trained model into a minimal working voice interaction loop, directly connecting to `AI_Agents\28_voice_agents`'s architecture.
**Shows:** deep learning applied to your area of specialization, with a direct, practical bridge into the AI_Agents voice content.

## Capstone 6 — Deep RL Agent
**Domain:** a game-playing or control agent.
**Features:** implement DQN and PPO (Section 12) on a shared environment, with a full ablation study of each algorithm's key stabilization techniques (experience replay, target networks, PPO's clipping). Write an explicit comparison connecting your PPO implementation's mechanics to RLHF and to `AI_Agents\34`'s agentic RL/GRPO content.
**Shows:** the RL foundation that underlies modern LLM alignment and agentic training techniques.

---

## Portfolio Presentation
For each capstone, publish:
1. GitHub repo (clean code, tests where applicable, clear README)
2. Architecture diagram (the actual network structure, not just a system diagram)
3. Training curves and a results table, including your required baseline comparison
4. A short write-up: what architecture choice mattered most, what you'd change with more time/compute, and how the project connects forward to `AI_Agents\`

## Suggested Timeline (per capstone)
| Week | Activity |
|---|---|
| 1 | Architecture design, baseline implementation |
| 2 | Main model implementation and initial training |
| 3 | Debugging, tuning, and the required baseline comparison |
| 4 | Optimization pass (Section 16), evaluation depth |
| 5 | Stretch goals, deployment demo if applicable |
| 6 | Write-up, diagrams, polish |

## How This Connects Forward
- Capstone 3 is the most direct, deliberate bridge into `AI_Agents\03_llm_foundations` — build it before moving into that folder if you haven't already
- Capstone 5 connects directly to `AI_Agents\28_voice_agents`
- Capstone 6 connects directly to `AI_Agents\34_agent_environments_and_agentic_rl`
- The model optimization and scale-training skills (Sections 16–17) transfer directly to any future LLM Engineering folder's training/serving content
