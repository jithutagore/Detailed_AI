# 06 — Machine Learning Fundamentals

> **Goal:** Learn the vocabulary and core theory that every ML algorithm is built on, before studying specific algorithms.

**Level:** Core · **Time:** 1–2 weeks · **Prerequisites:** 01, 02, 05

---

## Learning Objectives
- Explain the difference between supervised, unsupervised and reinforcement learning
- Explain the bias-variance tradeoff and why models overfit or underfit
- Understand loss functions, regularization and the training process in general
- Set up a correct train/validation/test workflow

---

## 6.1 Types of Machine Learning
- **Supervised learning**: classification vs regression
- **Unsupervised learning**: clustering, dimensionality reduction, density estimation
- **Semi-supervised learning**
- **Self-supervised learning** (concept; bridges to deep learning)
- **Reinforcement learning** (concept; full treatment in Section 19)
- Online vs batch learning

## 6.2 The Learning Problem
- Training data, features (X), target/label (y)
- Hypothesis space, model parameters
- Loss function vs cost function vs objective function
- Empirical risk minimization
- Why we optimize on training data but care about **generalization**

## 6.3 Bias-Variance Tradeoff
- **Underfitting** (high bias) vs **overfitting** (high variance)
- Bias-variance decomposition (conceptual)
- Model complexity vs error curves
- Learning curves (training size vs error) for diagnosis
- Validation curves (hyperparameter vs error)

## 6.4 Regularization
- Why regularization fights overfitting
- L1 (Lasso) — sparsity, feature selection
- L2 (Ridge) — shrinkage
- Elastic Net (L1 + L2)
- Early stopping as regularization
- Regularization strength and how to tune it

## 6.5 Training Workflow
- Train / validation / test split, and why the test set is touched only once
- Cross-validation (preview; full treatment in Section 11)
- Baselines: always compare against a dummy/majority-class model
- Hyperparameters vs parameters
- Iterative model development loop: baseline → error analysis → improve → re-evaluate

## 6.6 Distance & Similarity (used across many algorithms)
- Euclidean, Manhattan, Minkowski, cosine distance
- Curse of dimensionality (why distance becomes less meaningful in high dimensions)

## 6.7 No Free Lunch Theorem
- No single algorithm is best for every problem
- Why you try several algorithms and let evaluation decide

---

## Hands-on Exercises
1. Fit polynomial models of degree 1, 4 and 15 to noisy data; plot underfitting, a good fit and overfitting.
2. Plot a learning curve for a model and diagnose whether it needs more data.
3. Compare L1 vs L2 regularization effects on model coefficients.
4. Implement k-nearest-neighbors distance calculations by hand and compare metrics.

## Mini Project — Bias-Variance Playground
An interactive notebook (or Streamlit app) where changing model complexity and regularization strength updates the train/validation error curves live.

## Recommended Resources
- *An Introduction to Statistical Learning* (James, Witten, Hastie, Tibshirani) — free PDF, the best general ML book
- Andrew Ng, Machine Learning Specialization (Coursera)
- StatQuest: Bias/Variance, Regularization

## Definition of Done
- [ ] You can diagnose overfitting vs underfitting from a learning curve
- [ ] You can explain regularization to a non-expert
