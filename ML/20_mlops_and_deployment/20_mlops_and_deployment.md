# 20 — MLOps & Deployment

> **Goal:** Take a trained model from a notebook to a reliable, monitored production service. Most ML value is lost at this step, not at the modeling step.

**Level:** Production · **Time:** 3 weeks · **Prerequisites:** 05, 09, 11

---

## Learning Objectives
- Package, version and deploy models reproducibly
- Track experiments and manage a model registry
- Serve models in batch and real-time modes
- Monitor models in production and detect drift

---

## 20.1 The ML Lifecycle
```
Data → Features → Train → Evaluate → Register → Deploy → Monitor → Retrain
```
- Why this is a loop, not a line
- The gap between "works in a notebook" and "works in production"

## 20.2 Experiment Tracking
- **MLflow**: tracking runs, parameters, metrics, artifacts
- **Weights & Biases (W&B)**: tracking, sweeps, report generation
- What to log: data version, code version, hyperparameters, metrics, environment
- Comparing runs, reproducing a past result

## 20.3 Model Versioning & Registry
- Model registry concept (MLflow Model Registry, W&B Artifacts)
- Model stages: staging → production → archived
- Versioning models alongside the data and code that produced them
- Model cards (linking to AI Agents Section 30 governance practices)

## 20.4 Data & Pipeline Versioning
- **DVC** (Data Version Control) — versioning large datasets alongside Git
- Feature stores (concept): Feast, Tecton — solving train/serve feature skew
- Reproducible pipelines: Makefile, DVC pipelines, or orchestration tools (below)

## 20.5 Orchestration
- Workflow orchestrators: **Airflow**, **Prefect**, **Dagster**
- Scheduling training jobs, retraining triggers
- DAGs for the full pipeline: ingest → validate → featurize → train → evaluate → register

## 20.6 Packaging & Environments
- Pickling risks (`pickle`, `joblib`) — security and compatibility issues
- **ONNX** (framework-independent model format)
- Docker for reproducible serving environments
- Dependency pinning (matching training and serving environments exactly)

## 20.7 Serving Patterns
- **Batch inference**: scheduled jobs writing predictions to a table
- **Online/real-time inference**: a model behind a REST API
- **Streaming inference**: scoring events as they arrive (Kafka + a consumer)
- Serving frameworks: FastAPI (custom), **BentoML**, **Seldon Core**, **Ray Serve**, cloud-native endpoints (SageMaker, Vertex AI, Azure ML)
- Batching requests for throughput; latency vs throughput tradeoffs
- Model warm-up, cold starts

## 20.8 CI/CD for ML
- Testing: data validation tests, model quality gates (don't deploy if metrics regress), unit tests for feature code
- **Continuous Training (CT)**: automatically retraining on new data
- GitHub Actions / GitLab CI pipelines for ML
- Canary deployments, shadow deployment (score in parallel, don't act on it yet), blue-green deployment
- A/B testing model versions in production (link to Section 02.6)

## 20.9 Monitoring
- Infrastructure metrics: latency, throughput, error rate, resource usage
- **Model performance monitoring**: when ground truth arrives late or never, use proxy metrics
- **Data drift**: input distribution shift (PSI, KL divergence, KS test)
- **Concept drift**: the relationship between features and target changes
- Prediction drift monitoring
- Tools: Evidently AI, WhyLabs, Arize, Fiddler
- Alerting thresholds and retraining triggers

## 20.10 Governance & Reproducibility
- Audit trails: which model version, trained on which data, served which prediction
- Rollback strategy when a new model underperforms
- Cost monitoring (compute for training and serving)

---

## Hands-on Exercises
1. Track 10 experiment runs in MLflow with different hyperparameters; compare them in the UI.
2. Version a dataset with DVC across two versions and reproduce an old result.
3. Serve a model behind a FastAPI endpoint with request validation (Pydantic) and load-test it.
4. Simulate data drift (shift a feature's distribution) and detect it with Evidently AI or a PSI calculation.

## Project — End-to-End MLOps Pipeline
Take a model from an earlier ML section (e.g. the Section 09 tabular model or Section 14 forecaster). Build: an Airflow/Prefect DAG (ingest → train → evaluate → register), an MLflow-tracked training run, a FastAPI serving endpoint in Docker, a drift-monitoring dashboard, and a CI pipeline that blocks deployment on metric regression.

## Recommended Resources
- *Designing Machine Learning Systems* (Chip Huyen) — excellent, practical
- MLflow, DVC, Evidently AI official documentation
- Google's "MLOps: Continuous delivery and automation pipelines in machine learning" whitepaper

## Definition of Done
- [ ] A model can be reproduced from tracked experiment metadata alone
- [ ] The pipeline is automated end-to-end, not run by hand
- [ ] A drift monitor is running and alerts on a simulated shift
