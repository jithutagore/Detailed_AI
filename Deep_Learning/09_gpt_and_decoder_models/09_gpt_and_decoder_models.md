# 09 — GPT & Decoder Models

> **Goal:** Understand decoder-only, autoregressive Transformers in depth — the architecture behind every modern LLM. This section is the direct bridge into `AI_Agents\`: everything from here on in that folder builds on a decoder-only model exactly like the one covered here.

**Level:** Core · **Time:** 1–2 weeks · **Prerequisites:** 07 (essential), 08 (recommended, for contrast)

---

## Learning Objectives
- Explain the GPT pretraining objective and why decoder-only models scale so well
- Understand the GPT-1 → GPT-2 → GPT-3-and-beyond progression and what changed at each step
- Fine-tune and adapt decoder-only models
- Connect this architecture directly to everything covered in `AI_Agents\03_llm_foundations`

---

## 9.1 Recap: Decoder-Only Transformers
- From Section 07.5–07.6: masked (causal) self-attention — each token can only attend to itself and prior tokens
- The pretraining objective: **next-token prediction** (standard language modeling) — simpler than BERT's MLM, and it's exactly what you built in Section 07's capstone project
- Why this objective, despite being "just" next-token prediction, produces models capable of translation, summarization, reasoning, and more (the "unsupervised multitask learning" framing from the GPT-2 paper)

## 9.2 The GPT Lineage — What Changed at Each Step
- **GPT-1** (2018): decoder-only Transformer + unsupervised pretraining + supervised fine-tuning per task — establishing the paradigm
- **GPT-2** (2019): scaling up parameters and data; the surprising finding that a large enough language model performs tasks **zero-shot**, just from being prompted, without any task-specific fine-tuning — this is the conceptual origin of prompt engineering (`AI_Agents\05`)
- **GPT-3** (2020): scaling further; **few-shot / in-context learning** — the model learns a task from examples given directly in the prompt, no gradient updates at all — direct origin of `AI_Agents\05.2`'s few-shot prompting
- **InstructGPT / ChatGPT-era models**: adding instruction tuning and **RLHF** (Reinforcement Learning from Human Feedback) on top of the base pretrained model — the origin of the "chat"/"instruct" model distinction covered in `AI_Agents\03.8`
- **Modern reasoning models**: extended chain-of-thought reasoning trained via RL — direct link to `AI_Agents\03.8` and `AI_Agents\34` (agentic RL)
- This progression **is** the historical path from "a language model" to "an LLM you can chat with and build agents on" — everything in `AI_Agents\` sits on top of this lineage

## 9.3 Scaling Laws
- The empirical finding that loss decreases predictably as a power law with model size, data size, and compute (Kaplan et al., Chinchilla)
- Compute-optimal training: balancing model size against data size for a given compute budget (the Chinchilla finding) — why more parameters alone isn't the right lever
- Why this motivated the industry-wide scaling race, and why it also motivates smaller, well-trained models (link to `AI_Agents\34`'s emphasis on training small specialist models)

## 9.4 Training Objective & Loss
- Cross-entropy loss over the vocabulary at each position (recap Section 02.6, now applied at LLM scale)
- Perplexity as an evaluation metric (recap `ML\03.2`'s mention, now made concrete)
- Teacher forcing during training (recap Section 06.4) — every position's target is the actual next token, computed in parallel (this parallelism, impossible for RNNs, is exactly what Section 07 unlocked)

## 9.5 Fine-Tuning Decoder Models
- Full fine-tuning vs **parameter-efficient fine-tuning (PEFT)**: LoRA (Low-Rank Adaptation) — training small additional matrices instead of all weights, why this makes fine-tuning large models practical on limited hardware
- QLoRA (quantized base model + LoRA) — awareness
- Instruction tuning: fine-tuning on (instruction, response) pairs to make a base model follow directions
- Where this connects to `AI_Agents\25.5` (fine-tuning & distillation) and `AI_Agents\34` (RL-based training) — this section is their architectural foundation

## 9.6 Decoding Strategies — Implementation
- Recap `AI_Agents\03.6`'s conceptual treatment (temperature, top-p, top-k) — this section implements the actual decoding loop
- Greedy decoding, beam search (recap Section 06's NMT project), sampling-based decoding
- The KV cache: why regenerating from scratch at every step would be wasteful, and how caching key/value tensors from prior positions speeds up autoregressive generation (recap `AI_Agents\03.5`, now understanding the mechanism, not just the term)

## 9.7 From Here to AI_Agents
- This section is where the "Deep Learning" track ends and the "Gen AI / LLM Engineering" track (`AI_Agents\`) begins
- Read `AI_Agents\03_llm_foundations` immediately after this section — nearly every concept there (tokens, embeddings, context window, temperature, reasoning models, prompt engineering, structured outputs, tool calling) is a direct, practical extension of what's been built across Sections 07–09
- `AI_Agents\04_llm_apis_and_providers` onward assumes you now understand *why* an API behaves the way it does, not just *how* to call it

---

## Hands-on Exercises
1. Extend your Section 07 from-scratch GPT-style model: implement and compare greedy decoding, beam search, and temperature/top-p sampling on the same trained model — connect the generated text quality differences to the theory in `AI_Agents\03.6`.
2. Fine-tune a small pretrained decoder-only model (e.g. GPT-2 small, or a similarly-sized open model) on a custom text style/domain using full fine-tuning; observe the loss curve and sample outputs before/after.
3. Repeat the fine-tuning with LoRA instead of full fine-tuning; compare training time, memory usage, and output quality.
4. Implement instruction-tuning-style fine-tuning: format a small dataset as (instruction, response) pairs and fine-tune a small decoder model to follow instructions it wasn't trained on before.

## Project — Instruction-Tuned Model on a Budget
Take a small open-weight decoder-only model (in the 100M–1B parameter range, something trainable on a single consumer GPU or free Colab GPU). Fine-tune it with LoRA on an instruction-following dataset in a specific narrow domain (e.g. customer support responses, code comments, a specific writing style). Evaluate before/after with a small held-out test set (does it follow the target format/style?). Write up exactly how this connects to `AI_Agents\25.5`'s fine-tuning guidance and `AI_Agents\04`'s discussion of open-weight/local models.

## Recommended Resources
- Radford et al., "Improving Language Understanding by Generative Pre-Training" (GPT-1, 2018) and "Language Models are Unsupervised Multitask Learners" (GPT-2, 2019)
- Brown et al., "Language Models are Few-Shot Learners" (GPT-3, 2020)
- Ouyang et al., "Training language models to follow instructions with human feedback" (InstructGPT/RLHF, 2022)
- Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models" (2021)
- Andrej Karpathy, "Let's reproduce GPT-2" (nanoGPT, video) — the natural continuation of the Section 07 project
- Jay Alammar, "The Illustrated GPT-2"

## Definition of Done
- [ ] Your GPT-style model, extended with proper decoding strategies, produces noticeably better generations than with greedy decoding alone
- [ ] Your LoRA fine-tuning project shows a measurable behavior change with a fraction of full fine-tuning's compute/memory cost
- [ ] You can trace, with specifics, the GPT-1 → GPT-2 → GPT-3 → InstructGPT progression and name what each step contributed
- [ ] You've moved on to `AI_Agents\03_llm_foundations` and it now reads as a continuation, not a new topic
