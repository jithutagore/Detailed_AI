# 08 — Tree-Based Models

> **Goal:** Understand decision trees deeply, since they're the building block for the ensemble methods (Section 09) that win most tabular-data competitions.

**Level:** Core · **Time:** 1 week · **Prerequisites:** 06

---

## Learning Objectives
- Explain how a decision tree splits data and when to stop
- Use the right impurity measure for the task
- Control overfitting in trees with pruning and hyperparameters
- Read and interpret a trained tree

---

## 8.1 Decision Trees — Concept
- Recursive partitioning of the feature space
- Tree structure: root, internal nodes, leaves, depth
- Decision trees for classification and for regression

## 8.2 Splitting Criteria
- **Gini impurity**
- **Entropy** and **information gain**
- Variance reduction (for regression trees)
- How a split is chosen (greedy, per-feature threshold search)

## 8.3 Overfitting & Pruning
- Fully grown trees memorize the training data
- Pre-pruning (hyperparameters): `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_leaf_nodes`
- Post-pruning: cost-complexity pruning (`ccp_alpha`)
- Visualizing a tree and reading its decisions

## 8.4 Strengths & Weaknesses
- ✅ Interpretable, handles mixed types, no scaling needed, captures non-linearity and interactions automatically
- ⚠️ High variance (small data changes → different tree), biased toward features with many levels, weak at extrapolation
- Why a single tree is rarely used alone in production (motivates Section 09)

## 8.5 Feature Importance
- Impurity-based importance (and its bias toward high-cardinality features)
- Permutation importance as a more reliable alternative (link to Section 17)

---

## Hands-on Exercises
1. Implement information gain and Gini impurity calculations by hand on a small dataset.
2. Grow an unpruned tree and an appropriately pruned tree on the same data; compare train vs test accuracy.
3. Visualize how the decision boundary changes with `max_depth` = 1, 3, 10, unlimited.

## Mini Project — Interpretable Decision Tree for Customer Churn
Fit a shallow, well-pruned tree, visualize it, and translate the top 3 splits into plain-language business rules a non-technical team could act on.

## Recommended Resources
- *An Introduction to Statistical Learning*, Chapter 8 (Sections on trees)
- StatQuest: Decision Trees

## Definition of Done
- [ ] You can explain Gini vs entropy and when they give different splits
- [ ] Your pruned tree generalizes better than the unpruned one (shown with numbers)
