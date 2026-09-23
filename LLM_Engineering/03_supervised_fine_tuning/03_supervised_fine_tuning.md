# 03 — Supervised Fine-Tuning (SFT)

> **Goal:** Turn a base (next-token-predicting) pretrained model into an instruction-following assistant. This is the most commonly used technique in this folder — the thing most people mean when they say "fine-tune a model."

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** Section 01, Section 02 (read-through sufficient), `Deep_Learning\09_gpt_and_decoder_models`

---

## Learning Objectives
- Explain the difference between a base model and an instruction-tuned/chat model
- Build a correctly formatted instruction-tuning dataset and fine-tune a model on it
- Diagnose common SFT failure modes (overfitting, catastrophic forgetting, format collapse)
- Evaluate whether fine-tuning actually improved the model versus the base or a prompted alternative

---

## 3.1 Base Models vs. Instruction-Tuned Models
- What a raw pretrained model actually does when prompted (continues text plausibly, doesn't "answer") vs. what an instruction-tuned model does
- The instruction-tuning gap: recap `AI_Agents\03`'s coverage of this from the consumer side — this section teaches how to close that gap yourself
- Chat templates: system/user/assistant turn structure, special tokens, and why using the wrong template for a given base model silently degrades output quality

## 3.2 Building an SFT Dataset
- Recap Section 01.6's data pipeline content
- Dataset composition: task diversity, response quality, length distribution, and why a few thousand high-quality examples often beats hundreds of thousands of noisy ones (the core finding behind "LIMA"-style results)
- Multi-turn conversation formatting and masking: only computing loss on assistant turns, not user turns or the prompt
- Mixing in general-instruction data to avoid narrowing the model's capabilities when fine-tuning for a specific task

## 3.3 The SFT Training Loop
- Standard cross-entropy loss over the response tokens only (loss masking, recap 3.2)
- Full fine-tuning vs. partial (freezing early layers) — and why full fine-tuning of anything beyond small models is rarely done without the techniques in Section 04
- Packing sequences for efficiency vs. padding, and the trade-offs
- Learning rate selection for fine-tuning (typically much lower than pretraining) and short warmup/schedule choices

## 3.4 Common Failure Modes
- **Catastrophic forgetting**: the model loses general capability while gaining the fine-tuned task, and how to detect it (eval on general benchmarks before/after)
- **Overfitting on small datasets**: memorized outputs, degraded generalization — symptoms in the loss curve (recap `Deep_Learning\03`'s diagnostics)
- **Format collapse**: the model over-fits to superficial patterns in the training data (always starts responses the same way, ignores the actual question) rather than learning the underlying task
- **Repetition and degeneration** after fine-tuning, and decoding-side vs. training-side causes

## 3.5 Instruction-Tuning Recipes in Practice
- Single-task fine-tuning (e.g. a classifier-like structured task) vs. general instruction-following fine-tuning
- Multi-task instruction tuning and the role of instruction diversity (recap the FLAN-style approach: many tasks phrased as instructions)
- Iterative refinement: fine-tune, evaluate, identify failure categories, add targeted data, repeat

## 3.6 When Fine-Tuning Is (and Isn't) the Right Tool
- Recap `AI_Agents\25`'s fine-tune-vs-prompt-vs-RAG decision framework — this section gives you the mechanics that decision assumes
- Signals that favor fine-tuning: consistent output format/style needs, latency/cost pressure that rules out long prompts, a narrow well-defined task with enough training data
- Signals that favor prompting/RAG instead: rapidly changing information, small number of examples, need for source attribution

---

## Hands-on Exercises
1. Format a public instruction dataset (or your own) into a correct chat template for a specific open-weight base model; verify loss masking only applies to assistant turns.
2. Fine-tune a small open-weight base model on a narrow task (e.g. converting natural language to a fixed JSON schema) and measure accuracy before and after fine-tuning.
3. Deliberately overfit a model on a tiny dataset (20–30 examples, many epochs) and observe format collapse and memorization in its outputs.
4. Run a general-capability eval (a small standard benchmark subset) on a model before and after task-specific fine-tuning to measure catastrophic forgetting, if any.

## Project — Task-Specific Assistant, Base vs. Fine-Tuned vs. Prompted
Pick a concrete task (e.g. domain-specific classification, structured extraction, a narrow-domain support assistant). Build an SFT dataset, fine-tune a small open-weight model, and compare three approaches head-to-head with real numbers: (1) the base model with a well-engineered prompt, (2) the base model with few-shot examples, (3) your fine-tuned model. Report accuracy, latency, and cost for each.

## Recommended Resources
- Wei et al., "Finetuned Language Models Are Zero-Shot Learners" (FLAN, 2021)
- Zhou et al., "LIMA: Less Is More for Alignment" (2023) — the small-high-quality-dataset result
- Hugging Face `trl` (`SFTTrainer`) and `transformers` `Trainer` documentation
- Ouyang et al., "Training language models to follow instructions with human feedback" (InstructGPT, 2022) — Section 3 specifically covers the SFT stage

## Definition of Done
- [ ] You can explain, with an example, exactly what loss masking does and why it matters for chat-formatted data
- [ ] You've fine-tuned a model and can point to concrete before/after eval numbers, not just "it seems better"
- [ ] You can name at least two SFT failure modes you've personally observed in your own training runs
