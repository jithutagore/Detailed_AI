# 11 — Model Evaluation & Selection

> **Goal:** Measure model quality correctly and choose between models with confidence. Poor evaluation is the most common cause of ML projects failing quietly.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** 06, 07–10

---

## Learning Objectives
- Choose the right metric for classification, regression and ranking problems
- Apply cross-validation correctly, including for time series and grouped data
- Tune hyperparameters systematically
- Avoid the common evaluation mistakes that make results look better than they are

---

## 11.1 Classification Metrics
- Confusion matrix: TP, FP, TN, FN
- Accuracy, and why it's misleading on imbalanced data
- **Precision, Recall, F1** (and F-beta for weighting one over the other)
- **ROC curve and AUC**
- **Precision-Recall curve and AUC-PR** (better than ROC for imbalanced data)
- Log loss (calibrated probability quality)
- Multiclass metrics: macro/micro/weighted averaging
- Cohen's Kappa, Matthews Correlation Coefficient
- Choosing a decision threshold based on business cost (false positive vs false negative cost)

## 11.2 Regression Metrics
- MAE, MSE, RMSE, and their sensitivity to outliers
- R² and adjusted R²
- MAPE, sMAPE (percentage errors, and their pitfalls near zero)
- Residual plots (diagnosing bias, heteroscedasticity)

## 11.3 Ranking & Recommendation Metrics (preview)
- Precision@K, Recall@K, MAP, NDCG (full treatment in Section 15)

## 11.4 Cross-Validation
- k-Fold CV, Stratified k-Fold (classification)
- Leave-One-Out (when it's worth the cost)
- **TimeSeriesSplit** (no shuffling, no future leakage)
- **GroupKFold** (keeping groups like the same customer together)
- Nested cross-validation (unbiased hyperparameter tuning + evaluation)
- How many folds, and the variance-vs-cost tradeoff

## 11.5 Hyperparameter Tuning
- Grid search, random search
- Bayesian optimization (**Optuna**, Hyperopt)
- Successive halving / Hyperband (early-stopping bad configs)
- Search space design (log scale for learning rates, etc.)
- Avoiding overfitting the validation set through excessive tuning

## 11.6 Statistical Comparison of Models
- Is Model A really better than Model B, or is it noise?
- Paired tests across CV folds
- Confidence intervals on metrics (bootstrap)

## 11.7 Common Evaluation Mistakes
- Data leakage into evaluation (Section 05.8, revisited)
- Tuning on the test set (the test set touched more than once)
- Wrong CV strategy for time series or grouped data
- Optimizing the wrong metric for the business problem
- Not comparing against a baseline
- Survivorship bias in the evaluation data

## 11.8 Calibration
- Are predicted probabilities trustworthy?
- Calibration curves (reliability diagrams)
- Platt scaling, isotonic regression
- Why calibration matters for decisions based on probability thresholds

---

## Hands-on Exercises
1. On an imbalanced dataset, show how accuracy, F1 and AUC-PR disagree, and explain why.
2. Implement TimeSeriesSplit manually and show what goes wrong if you use regular k-Fold on time-series data instead.
3. Run nested cross-validation and compare its estimate to a naive "tune then evaluate on the same folds" approach.
4. Calibrate a model's probabilities and plot the before/after reliability diagram.

## Project — Rigorous Model Comparison
Take 3 algorithms from Sections 07–10 on the same dataset. Build a nested cross-validation pipeline with proper preprocessing (fit inside each fold), tune each with Optuna, and statistically compare the results. Deliver a report recommending one model with justification tied to the business metric.

## Recommended Resources
- scikit-learn User Guide: Model Evaluation, Cross-Validation, Model Selection
- *An Introduction to Statistical Learning*, Chapter 5
- Optuna documentation

## Definition of Done
- [ ] Your evaluation pipeline has zero leakage (explicitly checked)
- [ ] You chose a metric and justified it in terms of the business problem
