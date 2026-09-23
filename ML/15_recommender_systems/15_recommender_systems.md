# 15 — Recommender Systems

> **Goal:** Build systems that rank and suggest items to users, from simple similarity-based approaches to matrix factorization and hybrid production pipelines.

**Level:** Applied · **Time:** 1–2 weeks · **Prerequisites:** 12

---

## Learning Objectives
- Build collaborative filtering and content-based recommenders
- Use matrix factorization and understand implicit-feedback methods
- Evaluate recommenders with ranking metrics
- Design a realistic multi-stage production recommendation pipeline

---

## 15.1 Problem Framing
- Explicit feedback (ratings) vs **implicit feedback** (clicks, views, purchases — far more common in practice)
- The cold-start problem (new users, new items)
- The user-item interaction matrix, and its sparsity

## 15.2 Content-Based Filtering
- Representing items as feature vectors (metadata, text/TF-IDF, embeddings)
- Representing users as an aggregate of the items they engaged with
- Cosine similarity for recommendations
- Strength: works for new items; weakness: limited novelty (filter bubble)

## 15.3 Collaborative Filtering
- **User-based**: find similar users, recommend what they liked
- **Item-based**: find similar items to what the user already liked (usually more stable/scalable)
- Similarity metrics for CF: cosine, Pearson correlation, adjusted cosine

## 15.4 Matrix Factorization
- **SVD** for recommendations (link back to Section 01.1)
- **Alternating Least Squares (ALS)**, especially for implicit feedback
- Latent factors: what they represent
- Regularized matrix factorization objective
- Funk SVD / the Netflix Prize approach (historical context, still instructive)
- Libraries: `implicit`, Surprise, LightFM

## 15.5 Learning-to-Rank & Modern Approaches
- Factorization Machines, Field-aware FM (feature-rich sparse recommendation)
- Two-tower neural retrieval models (bridge to deep learning — candidate generation at scale)
- Sequential/session-based recommendation (concept)
- Graph-based recommendation (concept)

## 15.6 Hybrid Systems
- Combining content-based + collaborative signals
- Weighted, switching and cascade hybrid strategies
- Handling cold-start with hybrid fallback (content-based until enough interaction data exists)

## 15.7 Evaluation
- **Precision@K, Recall@K, MAP@K, NDCG@K** (ranking quality)
- Coverage, diversity, novelty, serendipity (beyond-accuracy metrics)
- Offline evaluation limitations vs online A/B testing (link to ML Section 02.6)
- Temporal train/test splitting (don't leak future interactions into training)

## 15.8 Production Architecture
```
Candidate Generation (fast, broad recall: item-based CF, embeddings/ANN)
        ↓
Ranking (precise, feature-rich model scoring a few hundred candidates)
        ↓
Business Rules / Filtering (diversity, inventory, deduplication)
        ↓
Presentation
```
- Why production systems separate cheap "retrieval" from expensive "ranking"
- Real-time vs batch-precomputed recommendations
- Exploration vs exploitation (bandits — link to Section 19)
- Feedback loops and popularity bias amplification

---

## Hands-on Exercises
1. Build item-based collaborative filtering from scratch (cosine similarity on the interaction matrix).
2. Implement matrix factorization with ALS on implicit feedback data (`implicit` library) and compare to item-based CF.
3. Compute NDCG@10 and compare it to a simple "most popular" baseline.
4. Design (on paper) a candidate-generation + ranking architecture for a specific product (e.g. a music app).

## Project — Movie/Product Recommender
Build a hybrid recommender on a public dataset (e.g. MovieLens): content-based fallback for cold-start, item-based CF and matrix factorization for warm users. Evaluate with Precision@K/NDCG@K using a temporal split, and report a diversity metric alongside accuracy.

## Recommended Resources
- *Recommender Systems Handbook* (Ricci, Rokach, Shapira) — reference
- Google's Recommendation Systems course (Machine Learning Crash Course track)
- `implicit` and Surprise library documentation

## Definition of Done
- [ ] Beats a "most popular" baseline on NDCG@K
- [ ] Cold-start handling is explicit, not accidental
