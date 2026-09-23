# 09 — Ensemble Methods & Gradient Boosting

> **Goal:** Master ensembling, the single most important idea for winning performance on structured/tabular data. Gradient-boosted trees are the default choice for most real-world tabular ML problems.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** 08

---

## Learning Objectives
- Explain why combining models reduces error
- Implement and tune bagging, boosting and stacking
- Use XGBoost, LightGBM and CatBoost effectively
- Tune gradient-boosting hyperparameters without overfitting

---

## 9.1 Why Ensembles Work
- The bias-variance lens: bagging reduces variance, boosting reduces bias
- Diversity among base models matters
- Wisdom-of-crowds intuition, and its limits (correlated errors don't cancel out)

## 9.2 Bagging
- **Bootstrap Aggregating**: train many models on bootstrap samples, average/vote
- **Random Forest**: bagging + random feature subsets per split
- Out-of-bag (OOB) error estimation
- Random Forest hyperparameters: `n_estimators`, `max_features`, `max_depth`, `min_samples_leaf`
- Extra Trees (extremely randomized trees)

## 9.3 Boosting — Concept
- Sequential training: each model corrects the previous ensemble's errors
- **AdaBoost**: reweighting misclassified samples
- **Gradient Boosting**: fitting new trees to the residual gradient of the loss

## 9.4 Modern Gradient Boosting Libraries
- **XGBoost**: regularized objective, second-order gradients, handling missing values, tree-pruning
- **LightGBM**: leaf-wise growth, histogram binning, speed on large data, native categorical support
- **CatBoost**: ordered boosting, strong native categorical handling, less tuning needed
- Choosing between them: dataset size, categorical features, speed needs, GPU support

## 9.5 Key Hyperparameters (all 3 libraries, roughly)
- `n_estimators` / `num_boost_round`
- `learning_rate` (and its tradeoff with `n_estimators`)
- `max_depth` / `num_leaves`
- `subsample`, `colsample_bytree` (row/column sampling — adds bagging-style regularization to boosting)
- `min_child_weight` / `min_data_in_leaf`
- `reg_alpha` (L1), `reg_lambda` (L2)
- **Early stopping** on a validation set

## 9.6 Stacking & Blending
- **Stacking**: train a meta-model on the out-of-fold predictions of base models
- Blending (simpler holdout-based version)
- Voting classifiers/regressors (hard vs soft voting)
- When ensembling-of-ensembles is (and isn't) worth the complexity

## 9.7 Practical Tuning Workflow
- Start simple: default LightGBM/XGBoost + early stopping as a strong baseline
- Tune `learning_rate` + `n_estimators` together first
- Then tree structure (`max_depth`/`num_leaves`, `min_child_weight`)
- Then sampling and regularization
- Use cross-validation, not a single validation split, for the final comparison (Section 11)
- Bayesian/automated tuning: Optuna, Hyperopt (preview of Section 11)

## 9.8 Interpreting Boosted Models
- Built-in feature importance (gain, split count) and its limits
- **SHAP values** for gradient boosting (fast, exact for trees) — preview of Section 17

---

## Hands-on Exercises
1. Implement a simple AdaBoost by hand on a toy dataset (reweighting samples manually).
2. Compare Random Forest, XGBoost, LightGBM and CatBoost on the same tabular dataset with default parameters.
3. Tune one gradient-boosting model with Optuna and show the improvement over defaults.
4. Build a 3-model stacking ensemble and compare it to the best single model.

## Project — Tabular Competition Pipeline
Pick a Kaggle tabular competition (past or active). Build: EDA → feature engineering → a Random Forest baseline → a tuned LightGBM/XGBoost/CatBoost model → a small stacked ensemble. Report the cross-validated score and the leaderboard-equivalent score if available.

## Recommended Resources
- XGBoost, LightGBM, CatBoost official docs
- StatQuest: AdaBoost, Gradient Boost, XGBoost
- Kaggle Grandmaster notebooks and write-ups on tabular competitions

## Definition of Done
- [ ] A tuned gradient-boosting model that clearly beats your Random Forest baseline
- [ ] Feature importance / SHAP summary included in the report
