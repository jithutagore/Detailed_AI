# 03 — LLM Foundations

> **Goal:** Understand how LLMs work well enough to predict their behavior, limits and cost. You don't need to train one.

**Level:** Foundation · **Time:** 1–2 weeks · **Prerequisites:** 01

---

## Learning Objectives
- Explain tokens, embeddings, attention and the context window
- Reason about the sampling parameters (temperature, top-p)
- Know the difference between base, instruction-tuned and reasoning models
- Understand why LLMs hallucinate and where they fail

---

## 3.1 Math Intuition (just enough)
- Vectors, dot product, **cosine similarity**
- Matrices and matrix multiplication (conceptually)
- Probability distributions, softmax
- Log-probabilities and perplexity

## 3.2 Tokens & Tokenization
- What a token is (subwords, BPE, SentencePiece)
- Counting tokens (`tiktoken`, provider token-count APIs)
- Why token count ≠ word count (languages, code, numbers)
- Tokenization quirks: spelling, arithmetic, non-English text costs more tokens

## 3.3 Embeddings
- Token embeddings vs sentence/document embeddings
- Semantic similarity in vector space
- Embedding dimensions and normalization
- Preview: embeddings are what makes RAG possible (Section 09)

## 3.4 The Transformer Architecture
- Encoder vs decoder vs encoder-decoder
- **Attention** and **self-attention** (queries, keys, values)
- Multi-head attention
- Feed-forward layers, residual connections, layer norm
- **Positional encoding** (sinusoidal, learned, RoPE)
- Mixture-of-Experts (MoE) models (conceptual)

## 3.5 Inference Mechanics
- Autoregressive generation (next-token prediction)
- **Context window**: limits, "lost in the middle", long-context trade-offs
- **KV cache** and why it speeds up generation
- Prefill vs decode phases (why input tokens are cheaper and faster than output tokens)
- Latency: time-to-first-token (TTFT) vs tokens per second
- Prompt caching (conceptual)

## 3.6 Sampling & Decoding
- Greedy decoding
- **Temperature**
- **Top-p** (nucleus) and top-k sampling
- Stop sequences, max tokens
- Determinism: why temperature 0 still isn't fully deterministic
- Which settings suit which tasks (extraction vs creative writing)

## 3.7 How Models Are Trained
- Pre-training on large text corpora
- Supervised fine-tuning (instruction tuning)
- RLHF, RLAIF, DPO (conceptual)
- Tool-use and agentic training
- Knowledge cutoff and why models don't know recent events

## 3.8 Model Types
- Base vs chat/instruct models
- **Reasoning models vs non-reasoning models**: extended thinking, thinking budgets, when reasoning is worth the extra cost and latency
- Small language models (SLMs) vs frontier models
- Open-weight vs closed (API-only) models
- Multimodal models (text, image, audio, video input)
- Embedding models and rerankers (different model types)

## 3.9 Limitations
- Hallucination: causes and how to reduce it
- Sycophancy and instruction-following failures
- Arithmetic and counting weaknesses
- Non-determinism
- Training-data bias

---

## Hands-on Exercises
1. Tokenize the same paragraph in English, your native language and Python code. Compare the token counts.
2. Compute cosine similarity between 10 sentence embeddings and plot them as a heatmap.
3. Run one prompt at temperature 0, 0.7 and 1.2, five times each, and compare the outputs.
4. Measure TTFT and tokens/sec for a small and a large model.
5. Compare a reasoning model and a non-reasoning model on a multi-step logic puzzle (accuracy, latency, cost).

## Recommended Resources
- "Attention Is All You Need" (Vaswani et al., 2017)
- Andrej Karpathy, "Let's build GPT" and "Intro to Large Language Models" videos
- Jay Alammar, "The Illustrated Transformer"
- 3Blue1Brown neural network / transformer series

## Definition of Done
- [ ] You can explain attention, the KV cache and temperature to a colleague without notes
- [ ] You have a notebook with the token, embedding and sampling experiments
