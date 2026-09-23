# 08 — BERT & Encoder Models

> **Goal:** Understand and apply BERT-family encoder-only Transformers — the architecture that transformed NLP by making pretraining + fine-tuning the standard workflow, and that still powers most classification, embedding and retrieval tasks today (including the retrieval side of RAG in `AI_Agents\09`).

**Level:** Core · **Time:** 1–2 weeks · **Prerequisites:** 07

---

## Learning Objectives
- Explain BERT's pretraining objectives and why they work
- Fine-tune BERT-family models for classification, NER and other tasks
- Understand and use sentence/text embedding models built on this architecture
- Choose the right encoder model size/variant for a task

---

## 8.1 Recap: Encoder-Only Transformers
- From Section 07.6: bidirectional, sees the whole input at once — good for *understanding*, not generation
- Why bidirectionality matters: a word's meaning depends on context from both directions ("bank" means different things depending on words before *and* after it)

## 8.2 BERT's Pretraining Objectives
- **Masked Language Modeling (MLM)**: randomly mask ~15% of input tokens, train the model to predict them from bidirectional context — this is what makes bidirectional pretraining possible at all (a left-to-right objective can't be bidirectional without "cheating")
- **Next Sentence Prediction (NSP)**: predicting whether two sentences are consecutive (later shown to be less essential — RoBERTa removes it, awareness)
- Why **self-supervised pretraining** on massive unlabeled text (recap Section 01.2) produces such transferable representations
- `[CLS]` token (aggregate sequence representation) and `[SEP]` token (segment separator)

## 8.3 The BERT Family
- **BERT** (2018): the original, base and large sizes
- **RoBERTa**: BERT trained "correctly" — more data, longer training, removed NSP, dynamic masking
- **DistilBERT**: knowledge distillation for a smaller, faster model (preview of Section 16's distillation techniques)
- **ALBERT**: parameter sharing for efficiency
- **ELECTRA**: a more sample-efficient pretraining objective (replaced-token detection instead of masking) — awareness
- Domain-specific variants: BioBERT, SciBERT, FinBERT, and others (pretraining continued on domain text)
- Multilingual variants: mBERT, XLM-RoBERTa

## 8.4 Fine-Tuning BERT for Downstream Tasks
- **Sequence classification**: adding a classification head on top of `[CLS]`, fine-tuning end-to-end — direct successor to `ML\16` classical text classification and Section 06.5's LSTM classifier, now compare all three
- **Token classification / NER**: a classification head per token — direct successor to `AI\06.5`'s HMM tagger and Section 06.5's BiLSTM tagger
- **Question answering**: predicting start/end token spans in a context passage
- **Sentence-pair tasks**: natural language inference, semantic similarity
- Fine-tuning practicalities: small learning rates (essential — large ones destroy pretrained knowledge), few epochs (2–4 typical), the Hugging Face `transformers` library workflow (`AutoModel`, `AutoTokenizer`, `Trainer`)

## 8.5 Sentence & Text Embeddings
- Why raw BERT `[CLS]` embeddings aren't great for semantic similarity out of the box
- **Sentence-BERT (SBERT)**: siamese/triplet network fine-tuning specifically for producing comparable sentence embeddings
- Contrastive learning for embeddings (concept)
- This is the exact technology behind the embedding models used in `AI_Agents\09_rag_fundamentals` — direct, practical link forward
- Modern embedding models (awareness): the current generation of retrieval-optimized embedding models, and the MTEB leaderboard (recap `AI_Agents\09.2`)

## 8.6 Tokenization for Encoder Models
- **WordPiece** (BERT's tokenizer) vs **BPE** (used elsewhere) — recap and extend `AI_Agents\03.2`
- Subword tokenization handling out-of-vocabulary words
- Special tokens and their roles

## 8.7 Evaluating Encoder Models
- Standard NLP benchmarks: GLUE, SuperGLUE (awareness — what they measure and why they mattered historically)
- Task-specific metrics: accuracy/F1 for classification, F1 for NER, EM/F1 for QA (recap `ML\11.1`)

---

## Hands-on Exercises
1. Fine-tune a pretrained BERT-base model for sentiment classification; compare accuracy, training time, and inference latency against your `ML\16` TF-IDF baseline and your Section 06 LSTM classifier.
2. Fine-tune BERT for token-level NER on a labeled dataset; compare F1 against a classical baseline.
3. Use a Sentence-BERT model to compute semantic similarity between sentence pairs; compare its similarity rankings to simple TF-IDF cosine similarity (`ML\16.6`).
4. Visualize BERT's attention patterns on a sentence using `bertviz` or similar; identify heads that seem to track syntax vs coreference.

## Project — Document Classification & Semantic Search System
Build a two-part system: (1) fine-tune BERT for classifying documents into categories, with a full evaluation report comparing against classical and LSTM baselines; (2) use a sentence-embedding model to build a small semantic search index over the same documents (cosine similarity retrieval). Document where each approach (classical/LSTM/BERT-classification/embedding-search) wins on accuracy, speed and data efficiency.

## Recommended Resources
- Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (2018)
- Jay Alammar, "The Illustrated BERT"
- Hugging Face `transformers` documentation and course (huggingface.co/course)
- Reimers & Gurevych, "Sentence-BERT" (2019)

## Definition of Done
- [ ] Your fine-tuned BERT classifier outperforms your classical and LSTM baselines on the same task
- [ ] You can explain why MLM enables bidirectionality where a standard language-modeling objective can't
- [ ] Your semantic search system returns sensibly ranked results for held-out queries
