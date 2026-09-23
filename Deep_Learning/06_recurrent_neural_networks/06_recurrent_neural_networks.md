# 06 — Recurrent Neural Networks (RNN, LSTM, GRU)

> **Goal:** Implement RNN, LSTM and GRU architectures in full depth with PyTorch, building directly on the classical-AI-side treatment in `AI\08_sequence_models`. This section is hands-on and framework-based; `AI\08` covers the from-scratch NumPy theory. Together they form the direct on-ramp to Transformers (Section 07).

**Level:** Core · **Time:** 2–3 weeks · **Prerequisites:** `AI\08_sequence_models` (strongly recommended first), 02, 03

---

## Learning Objectives
- Implement RNN, LSTM and GRU layers using PyTorch's building blocks and from lower-level primitives
- Build sequence classification and sequence-to-sequence models
- Apply the Section 03 training toolkit to the specific instabilities of recurrent networks
- Know exactly where RNNs still win over Transformers in production

---

## 6.1 Recap: Why Sequences Need Recurrence
- Full theory covered in `AI\08.1–08.2` — read that first if you haven't
- This section's focus: **implementing** it well in PyTorch, at production quality

## 6.2 PyTorch RNN Building Blocks
- `nn.RNN`, `nn.LSTM`, `nn.GRU`: input/output shapes, `batch_first` convention, hidden state initialization
- Multi-layer (stacked) RNNs
- Bidirectional RNNs in PyTorch (recap `AI\08.5`)
- Packing padded sequences (`pack_padded_sequence`) — handling variable-length sequences efficiently in batches, and why this matters for real data (not all sequences are the same length)

## 6.3 Implementing LSTM/GRU from Primitives
- Building an LSTM cell manually from `nn.Linear` + activations (matching the gate equations from `AI\08.3`) — confirms the theory is fully understood, not just imported
- Comparing your from-scratch cell's behavior to `nn.LSTM`'s

## 6.4 Training Recurrent Networks
- **Gradient clipping** (recap Section 3.2) — essential and near-universal for RNN training, unlike for feedforward/conv nets
- Truncated BPTT in practice: chunking long sequences for memory-feasible training
- Teacher forcing (recap `AI\08.6`) — scheduled sampling as a refinement (gradually reducing teacher forcing during training to reduce train/inference mismatch)
- Why RNNs train slower than CNNs/Transformers: the sequential dependency prevents parallelizing across time steps (this becomes a major motivation for Section 07)

## 6.5 Sequence Modeling Task Patterns
- **Many-to-one**: sequence classification (sentiment analysis, intent classification)
- **Many-to-many (aligned)**: sequence labeling (POS tagging — recap `AI\06.5`'s HMM approach, now compare to an LSTM tagger)
- **Many-to-many (unaligned)**: sequence-to-sequence (translation, summarization — recap `AI\08.6`)
- **One-to-many**: sequence generation from a fixed input (image captioning — a CNN encoder + RNN decoder, a natural bridge exercise combining Sections 04 and 06)

## 6.6 Seq2Seq with Attention — Implementation
- Recap `AI\08.7`'s theory (Bahdanau/Luong attention)
- Full PyTorch implementation: encoder LSTM, attention-weighted context vector, decoder LSTM
- Visualizing attention weights as alignment heatmaps (recap the `AI\08` project, now at production code quality)

## 6.7 Where RNNs Still Win in Production
- **Streaming/online inference**: process one time step at a time with O(1) memory per step, vs a Transformer's need to reprocess growing context — directly relevant to `AI_Agents\28_voice_agents` (real-time STT, low-latency streaming)
- Small-parameter-budget edge deployment
- Genuinely short sequences where attention's overhead isn't worth it (recap `ML\14_time_series_forecasting`)
- Why nearly all large-scale language modeling still moved to Transformers despite this (parallelization during training dominates at scale — the core motivation for Section 07)

---

## Hands-on Exercises
1. Implement an LSTM cell from `nn.Linear` primitives; verify its output matches `nn.LSTMCell` given the same weights.
2. Build a many-to-one sentiment classifier (LSTM) on a text dataset (e.g. IMDB); compare against your `ML\16` classical TF-IDF baseline on accuracy and inference latency.
3. Build a sequence labeling model (BiLSTM) for POS tagging; compare accuracy against your `AI\06.5` HMM/Viterbi implementation.
4. Implement an image-captioning model: CNN encoder (Section 05's pretrained backbone) + LSTM decoder with attention over spatial feature maps.

## Project — Neural Machine Translation, Production Quality
Extend the `AI\08` seq2seq-with-attention project into a properly engineered PyTorch system: packed sequences for variable-length batching, gradient clipping, teacher forcing with scheduled sampling, BLEU score evaluation, and beam search decoding at inference time (rather than greedy decoding). Document training curves and sample translations at several training checkpoints.

## Recommended Resources
- PyTorch official seq2seq translation tutorial
- *Dive into Deep Learning* (d2l.ai) — RNN, LSTM, GRU, and seq2seq chapters
- Sean Robertson, "NLP From Scratch: Translation with a Sequence to Sequence Network and Attention" (PyTorch tutorials)

## Definition of Done
- [ ] Your from-scratch LSTM cell numerically matches PyTorch's built-in implementation
- [ ] Your NMT project uses beam search and reports a BLEU score, not just qualitative examples
- [ ] You can explain, concretely, one production scenario where you'd choose an RNN over a Transformer today
