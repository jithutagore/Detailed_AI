# 13 — Anomaly Detection

> **Goal:** Detect rare, unusual or suspicious data points — fraud, defects, intrusions, outages — where labeled examples are scarce or the target keeps changing shape.

**Level:** Applied · **Time:** 1 week · **Prerequisites:** 11, 12

---

## Learning Objectives
- Choose between supervised, unsupervised and semi-supervised approaches to anomaly detection
- Apply statistical, distance-based and model-based detectors
- Evaluate anomaly detectors despite extreme class imbalance
- Design a workable production anomaly-detection pipeline

---

## 13.1 Framing the Problem
- Point anomalies, contextual anomalies, collective anomalies
- Supervised (labeled fraud/not-fraud) vs unsupervised (no labels, or labels are too rare/delayed) vs semi-supervised (train only on normal data)
- Why anomaly detection is fundamentally an imbalanced-data problem (link to Section 05.7)

## 13.2 Statistical Methods
- Z-score, modified z-score (median-based, robust to outliers)
- IQR-based rules
- Grubbs' test, generalized ESD
- Multivariate: Mahalanobis distance

## 13.3 Distance & Density-Based Methods
- kNN-based outlier scoring (distance to k-th neighbor)
- **Local Outlier Factor (LOF)** — density relative to neighbors
- DBSCAN noise points as anomalies (link to Section 12.1)
- One-Class SVM

## 13.4 Model-Based Methods
- **Isolation Forest** (isolates anomalies with fewer random splits) — usually the strongest simple baseline
- Autoencoders for anomaly detection (reconstruction error) — bridge to deep learning
- Elliptic Envelope (Gaussian-assumption based)

## 13.5 Time-Series Anomaly Detection (preview)
- Residual-based detection (forecast vs actual)
- Seasonal decomposition for detecting deviations
- Full treatment of forecasting in Section 14

## 13.6 Evaluation
- Why accuracy is meaningless here (99.9% "normal" data)
- Precision@K, Recall at a fixed false-positive budget
- Precision-Recall AUC over ROC AUC
- The role of a human review queue (alerts, not automatic action)
- Delayed / weak labels: using post-hoc confirmed fraud to build eval sets

## 13.7 Production Considerations
- Alert fatigue and the cost of false positives
- Concept drift (normal behavior changes over time — retraining cadence)
- Thresholding for a target alert volume
- Explainability for each flagged anomaly (which features drove the score — link to Section 17)

---

## Hands-on Exercises
1. Compare Isolation Forest, LOF and One-Class SVM on a synthetic dataset with known anomalies.
2. Build a Mahalanobis-distance detector and compare it to Isolation Forest on multivariate data.
3. Simulate concept drift and show how a static anomaly detector degrades over time.

## Project — Fraud / Intrusion Detection Pipeline
Using a public fraud or network-intrusion dataset: build an unsupervised baseline (Isolation Forest), evaluate with Precision-Recall AUC and Precision@K, tune the threshold for a fixed daily alert budget, and add a simple explanation (top contributing features) to each alert.

## Recommended Resources
- *Outlier Analysis* (Charu Aggarwal)
- scikit-learn: Novelty and Outlier Detection guide
- PyOD library documentation (a dedicated anomaly-detection toolkit)

## Definition of Done
- [ ] Evaluation uses Precision-Recall AUC or Precision@K, not accuracy
- [ ] Each flagged anomaly comes with a reason, not just a score
