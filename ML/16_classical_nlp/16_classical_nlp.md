# 16 — Classical NLP

> **Goal:** Learn text processing and classical NLP techniques. This is the foundation beneath modern LLM-based NLP, and it's still the right tool for many production tasks (it's faster, cheaper, and more interpretable than an LLM).
> **Note:** Transformer-based NLP (BERT, embeddings, fine-tuning) belongs in the deep learning / LLM engineering folders. This section covers the pre-transformer toolkit.

**Level:** Applied · **Time:** 1 week · **Prerequisites:** 05, 07, 12

---

## Learning Objectives
- Preprocess and represent text numerically with classical methods
- Build text classifiers without deep learning
- Understand topic modeling and basic information extraction
- Know when classical NLP is the better engineering choice over an LLM call

---

## 16.1 Text Preprocessing
- Tokenization (word, subword, sentence)
- Lowercasing, stopword removal (and when NOT to remove them)
- Stemming (Porter, Snowball) vs Lemmatization
- Regular expressions for text cleaning
- Handling punctuation, numbers, emojis, unicode normalization
- N-grams (bigrams, trigrams)

## 16.2 Text Representation
- **Bag of Words**
- **TF-IDF**: term frequency, inverse document frequency, why it downweights common words
- Word embeddings: **Word2Vec** (CBOW, Skip-gram), **GloVe**, FastText (subword embeddings, handles OOV words)
- Document embeddings: averaging word vectors, Doc2Vec
- Static embeddings vs contextual embeddings (bridge concept to transformers)

## 16.3 Text Classification
- Naive Bayes for text (link back to Section 07.6)
- Logistic regression / SVM on TF-IDF features (a strong, fast baseline)
- Feature engineering for text: n-gram ranges, min/max document frequency
- Multiclass and multilabel text classification

## 16.4 Topic Modeling
- **Latent Dirichlet Allocation (LDA)**: generative topic model concept
- Non-negative Matrix Factorization (NMF) for topics
- BERTopic (awareness — modern embedding-based topic modeling)
- Choosing the number of topics, interpreting topic-word distributions

## 16.5 Basic Information Extraction
- Named Entity Recognition (rule-based and statistical, e.g. spaCy's NER) — concept
- Part-of-speech tagging
- Dependency parsing (concept)
- Regular-expression-based extraction for structured patterns (emails, phone numbers, dates)

## 16.6 Text Similarity & Search
- Cosine similarity on TF-IDF / embeddings
- Jaccard similarity, edit distance (Levenshtein)
- Fuzzy matching (`rapidfuzz`)
- **BM25** (link forward to the RAG retrieval content in the Agents syllabus)

## 16.7 Sentiment Analysis
- Lexicon-based approaches (VADER, TextBlob) — fast, no training needed
- Trained classifiers (TF-IDF + logistic regression) vs lexicon-based: accuracy/speed tradeoff

## 16.8 When to Use Classical NLP vs an LLM
- Classical NLP wins: high volume, low latency/cost budget, well-defined categories, need for full interpretability
- LLMs win: nuanced understanding, few-shot adaptability, unstructured/open-ended tasks
- Hybrid: classical NLP as a fast first-pass filter, LLM for the harder remaining cases

---

## Hands-on Exercises
1. Build a spam classifier with TF-IDF + logistic regression and compare it to Naive Bayes.
2. Train Word2Vec on a text corpus and explore nearest-neighbor words and analogies (`king - man + woman`).
3. Run LDA topic modeling on a set of news articles and label the discovered topics.
4. Compare lexicon-based sentiment (VADER) vs a trained classifier on the same reviews dataset.

## Project — Support Ticket Classifier (Classical Baseline)
Build a TF-IDF + logistic regression classifier for support-ticket routing. Measure accuracy, F1 and inference latency, then compare against an LLM-based classifier (if available) on cost and latency. Write a recommendation for which to use in production and why.

## Recommended Resources
- *Speech and Language Processing* (Jurafsky & Martin) — free draft chapters
- spaCy documentation and course (course.spacy.io)
- Gensim documentation (Word2Vec, LDA)

## Definition of Done
- [ ] A working classical-NLP baseline with measured accuracy and latency
- [ ] A written comparison against an LLM-based approach on cost and accuracy
