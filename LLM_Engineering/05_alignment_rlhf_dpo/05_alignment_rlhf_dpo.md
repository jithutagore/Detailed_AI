# 05 — Alignment: RLHF, DPO, and GRPO

> **Goal:** Understand how models are aligned to human preferences beyond what supervised fine-tuning alone achieves — the techniques that turn an instruction-following model into one that reliably prefers helpful, safe, well-formed responses.

**Level:** Core · **Time:** 2–3 weeks · **Prerequisites:** Section 03, `Deep_Learning\12_deep_reinforcement_learning`

---

## Learning Objectives
- Explain why SFT alone is insufficient and what preference-based alignment adds
- Describe the RLHF pipeline (reward model + PPO) end-to-end
- Explain DPO as a simpler alternative to RLHF and implement it
- Understand GRPO and how alignment techniques extend into agentic RL

---

## 5.1 Why SFT Isn't Enough
- SFT teaches the model to imitate demonstrations, but demonstrations don't capture *preferences between* outputs (this response is better than that one, not just "here's a good one")
- The core alignment problem: getting a model to prefer outputs humans actually prefer, including subtle qualities SFT data doesn't directly teach (helpfulness, honesty, harmlessness)
- Recap `AI_Agents\30`'s responsible-AI content — alignment is the training-side mechanism behind those governance concerns

## 5.2 Reward Modeling
- Collecting human preference data: pairwise comparisons (A vs. B, which is better) rather than absolute scores, and why pairwise comparison is more reliable to collect
- Training a reward model: a classifier/regressor that scores a response, trained on the pairwise preference data via a Bradley-Terry-style loss
- Reward model failure modes: reward hacking (recap `AI_Agents\34`'s reward-hacking coverage), reward model overfitting, distribution shift between reward-model training data and the policy's actual outputs during RL

## 5.3 RLHF with PPO
- Recap `Deep_Learning\12`'s PPO mechanics (clipping, advantage estimation) — this section applies them specifically to LLM policy optimization
- The RLHF loop: the policy (the LLM) generates responses, the reward model scores them, PPO updates the policy to increase expected reward
- The KL-divergence penalty against the original SFT model: why it's needed (prevents the policy from drifting into reward-hacking degenerate text) and how it's weighted
- Why RLHF-with-PPO is complex and unstable in practice: four models in memory at once (policy, reference, reward model, value model), sensitive hyperparameters, expensive

## 5.4 DPO (Direct Preference Optimization)
- The key insight: preference data can be used to directly optimize the policy with a closed-form loss derived from the RLHF objective, without training a separate reward model or running RL at all
- DPO's loss function and how it implicitly represents a reward model
- Why DPO became popular: simpler pipeline (two models instead of four), more stable training, comparable results to RLHF-with-PPO on many tasks
- DPO variants: IPO, KTO (using unpaired binary "good/bad" feedback instead of pairwise comparisons), and when each is preferable

## 5.5 GRPO and the Bridge to Agentic RL
- Group Relative Policy Optimization: replacing PPO's learned value model with a simpler baseline computed from a group of sampled responses to the same prompt
- Why this matters for reasoning models and agentic tasks: reward signals that come from verifiable outcomes (correct/incorrect, passed/failed a test) rather than a learned reward model
- Direct bridge to `AI_Agents\34_agent_environments_and_agentic_rl`: this section is the prerequisite foundation for GRPO applied to tool-use and agentic reasoning tasks

## 5.6 Practical Alignment Workflow
- Typical pipeline order: base model → SFT → preference alignment (DPO or RLHF) → evaluation → iterate
- Constructing a preference dataset: from human annotation, from existing public preference datasets, or synthetically (a stronger model judges pairs — recap Section 01.6's synthetic-data caveats)
- Evaluating alignment: win-rate against a reference model (often judged by a strong LLM — recap Section 06's LLM-as-judge content), not just reward-model score

---

## Hands-on Exercises
1. Train a small reward model on a public pairwise-preference dataset; verify it assigns higher scores to the preferred response in a held-out set.
2. Implement DPO's loss function from scratch (not just calling a library) and fine-tune a small SFT model on a preference dataset with it.
3. Compare a DPO-aligned model against its SFT-only starting point using pairwise win-rate judged by a stronger model.
4. Read and diagram the full RLHF-with-PPO pipeline (which models are involved, what data flows between them) well enough to explain it without notes.

## Project — SFT → DPO Alignment Pipeline with Measured Win-Rate
Starting from a base model, build an SFT model (reuse Section 03's project or dataset), then align it further with DPO on a preference dataset (public or self-constructed via a stronger-model judge). Evaluate all three stages — base, SFT, DPO-aligned — with a consistent pairwise win-rate evaluation. Report the win-rate progression and at least one qualitative example per stage showing the behavioral difference.

## Recommended Resources
- Ouyang et al., "Training language models to follow instructions with human feedback" (InstructGPT, 2022) — the canonical RLHF pipeline paper
- Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model" (2023)
- Shao et al., "DeepSeekMath" (GRPO's origin paper) and the DeepSeek-R1 technical report for GRPO applied to reasoning
- Ethayarajh et al., "KTO: Model Alignment as Prospect Theoretic Optimization" (2024)
- Hugging Face `trl` library documentation (`RewardTrainer`, `PPOTrainer`, `DPOTrainer`)

## Definition of Done
- [ ] You can explain why DPO doesn't require a separate reward model or an RL loop, in terms of the math, not just "it's simpler"
- [ ] You've trained at least one preference-aligned model and measured its win-rate against its pre-alignment version
- [ ] You can explain how GRPO connects this section to `AI_Agents\34`'s agentic RL content
