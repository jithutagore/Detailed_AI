# 12 — Unsupervised Learning

> **Goal:** Find structure in data without labels: groups, patterns and lower-dimensional representations.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** 01, 06

---

## Learning Objectives
- Apply the main clustering algorithms and evaluate clusters without ground truth
- Reduce dimensionality for visualization, compression and noise reduction
- Mine association rules
- Know where unsupervised methods feed into supervised pipelines and into RAG (embeddings)

---

## 12.1 Clustering
- **k-Means**: algorithm, initialization (k-means++), choosing k (elbow method, silhouette score)
- k-Means weaknesses: assumes spherical clusters, sensitive to scale and outliers
- **Hierarchical clustering**: agglomerative, linkage methods (single, complete, average, Ward), dendrograms
- **DBSCAN**: density-based, finds arbitrary shapes, handles noise/outliers, no need to pick k
- HDBSCAN (a practical improvement over DBSCAN)
- Gaussian Mixture Models (soft/probabilistic clustering, EM algorithm concept)
- Evaluating clusters: silhouette score, Davies-Bouldin index, Calinski-Harabasz index
- Evaluating against known labels (when available): Adjusted Rand Index, NMI

## 12.2 Dimensionality Reduction
- **PCA**: variance maximization, explained variance ratio, choosing the number of components, scree plots
- PCA for visualization, compression and noise reduction
- Limitations of PCA (linear only)
- **t-SNE**: non-linear, good for visualization, perplexity parameter, and its pitfalls (don't trust distances between clusters)
- **UMAP**: faster than t-SNE, better global structure, common default for embeddings visualization
- Autoencoders (bridge concept to Section 18 / deep learning)
- Feature selection vs feature extraction (the difference)

## 12.3 Association Rule Mining
- Support, confidence, lift
- Apriori algorithm, FP-Growth
- Market basket analysis

## 12.4 Density Estimation (awareness)
- Kernel Density Estimation (KDE)
- Use in anomaly detection (Section 13) and data visualization

## 12.5 Where Unsupervised Learning Meets Modern AI
- Embeddings as a learned representation (link to LLM Foundations)
- Clustering embeddings for topic discovery
- PCA/UMAP for visualizing embedding spaces
- k-Means for building coarse quantizers in vector search indexes (link to RAG vector DBs)

---

## Hands-on Exercises
1. Implement k-Means from scratch (Lloyd's algorithm) and verify against scikit-learn.
2. Compare k-Means, hierarchical and DBSCAN on datasets with non-spherical clusters (e.g. two moons).
3. Apply PCA to a high-dimensional dataset, plot explained variance, and reduce to 2D for visualization.
4. Compare PCA, t-SNE and UMAP visualizations of the same high-dimensional data.
5. Run Apriori on a transactions dataset and find the top association rules by lift.

## Project — Customer Segmentation
Cluster customers using RFM (Recency, Frequency, Monetary) or behavioral features. Choose the number of clusters with silhouette analysis, profile each segment, visualize with PCA/UMAP, and write a one-page recommendation per segment for a marketing team.

## Recommended Resources
- *An Introduction to Statistical Learning*, Chapter 12
- StatQuest: PCA, k-Means, Hierarchical Clustering, t-SNE
- UMAP documentation ("Understanding UMAP")

## Definition of Done
- [ ] Cluster count chosen with a documented method, not a guess
- [ ] Each cluster is profiled and named in business terms
