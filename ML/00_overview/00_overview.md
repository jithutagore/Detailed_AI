# Machine Learning — Syllabus Overview

This folder is the index for the Machine Learning curriculum. Each numbered folder has its own `.md` file with the detailed syllabus for that section.

**Scope:** classical machine learning, from math foundations to production (MLOps) and ML system design. It ends with a bridge into deep learning.
**Not in scope here** (planned as separate folders): in-depth data engineering, deep learning, LLM engineering, AI agents.

---

## Section Map

| # | Folder | Level | Suggested time |
|---|---|---|---|
| 01 | `01_math_for_ml` | Foundation | 3–4 weeks |
| 02 | `02_probability_and_statistics` | Foundation | 3 weeks |
| 03 | `03_python_for_ml` | Foundation | 2 weeks |
| 04 | `04_exploratory_data_analysis` | Foundation | 1–2 weeks |
| 05 | `05_data_preprocessing_and_feature_engineering` | Foundation | 2 weeks |
| 06 | `06_ml_fundamentals` | Core | 1–2 weeks |
| 07 | `07_linear_models` | Core | 2 weeks |
| 08 | `08_tree_based_models` | Core | 1 week |
| 09 | `09_ensemble_methods_and_gradient_boosting` | Core | 2 weeks |
| 10 | `10_other_supervised_algorithms` | Core | 1 week |
| 11 | `11_model_evaluation_and_selection` | Core | 2 weeks |
| 12 | `12_unsupervised_learning` | Core | 2 weeks |
| 13 | `13_anomaly_detection` | Applied | 1 week |
| 14 | `14_time_series_forecasting` | Applied | 2 weeks |
| 15 | `15_recommender_systems` | Applied | 1–2 weeks |
| 16 | `16_classical_nlp` | Applied | 1 week |
| 17 | `17_explainability_and_fairness` | Applied | 1 week |
| 18 | `18_neural_network_basics` | Bridge | 2 weeks |
| 19 | `19_reinforcement_learning_basics` | Bridge | 1–2 weeks |
| 20 | `20_mlops_and_deployment` | Production | 3 weeks |
| 21 | `21_ml_system_design` | Production | 2 weeks |
| 22 | `22_capstone_projects` | Portfolio | 4–6 weeks |

**Total:** about 8–10 months part-time (10–15 hrs/week), or 4–5 months full-time.

---

## Learning Path

```
Math → Probability & Statistics → Python for ML → EDA → Preprocessing & Features
   ↓
ML Fundamentals → Linear Models → Trees → Ensembles/Boosting → Other Algorithms
   ↓
Evaluation & Model Selection → Unsupervised Learning
   ↓
Applied: Anomaly Detection · Time Series · Recommenders · Classical NLP · Explainability
   ↓
Bridge: Neural Network Basics · RL Basics
   ↓
MLOps & Deployment → ML System Design → Capstones
```

### Core track (if time is short)
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 11 → 12 → 20 → 22.
The applied sections (13–17) are specializations: pick the ones that match your goals.

### Habits to keep throughout
- **Build a baseline first** (a simple model, or even a "predict the mean" dummy) before anything complex.
- **Guard against data leakage** in every project: fit preprocessing on training data only, and split by time or group when needed.
- **Track experiments** (MLflow or W&B) from Section 07 onward.
- **Write down the business metric** as well as the ML metric for every project.
- **Publish each project on GitHub** with a README, the results and what you learned.

---

## How This Connects to the Other Domains
```
Data Engineering → Machine Learning (this folder) → Deep Learning → LLM Engineering → AI Agents
```
- Section 05 covers ML-specific preprocessing; large-scale pipelines belong in the data engineering folder.
- Section 18 is a bridge; the full treatment belongs in the deep learning folder.
- ML skills that agents reuse: evaluation (11), embeddings and clustering (12), classification (07–09), MLOps (20).
