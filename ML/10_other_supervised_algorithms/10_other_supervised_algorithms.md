# 10 — Other Supervised Algorithms

> **Goal:** Round out your toolbox with algorithms that are less commonly the "best" choice but are important to know, appear in interviews, and fit specific situations well.

**Level:** Core · **Time:** 1 week · **Prerequisites:** 06, 07

---

## Learning Objectives
- Use k-Nearest Neighbors correctly, including its pitfalls
- Understand instance-based vs model-based learning
- Know Gaussian Processes and probabilistic classifiers at a conceptual level
- Recognize when a simple algorithm beats a complex one

---

## 10.1 k-Nearest Neighbors (kNN)
- Lazy learning (no training phase, all computation at prediction time)
- Choosing k, distance metrics, weighted voting
- The curse of dimensionality and why kNN struggles in high dimensions
- Feature scaling is mandatory for kNN
- Efficient search: KD-trees, Ball trees, approximate nearest neighbors (link to vector DBs in the Agents syllabus, Section 09)

## 10.2 Discriminant Analysis
- Linear Discriminant Analysis (LDA): classification + dimensionality reduction
- Quadratic Discriminant Analysis (QDA)
- Comparison with logistic regression

## 10.3 Gaussian Processes (awareness)
- Non-parametric, probabilistic regression with uncertainty estimates
- Kernels/covariance functions
- Where they're used: Bayesian optimization, small-data problems needing uncertainty

## 10.4 Rule-Based & Simple Baselines
- Decision rules / rule lists (interpretable-by-design models)
- Always start with the simplest possible baseline (majority class, linear model) before anything complex

## 10.5 Multi-Label & Multi-Output Learning
- Binary relevance, classifier chains
- Multi-output regression
- Label correlations

## 10.6 Semi-Supervised & Self-Training (awareness)
- Label propagation
- Self-training / pseudo-labeling
- When labeled data is scarce but unlabeled data is abundant

---

## Hands-on Exercises
1. Implement kNN classification by hand (no library) and verify it matches scikit-learn.
2. Show the curse of dimensionality: plot kNN accuracy as you add random noise features.
3. Compare LDA vs logistic regression on a dataset where classes are roughly Gaussian.

## Mini Project — Algorithm Bake-Off
On one classification dataset, compare kNN, LDA, logistic regression, a decision tree and a gradient-boosted model, all with proper cross-validation. Report accuracy, F1, training time and inference time. Conclude with a recommendation and the reasoning behind it.

## Definition of Done
- [ ] You can explain when kNN is a reasonable choice and when it isn't
- [ ] The bake-off report includes both performance and practical trade-offs (speed, interpretability)
