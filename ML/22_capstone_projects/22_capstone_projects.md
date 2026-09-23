# 22 — Capstone Projects

> **Goal:** Build portfolio-grade ML projects that demonstrate the full lifecycle: framing, data, modeling, evaluation, deployment and monitoring — not just a notebook with a high accuracy number.

**Level:** Portfolio · **Time:** 4–6 weeks · **Prerequisites:** All core + at least 2 applied sections + 20

---

## Required for EVERY Capstone
- [ ] A written problem framing (business question → ML problem, per Section 21.1)
- [ ] EDA report with documented findings (Section 04)
- [ ] Leakage-free preprocessing pipeline (Section 05)
- [ ] At least 3 candidate models compared with proper cross-validation (Section 11)
- [ ] Explainability applied to the final model (Section 17)
- [ ] Deployed as a real service or batch pipeline, not just a notebook (Section 20)
- [ ] Monitoring/drift-detection component, even if simulated (Section 20.9)
- [ ] README with architecture diagram, results table and limitations section

---

## Capstone 1 — Tabular Prediction at Production Quality
**Domain:** pick one — credit risk, insurance claims, healthcare readmission, customer churn.
**Features:** full preprocessing pipeline, gradient-boosted model tuned with Optuna, SHAP explanations, fairness check across a sensitive attribute, FastAPI serving endpoint, drift monitor.
**Stretch:** a stacked ensemble; a cost-sensitive threshold chosen from a business cost matrix.
**Shows:** the complete classical-ML lifecycle end to end.

## Capstone 2 — Forecasting System
**Domain:** retail demand, energy load, web traffic, or a domain of your choice.
**Features:** decomposition + EDA, a naive baseline, a classical model (SARIMA/Prophet) and an ML model (lag-feature gradient boosting) compared with walk-forward validation, prediction intervals, a scheduled retraining pipeline (Airflow/Prefect).
**Stretch:** hierarchical forecasting across multiple related series (e.g. per-store).
**Shows:** correct time-series methodology, which is where most practitioners make silent mistakes.

## Capstone 3 — Recommendation Engine
**Domain:** e-commerce, media/content, or job matching.
**Features:** hybrid content-based + collaborative filtering, matrix factorization for implicit feedback, a two-stage candidate-generation + ranking architecture, evaluation with NDCG@K and a diversity metric, a simple API serving top-N recommendations.
**Stretch:** an online-learning or bandit-based re-ranking layer for exploration.
**Shows:** production recommender-system architecture, not just an offline notebook metric.

## Capstone 4 — Anomaly/Fraud Detection System
**Domain:** payment fraud, network intrusion, or industrial sensor monitoring.
**Features:** unsupervised baseline (Isolation Forest) + supervised model where labels exist, Precision@K evaluation under a fixed alert budget, per-alert explanation (SHAP), a monitoring dashboard tracking alert volume and drift.
**Stretch:** a semi-supervised approach blending scarce labels with the unsupervised signal.
**Shows:** handling extreme class imbalance and designing for a human-in-the-loop review process.

## Capstone 5 — Full MLOps Platform Demo
**Domain:** take any model from Capstones 1–4 and rebuild its lifecycle as the primary deliverable.
**Features:** DVC-versioned data, MLflow experiment tracking and model registry, an orchestrated retraining DAG, CI/CD with quality gates, canary or shadow deployment, full drift + performance monitoring with alerting.
**Shows:** MLOps engineering depth — the skill set that separates "built a model" from "runs ML in production."

---

## Portfolio Presentation
For each capstone, publish:
1. GitHub repo (clean code, tests, CI badge, clear README)
2. Architecture diagram (data flow, not just the model)
3. Results table: offline metrics + what an online A/B test would measure
4. A short write-up: the business framing, key trade-offs made, and what you'd do differently with more time/data

## Suggested Timeline (per capstone)
| Week | Activity |
|---|---|
| 1 | Problem framing, EDA, data pipeline |
| 2 | Feature engineering, baseline models |
| 3 | Model tuning, evaluation, explainability, fairness check |
| 4 | Deployment (serving + orchestration) |
| 5 | Monitoring, CI/CD, documentation |
| 6 | Write-up, diagram, polish |

## How This Connects Forward
- Capstones 2 and 4 connect directly to the AI Agents syllabus specialized-agent labs (finance workflow, SQL/data analyst agent)
- Capstone 5's MLOps skills transfer directly to LLMOps in the planned LLM Engineering folder
- The system-design skill from Section 21 transfers to the AI Agents Section 31 (Agent Architecture Design)
