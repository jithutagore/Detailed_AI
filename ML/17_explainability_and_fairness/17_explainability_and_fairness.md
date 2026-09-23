# 17 — Explainability & Fairness

> **Goal:** Explain what a model is doing and check whether it treats groups of people fairly. Required for regulated domains (finance, hiring, healthcare) and for debugging models generally.

**Level:** Applied · **Time:** 1 week · **Prerequisites:** 09, 11

---

## Learning Objectives
- Use feature-importance and explanation tools correctly
- Distinguish global from local explanations
- Measure fairness with the right metric for the situation
- Debug a model using explanations, not just guesses

---

## 17.1 Why Explainability Matters
- Trust and adoption (a stakeholder won't act on a black box)
- Regulatory requirements (credit decisions, hiring — link to the AI Agents syllabus, Section 30)
- Debugging: catching leakage, spurious correlations, bugs
- Model monitoring: explanation drift as an early warning sign

## 17.2 Interpretable-by-Design Models
- Linear/logistic regression coefficients (Section 07)
- Decision trees and shallow rule lists (Section 08)
- Generalized Additive Models (GAMs) — interpretable non-linear models
- The interpretability-vs-performance tradeoff, and when it's worth paying

## 17.3 Global Explanation Methods
- Built-in feature importance (impurity-based, and its biases — Section 08.5)
- **Permutation importance** (model-agnostic, more reliable)
- Partial Dependence Plots (PDP)
- Accumulated Local Effects (ALE) — more reliable than PDP under feature correlation
- Feature interaction detection (H-statistic)

## 17.4 Local Explanation Methods
- **SHAP (SHapley Additive exPlanations)**: game-theoretic foundation, additive attributions
  - TreeSHAP (fast, exact for tree models — link to Section 09.8)
  - KernelSHAP (model-agnostic, slower)
  - Summary plots, dependence plots, force plots, waterfall plots
- **LIME** (Local Interpretable Model-agnostic Explanations): local surrogate models
- SHAP vs LIME: theoretical guarantees vs speed/simplicity
- Counterfactual explanations ("what would need to change for a different prediction?")
- Anchors (rule-based local explanations)

## 17.5 Explaining Specific Model Types
- Explaining gradient-boosted trees (native, fast SHAP)
- Explaining linear models (coefficients × feature value)
- Explaining deep learning (bridge concept: saliency maps, integrated gradients, attention visualization — full treatment in the deep learning folder)

## 17.6 Fairness — Concepts
- Protected attributes (race, gender, age, and proxies for them)
- Disparate treatment vs **disparate impact**
- Where bias enters: historical data, sampling, label bias, feature proxies, feedback loops

## 17.7 Fairness Metrics
- **Demographic parity** (equal positive-prediction rate across groups)
- **Equalized odds** / equal opportunity (equal TPR/FPR across groups)
- Predictive parity (equal precision across groups)
- Why you generally can't satisfy all fairness metrics simultaneously (the impossibility results)
- Choosing the right metric for the specific harm you're trying to prevent

## 17.8 Bias Mitigation
- Pre-processing: reweighting, resampling, removing/transforming proxy features
- In-processing: fairness constraints during training, adversarial debiasing (concept)
- Post-processing: group-specific threshold adjustment
- Tools: Fairlearn, AIF360 (IBM), What-If Tool

## 17.9 Practical Workflow
- Run SHAP on every non-trivial model before shipping it
- Check fairness metrics across every protected/sensitive group you can identify
- Document findings (a simple model card: intended use, performance by subgroup, known limitations)

---

## Hands-on Exercises
1. Compare permutation importance vs impurity-based importance on a model with a high-cardinality feature.
2. Generate SHAP summary and waterfall plots for a gradient-boosted model; explain 3 individual predictions in plain language.
3. Compute demographic parity and equalized odds for a classifier across a protected attribute, and show they conflict.
4. Apply Fairlearn's threshold optimizer to reduce a fairness gap and measure the accuracy cost.

## Project — Explainable & Fair Credit Model
Extend the Section 07 credit-risk model: add global (permutation importance, PDP) and local (SHAP) explanations, measure fairness across at least one sensitive attribute, apply one mitigation technique, and write a model card documenting performance, explanations and fairness trade-offs.

## Recommended Resources
- *Interpretable Machine Learning* (Christoph Molnar) — free online, the standard reference
- SHAP documentation and original paper (Lundberg & Lee, 2017)
- Fairlearn documentation
- Google's "People + AI Guidebook" (fairness sections)

## Definition of Done
- [ ] Every shipped model has at least a global and a local explanation method applied
- [ ] A fairness check was run and documented, even if the answer is "no significant gap found"
