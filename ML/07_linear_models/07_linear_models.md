# 07 — Linear Models

> **Goal:** Master linear and logistic regression deeply. They're simple, interpretable, and the foundation for understanding every more complex model.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** 06

---

## Learning Objectives
- Derive and implement linear and logistic regression
- Apply regularized variants correctly
- Interpret coefficients and know the assumptions behind each model
- Use SVMs and understand the kernel trick

---

## 7.1 Linear Regression
- Model: `y = Xw + b`
- Assumptions: linearity, independence, homoscedasticity, normal residuals (and what happens when they're violated)
- Cost function: Mean Squared Error
- Closed-form solution (normal equation) vs gradient descent
- Coefficient interpretation, confidence intervals on coefficients
- Multicollinearity and VIF
- Residual analysis and diagnostic plots
- Polynomial regression

## 7.2 Regularized Linear Regression
- **Ridge regression** (L2)
- **Lasso regression** (L1) — automatic feature selection
- **Elastic Net**
- Choosing the regularization strength (cross-validated alpha path)

## 7.3 Logistic Regression
- From linear regression to classification: the **sigmoid** function
- **Log loss / binary cross-entropy**
- Decision boundary, threshold selection
- Multiclass: one-vs-rest, softmax/multinomial logistic regression
- Coefficient interpretation via odds ratios
- Class weights for imbalance
- Regularized logistic regression

## 7.4 Support Vector Machines
- Maximum margin classifier, support vectors
- Soft margin (the C parameter)
- **Kernel trick**: linear, polynomial, RBF kernels
- SVM for regression (SVR)
- When SVMs work well (high-dimensional, small-to-medium data) and when they don't (very large datasets)

## 7.5 Generalized Linear Models (awareness)
- Poisson regression (count data)
- The GLM family concept: link function + distribution

## 7.6 Naive Bayes
- Bayes' theorem applied to classification
- The "naive" conditional independence assumption
- Gaussian, Multinomial, Bernoulli Naive Bayes
- Why it works well for text classification despite the naive assumption

---

## Hands-on Exercises
1. Implement linear regression with gradient descent from scratch (no scikit-learn) and match scikit-learn's result.
2. Fit Ridge and Lasso on the same data; plot coefficients shrinking as alpha increases (a regularization path).
3. Implement logistic regression from scratch with gradient descent on log loss.
4. Compare linear vs RBF kernel SVM decision boundaries on a non-linear toy dataset.
5. Build a Naive Bayes spam classifier.

## Project — Interpretable Credit Risk Model
Build a regularized logistic regression to predict loan default. Report odds ratios for each feature, choose a threshold based on business cost (false positive vs false negative), and write a one-page explanation for a non-technical loan officer.

## Recommended Resources
- *An Introduction to Statistical Learning*, Chapters 3–4, 9
- StatQuest: Linear/Logistic Regression, Ridge/Lasso, SVM

## Definition of Done
- [ ] From-scratch implementation matches scikit-learn within a small tolerance
- [ ] Model coefficients explained in plain language
