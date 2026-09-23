# 21 — ML System Design

> **Goal:** Design complete ML systems end-to-end, the way you'd be asked to in a senior ML engineer interview or a real architecture review. This is where individual techniques come together into a coherent system.

**Level:** Production · **Time:** 2 weeks · **Prerequisites:** 11, 17, 20

---

## Learning Objectives
- Translate a business problem into an ML problem statement
- Design a full system: data, features, model, serving, monitoring
- Reason explicitly about trade-offs and non-functional requirements
- Practice the ML system design interview format

---

## 21.1 From Business Problem to ML Problem
- Clarifying questions: what decision will this prediction drive? what's the cost of being wrong?
- Is ML even the right approach? (vs rules, vs a simpler heuristic)
- Framing: classification vs regression vs ranking vs clustering vs forecasting
- Defining the **prediction target** precisely (and its edge cases)
- Success metrics: the ML metric AND the business metric, and how they connect

## 21.2 Design Framework
For any system, work through:
1. **Requirements**: functional (what it predicts) and non-functional (latency, throughput, scale, freshness)
2. **Data**: sources, labeling strategy, volume, quality, privacy constraints
3. **Features**: what's available at prediction time (training/serving skew risk)
4. **Model**: candidate approaches, and why
5. **Evaluation**: offline metrics, online A/B test design
6. **Serving**: batch vs real-time, latency budget
7. **Monitoring**: drift, performance decay, alerting
8. **Scale & cost**: back-of-envelope estimates

## 21.3 Key Trade-offs to Reason About
- Simple, interpretable model vs complex, higher-performing model
- Batch (cheap, stale) vs real-time (expensive, fresh) predictions
- Training/serving skew (the #1 real-world production bug source)
- Cold-start handling (new users, items, or entities with no history)
- Label latency (immediate feedback vs delayed/weak labels vs no labels)
- Class imbalance in the target problem
- Fairness constraints vs raw accuracy (link to Section 17)
- Build vs buy (a managed API vs a custom-trained model)

## 21.4 Common System Design Prompts (practice these)
1. **Fraud detection system** for a payments platform
2. **Search ranking** for an e-commerce site
3. **Feed ranking** for a social app
4. **Churn prediction** for a subscription business
5. **Dynamic pricing** system for ride-sharing
6. **Ad click-through-rate (CTR) prediction**
7. **Demand forecasting** for a logistics company
8. **Content moderation** classifier at scale
9. **Credit scoring** system with fairness and regulatory constraints
10. **Real-time anomaly detection** for infrastructure metrics

For each: work through the 8-step framework above, out loud or in writing, in about 45 minutes.

## 21.5 Reference Architecture
```
Data Sources → Ingestion → Feature Store (offline + online) → Training Pipeline
                                                                      ↓
                                                              Model Registry
                                                                      ↓
                                      ┌────────── Serving ───────────┐
                                      │  Batch scoring  |  Online API │
                                      └───────────────────────────────┘
                                                      ↓
                                        Monitoring (drift, performance)
                                                      ↓
                                          Retraining trigger → back to Training
```

## 21.6 Writing It Up
- One-page design docs: problem, approach, trade-offs, metrics, risks
- Diagrams that communicate the data flow, not just the model
- Back-of-envelope capacity estimates (requests/sec, storage, training time)

---

## Hands-on Exercises
1. Write a full design doc for 3 of the prompts in 21.4.
2. Do a mock system-design interview (self-recorded or with a peer) for one prompt, timed at 45 minutes.
3. Critique a real (public) ML system write-up (e.g. an engineering blog post) using the 8-step framework — what did they trade off, and why?

## Capstone-Prep Project — Full Design Doc
Pick one prompt from 21.4 that's different from your Section 22 capstone. Produce a complete design document (requirements, data, features, model, evaluation, serving, monitoring, scale estimate, risks) as if presenting it to a hiring panel or an architecture review board.

## Recommended Resources
- *Designing Machine Learning Systems* (Chip Huyen)
- *Machine Learning System Design Interview* (Ali Aminian, Alex Xu)
- Engineering blogs: Netflix, Uber, Airbnb, DoorDash, Instacart tech blogs (search their ML sections)

## Definition of Done
- [ ] 3 written design docs covering different problem types (ranking, classification, forecasting)
- [ ] You can complete a cold-start design discussion in 45 minutes without notes
