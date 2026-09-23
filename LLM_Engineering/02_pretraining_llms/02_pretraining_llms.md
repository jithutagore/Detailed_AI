# 02 — Pretraining LLMs

> **Goal:** Understand what it actually takes to pretrain a language model from scratch — the objective, the architecture choices modern LLMs make beyond vanilla GPT, and scaling laws in practice. Most practitioners never pretrain a frontier model, but understanding this layer explains every design decision downstream.

**Level:** Foundation · **Time:** 2–3 weeks · **Prerequisites:** `Deep_Learning\09_gpt_and_decoder_models`, `Deep_Learning\17_training_at_scale`, this folder's Section 01

---

## Learning Objectives
- Explain the causal language modeling objective and why it scales so well
- Describe the architectural deltas modern open LLMs (Llama/Mistral-family) make versus the original GPT decoder
- Apply scaling laws to reason about compute-optimal model/data sizing
- Pretrain a small language model from scratch end-to-end on a single GPU or small cluster

---

## 2.1 The Pretraining Objective
- Recap `Deep_Learning\09`'s causal language modeling (next-token prediction) objective
- Why next-token prediction on massive unlabeled text produces broadly capable models — the "unsupervised multitask learner" framing
- Cross-entropy loss, perplexity as the standard pretraining metric, and why lower perplexity doesn't always mean a "better" model for downstream use

## 2.2 Modern Architecture Deltas from Vanilla GPT
- **Positional encoding**: RoPE (Rotary Position Embeddings) and why it largely replaced learned/absolute positional embeddings — recap `Deep_Learning\07`'s positional encoding coverage
- **Normalization**: Pre-LayerNorm vs. Post-LayerNorm placement, and RMSNorm as a simplification of LayerNorm
- **Activation functions**: SwiGLU/GeGLU gated feed-forward blocks replacing plain ReLU/GELU FFNs
- **Attention variants**: Multi-Query Attention (MQA) and Grouped-Query Attention (GQA) as KV-cache-memory-saving alternatives to standard multi-head attention (this pays off directly in Section 08's serving content)
- Context length extension techniques: position interpolation, NTK-aware scaling, and why base models increasingly train with long-context data directly

## 2.3 Scaling Laws in Practice
- Recap `Deep_Learning\09.3`'s introduction to scaling laws
- The Chinchilla result: compute-optimal training balances model size and data size (roughly 20 tokens per parameter), and why many earlier models were undertrained relative to their size
- Reading a scaling-law plot: how loss decreases predictably with compute, and how that lets you extrapolate before committing to an expensive run
- Practical use: estimating how much data/compute you'd need for a target model size, and vice versa

## 2.4 The Pretraining Loop at Scale
- Recap `Deep_Learning\17`'s parallelism strategies (data/tensor/pipeline, ZeRO/FSDP) — this section is where they get applied specifically to LLM pretraining
- Learning rate schedules: warmup + cosine decay, and why LLM pretraining is unusually sensitive to learning rate
- Batch size scheduling and gradient clipping as stability tools for large-scale runs
- Checkpointing strategy: saving frequently enough to recover from the inevitable hardware failures on long multi-day/week runs

## 2.5 Training Stability and Monitoring
- Recap `Deep_Learning\03`'s training diagnostics toolkit — applied at pretraining scale, where a failed run can cost thousands of dollars
- Loss spikes: causes (bad data batches, learning rate too high, numerical instability) and mitigations (skip/replay the batch, restart from checkpoint with adjusted LR)
- Monitoring gradient norms, activation statistics, and dead-neuron/attention-collapse symptoms during long runs

## 2.6 Continued Pretraining and Domain-Adaptive Pretraining
- Taking an existing pretrained base model and continuing pretraining on domain-specific unlabeled text (not yet instruction data — that's Section 03)
- When this is worth it vs. going straight to fine-tuning: large domain vocabulary/style gap (legal, medical, code, a non-English language) justifies it
- Catastrophic forgetting risk and mitigations: mixing in a small fraction of general-domain data during continued pretraining

---

## Hands-on Exercises
1. Implement RoPE from scratch and verify it produces the expected relative-position behavior on a toy sequence.
2. Compare Multi-Head, Multi-Query, and Grouped-Query Attention implementations on memory usage and inference speed for the same model size.
3. Given a fixed compute budget, use Chinchilla-style scaling-law numbers to compute the compute-optimal model size and token count; compare against an "undertrained" (too large, too little data) alternative.
4. Pretrain a small (10–100M parameter) language model from scratch on a modest text corpus; plot the loss curve and compute the final perplexity.

## Project — Small Language Model From Scratch
Pretrain a small decoder-only LLM (extending `Deep_Learning\09`'s from-scratch GPT) incorporating at least RoPE, RMSNorm, and SwiGLU. Train it on a corpus of your choice with proper learning-rate scheduling and checkpointing. Report the training loss/perplexity curve, generate samples at several checkpoints to show capability emerging over training, and document the actual compute/time/cost spent versus what scaling laws predicted you'd need.

## Recommended Resources
- Radford et al., "Language Models are Unsupervised Multitask Learners" (GPT-2 paper)
- Touvron et al., "LLaMA: Open and Efficient Foundation Language Models" (2023) — the reference for the modern architecture deltas in 2.2
- Hoffmann et al., "Training Compute-Optimal Large Language Models" (Chinchilla, 2022)
- Su et al., "RoFormer: Enhanced Transformer with Rotary Position Embedding" (2021)
- Karpathy, "Let's build GPT" and "nanoGPT" / "llm.c" — hands-on from-scratch pretraining references

## Definition of Done
- [ ] You can explain, precisely, what changed between the original GPT architecture and a modern open-weight LLM, and why each change was made
- [ ] You can use a scaling-law calculation to justify a model/data size decision, not just cite "bigger is better"
- [ ] Your from-scratch pretraining project has a genuine loss curve and checkpoint samples showing capability improving over training
