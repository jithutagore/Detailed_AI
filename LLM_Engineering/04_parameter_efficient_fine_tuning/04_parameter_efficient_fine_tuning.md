# 04 — Parameter-Efficient Fine-Tuning (PEFT)

> **Goal:** Fine-tune large models on modest hardware by updating a small fraction of parameters. This is how most fine-tuning is actually done in practice outside of large labs.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** Section 03, `Deep_Learning\17_training_at_scale`

---

## Learning Objectives
- Explain how LoRA works mathematically and why it drastically reduces trainable parameters and memory
- Fine-tune a large model on consumer/limited hardware using LoRA and QLoRA
- Compare PEFT methods and choose the right one for a given constraint
- Merge, swap, and serve multiple LoRA adapters against a shared base model

---

## 4.1 Why Full Fine-Tuning Doesn't Scale
- Recap `Deep_Learning\17.6`'s optimizer memory content: Adam stores two extra moment estimates per parameter, so full fine-tuning a large model requires far more memory than just the model weights
- The motivating question: can we get most of full fine-tuning's benefit while updating a tiny fraction of the parameters?

## 4.2 LoRA (Low-Rank Adaptation)
- Recap `Deep_Learning\09.5`'s introduction to LoRA — this section covers the mechanism in depth
- The core idea: freeze the pretrained weight matrix, learn a low-rank decomposition (two small matrices) as an additive update
- Why low intrinsic rank works: the hypothesis that fine-tuning updates live in a low-dimensional subspace
- Key hyperparameters: rank (`r`), alpha (scaling), which layers/matrices to target (attention projections vs. also the FFN), dropout
- Merging LoRA weights back into the base model for zero-overhead inference, vs. keeping them separate for swappable adapters

## 4.3 QLoRA and Quantized Fine-Tuning
- Combining LoRA with a quantized (4-bit) frozen base model to fine-tune models far larger than would otherwise fit in available memory
- NF4 (NormalFloat4) quantization and double quantization, as introduced by QLoRA
- Paged optimizers: handling memory spikes during fine-tuning on limited hardware
- The accuracy trade-off: how close QLoRA fine-tuning gets to full-precision LoRA/full fine-tuning in practice

## 4.4 Other PEFT Methods
- **Prefix tuning / prompt tuning**: learning a small number of continuous "soft prompt" vectors prepended to the input, leaving the model fully frozen
- **Adapters**: small bottleneck layers inserted between existing layers, an earlier alternative to LoRA
- **(IA)³**: learning per-channel rescaling vectors, an even more parameter-frugal approach
- Comparing methods on trainable-parameter count, memory, training speed, and typical quality vs. full fine-tuning

## 4.5 Practical LoRA Workflow
- Choosing rank and target modules for a given task and model size — starting points and how to tune them
- Multi-adapter workflows: training separate LoRA adapters for different tasks/domains against the same frozen base model
- Adapter composition and switching at inference time (recap forward-looking to Section 08's serving content on multi-LoRA serving)
- Using Hugging Face `peft` library end-to-end: config, wrapping a base model, training, saving/loading adapters

## 4.6 Choosing Between Full Fine-Tuning and PEFT
- When full fine-tuning still wins: maximum quality ceiling, large compute/data budget, fundamentally new capability rather than adaptation
- When PEFT wins: limited hardware, need for many task-specific variants of one base model, fast iteration
- Combining with Section 03: PEFT is a *how* (efficient training mechanism), SFT is a *what* (the training objective/data) — they're usually used together, not as alternatives

---

## Hands-on Exercises
1. Implement LoRA's low-rank update from scratch (the two small matrices and the forward-pass math) on a single linear layer, without using a library, and verify it matches the `peft` library's output on the same input.
2. Fine-tune a model with LoRA at several different ranks (e.g. 4, 8, 32, 128) on the same task; plot trainable-parameter count and task performance against rank.
3. Fine-tune the same model with QLoRA on hardware that couldn't fit full-precision LoRA fine-tuning; measure peak memory usage for both.
4. Train two separate LoRA adapters for two different tasks against the same frozen base model, and demonstrate hot-swapping between them at inference time.

## Project — Multi-Adapter Fine-Tuning Under a Hardware Budget
Take a mid-sized open-weight model that doesn't comfortably fit full fine-tuning on your available hardware. Using LoRA/QLoRA, train at least three task-specific adapters against the same frozen base. Document: memory budget for each approach (full fine-tune estimate vs. LoRA vs. QLoRA), training time, and task performance for each adapter compared to a full-fine-tuning baseline (run on a smaller model if necessary to get a true full-fine-tuning comparison point).

## Recommended Resources
- Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models" (2021)
- Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs" (2023)
- Liu et al., "Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning" ((IA)³ paper, 2022)
- Hugging Face `peft` library documentation

## Definition of Done
- [ ] You can derive/explain LoRA's forward pass math from memory
- [ ] You've measured, not just read about, the memory savings of LoRA and QLoRA versus full fine-tuning
- [ ] You can justify, for a given hardware/task constraint, which PEFT method (or full fine-tuning) you'd choose and why
