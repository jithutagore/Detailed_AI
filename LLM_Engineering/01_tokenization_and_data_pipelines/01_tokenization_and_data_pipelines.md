# 01 — Tokenization and Data Pipelines

> **Goal:** Understand how raw text becomes model input, and how pretraining/fine-tuning corpora are actually built and cleaned. This is the unglamorous layer everything else in this folder depends on.

**Level:** Foundation · **Time:** 1–2 weeks · **Prerequisites:** `Deep_Learning\07_attention_and_transformers`, `Deep_Learning\09_gpt_and_decoder_models`

---

## Learning Objectives
- Explain how BPE, WordPiece, and Unigram tokenization differ and why modern LLMs mostly use BPE variants
- Train a tokenizer from scratch on a custom corpus
- Explain the practical consequences of vocabulary size and tokenizer choice (sequence length, multilingual fairness, cost)
- Build a cleaned, deduplicated text corpus suitable for pretraining or fine-tuning

---

## 1.1 Why Tokenization Matters More Than It Looks
- Recap `Deep_Learning\07`'s mention of tokenization as a preprocessing step — this section treats it as a first-class design decision
- Every token costs money and context window (recap `AI_Agents\04`'s token-counting content, but now from the *design* side, not the consumer side)
- Tokenizer choice affects: sequence length for the same text, fairness across languages, ability to represent code/numbers/rare words

## 1.2 Subword Tokenization Algorithms
- **Byte-Pair Encoding (BPE)**: iterative merging of the most frequent adjacent symbol pairs; used by GPT-family models
- **Byte-level BPE**: operating on raw bytes instead of Unicode characters, guaranteeing no out-of-vocabulary tokens
- **WordPiece**: BERT's likelihood-based merge criterion, similar goal to BPE with a different scoring rule
- **Unigram Language Model tokenization**: starts from a large vocabulary and prunes, used by SentencePiece/T5
- **SentencePiece** as a language-agnostic wrapper that treats text as a raw stream (no pre-tokenization assumption of whitespace-separated words) — why this matters for non-whitespace-segmented languages

## 1.3 Training a Tokenizer
- Vocabulary size trade-offs: larger vocab → shorter sequences but bigger embedding/output matrices and rarer-token sparsity
- Special tokens: BOS/EOS/PAD/UNK, chat-template tokens (system/user/assistant role markers), tool-call tokens
- Using Hugging Face `tokenizers` to train a BPE tokenizer from scratch on a custom corpus
- Extending an existing tokenizer's vocabulary (e.g. adding domain terms or a new language) vs. training fresh

## 1.4 Tokenization Failure Modes
- Why LLMs are bad at character-level tasks (spelling, counting letters, arithmetic on digits) — a direct consequence of subword tokenization
- Multilingual fairness: low-resource languages often get fragmented into far more tokens per word than English, inflating cost and reducing effective context
- Tokenizer/model mismatch: why you can't swap a tokenizer under a pretrained model without retraining the embedding layer

## 1.5 Pretraining Data Pipelines
- Data sources: web crawls (Common Crawl and derivatives), books, code, curated/licensed sources
- **Filtering**: quality classifiers, perplexity filtering, language identification
- **Deduplication at scale**: exact dedup (hashing) and near-duplicate detection (MinHash/LSH) — recap `AI_Agents\09.2`'s cleaning concepts, applied at pretraining scale (recap `Deep_Learning\17.7`)
- **Decontamination**: removing benchmark/eval data from training corpora to avoid inflated eval scores
- Data mixing: how much web text vs. code vs. books vs. curated data, and why the mixture ratio is itself a tuned hyperparameter

## 1.6 Fine-Tuning Data Pipelines
- Instruction-tuning dataset formats: prompt/response pairs, multi-turn conversations, chat templates
- Building a fine-tuning dataset from scratch: sourcing, writing, or synthetically generating examples
- Synthetic data generation using a stronger model, and the risks (distillation artifacts, mode collapse, licensing questions)
- Data quality over quantity: why a small, clean instruction dataset often outperforms a large noisy one (foreshadows Section 03)

---

## Hands-on Exercises
1. Train a BPE tokenizer from scratch on a small corpus (e.g. a book or a code repository) using Hugging Face `tokenizers`; inspect the learned merges.
2. Compare token counts for the same multilingual sentences (English, and at least one non-Latin-script language) across GPT-family, BERT, and a multilingual tokenizer; quantify the fairness gap.
3. Implement exact and near-duplicate detection (MinHash) on a text dataset and measure how much of it is duplicate/near-duplicate content.
4. Build a small instruction-tuning dataset (50–100 examples) in a standard chat format, including a system prompt and multi-turn examples.

## Project — Custom Domain Tokenizer + Cleaned Corpus
Pick a specialized domain (legal, medical, code in a specific language, or a non-English language your target model underserves). Train a domain-specific tokenizer, compare its token efficiency against a general-purpose tokenizer (e.g. GPT-4's or Llama's) on held-out domain text, and build a cleaned, deduplicated, decontaminated corpus ready for fine-tuning. Document the token-efficiency improvement and the cleaning pipeline's effect on corpus size.

## Recommended Resources
- Sennrich et al., "Neural Machine Translation of Rare Words with Subword Units" (2015) — the original BPE-for-NLP paper
- Kudo & Richardson, "SentencePiece" (2018)
- Hugging Face `tokenizers` library documentation and the "Build a tokenizer from scratch" tutorial
- Penedo et al., "The FineWeb Datasets" / "The RefinedWeb Dataset" — modern web-data filtering pipelines described in detail

## Definition of Done
- [ ] You can explain BPE, WordPiece, and Unigram tokenization well enough to whiteboard the difference
- [ ] You've trained a tokenizer from scratch and can explain its vocabulary size trade-offs
- [ ] Your project's cleaned corpus has measured deduplication and decontamination results, not just "I ran a script"
