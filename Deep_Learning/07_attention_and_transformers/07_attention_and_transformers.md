# 07 — Attention & Transformers

> **Goal:** Build the Transformer architecture from scratch. This is the most important section in the entire Deep Learning folder — it's the direct technical successor to Section 06, and everything in `AI_Agents\` (LLMs, agents, RAG) assumes you understand what's built here.

**Level:** Core · **Time:** 3 weeks · **Prerequisites:** 06 (essential — read `AI\08.7` and this folder's Section 06.6/06.7 first)

---

## Learning Objectives
- Explain exactly why the Transformer removes recurrence and what replaces it
- Implement self-attention and multi-head attention from scratch
- Build a complete Transformer encoder-decoder from primitives
- Understand positional encoding and why it's necessary once recurrence is gone

---

## 7.1 Recap: The Two Problems Attention Solves
- From `AI\08.7` and Section 06.4/06.7: (1) the fixed-context bottleneck of seq2seq, (2) the **sequential bottleneck** — RNNs can't parallelize across time steps, which caps training speed at scale
- The Transformer's radical move (Vaswani et al., 2017, "Attention Is All You Need"): **remove recurrence entirely**, rely purely on attention
- Why this one architectural change unlocked training at a scale that made modern LLMs possible

## 7.2 Self-Attention — From First Principles
- The core idea: for each token, compute a weighted combination of *all other tokens*, where the weights are learned based on relevance
- **Queries, Keys, Values (Q, K, V)**: what each represents, and the scaled dot-product attention formula
- Why the scaling factor (√d_k) matters (preventing extremely peaked softmax outputs at high dimensions)
- Attention as a soft, differentiable lookup/retrieval mechanism (a conceptual link worth internalizing: this is the same underlying idea as retrieval in `AI_Agents\09_rag_fundamentals`, just operating inside the model instead of against an external corpus)
- Implementing scaled dot-product attention from scratch in PyTorch (pure matrix operations, no library shortcuts)

## 7.3 Multi-Head Attention
- Why one attention pattern isn't enough — different heads can learn to attend to different types of relationships (syntax, coreference, adjacency)
- Splitting Q/K/V into multiple heads, computing attention per head, concatenating and projecting back
- Implementing multi-head attention from scratch
- Visualizing attention heads on real sentences (some heads attend to adjacent words, others to syntactic dependencies — genuinely instructive to see)

## 7.4 Positional Encoding
- Why the Transformer needs this at all: self-attention alone is **permutation-invariant** — it has no inherent notion of order (unlike an RNN, where order is baked into the recurrence)
- **Sinusoidal positional encoding** (the original paper's approach): the actual formula, and the intuition for why sine/cosine at different frequencies encode position
- Learned positional embeddings (a simpler alternative, used by BERT/GPT — preview of Sections 08–09)
- Relative positional encoding, RoPE (Rotary Position Embedding) — the modern default in most current LLMs (awareness, with a pointer to `AI_Agents\03_llm_foundations` for how it's used at the LLM-application level)

## 7.5 The Full Transformer Block
- **Encoder block**: multi-head self-attention → add & norm (residual connection + LayerNorm, recap Section 03.3/03.5 and Section 05.2 — the same residual idea, reused again) → feed-forward network → add & norm
- **Feed-forward network**: a position-wise 2-layer MLP applied identically to every token — why it's there (attention mixes information *across* tokens; the FFN processes *each* token's representation)
- **Decoder block**: adds **masked self-attention** (preventing a position from attending to future tokens — essential for autoregressive generation) and **cross-attention** (attending to the encoder's output, for encoder-decoder tasks like translation)
- Stacking N encoder/decoder blocks

## 7.6 Encoder-Only vs Decoder-Only vs Encoder-Decoder
- **Encoder-only** (bidirectional, sees the whole input at once): good for understanding tasks — preview of BERT, Section 08
- **Decoder-only** (autoregressive, masked): good for generation tasks — preview of GPT, Section 09
- **Encoder-decoder** (the original architecture): good for sequence transformation tasks (translation, summarization) — direct successor to Section 06's seq2seq
- Why most modern LLMs are decoder-only (simplicity, and it turns out decoder-only models generalize well to understanding tasks too via generation)

## 7.7 Building a Transformer From Scratch
- Assembling: embedding layer + positional encoding → N encoder/decoder blocks → output projection
- Training a small Transformer for a toy task (e.g. character-level language modeling, or a small translation task) — comparing directly against Section 06's LSTM seq2seq on the same task
- Inference: greedy decoding, temperature/top-p sampling (recap `AI_Agents\03.6`'s treatment, now understanding the mechanism generating those logits)

## 7.8 Where This Folder Hands Off to AI_Agents
- `AI_Agents\03_llm_foundations` covers: tokenization, embeddings at the LLM-application level, the KV cache, sampling parameters in depth, reasoning models — all assuming the architecture built in this section
- This section is the last stop before that folder; read `AI_Agents\03` immediately after finishing here

---

## Hands-on Exercises
1. Implement scaled dot-product attention from scratch (pure matrix math, no `nn.MultiheadAttention`) and verify it against PyTorch's built-in layer given identical weights.
2. Implement multi-head attention from scratch; visualize attention weights for several heads on a real sentence.
3. Implement sinusoidal positional encoding from the paper's formula and plot it as a heatmap to see the frequency pattern.
4. Implement the causal (look-ahead) mask for decoder self-attention and verify a token genuinely cannot attend to future positions.

## Project — GPT-Style Transformer From Scratch
Following Andrej Karpathy's "nanoGPT"/"Let's build GPT" approach, implement a decoder-only Transformer entirely from scratch (embedding, positional encoding, masked multi-head self-attention, feed-forward blocks, stacked layers) and train it as a character-level or small-vocabulary language model on a text corpus of your choice. Compare its generated text quality and training speed against your Section 06 LSTM language model on the same data and same training budget — this comparison is the whole point of the exercise.

## Recommended Resources
- Vaswani et al., "Attention Is All You Need" (2017) — the original paper, read it fully now that you have the background
- Andrej Karpathy, "Let's build GPT: from scratch, in code, spelled out" (video + nanoGPT repo) — the single best hands-on resource for this section
- Jay Alammar, "The Illustrated Transformer" (visual walkthrough)
- Jay Alammar, "The Illustrated GPT-2" (bridges directly into Section 09)

## Definition of Done
- [ ] Your from-scratch multi-head attention numerically matches PyTorch's built-in layer
- [ ] Your GPT-style model generates coherent (even if simple) text after training
- [ ] You can explain, without notes, why positional encoding is necessary and why the FFN and attention sub-layers each exist
- [ ] You've read `AI_Agents\03_llm_foundations` and can map every concept there back to something built in this section
