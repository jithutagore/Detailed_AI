# 05 — Data Preprocessing & Feature Engineering

> **Goal:** Turn raw data into model-ready features without leaking information, using reproducible pipelines.
> **Note:** This section covers ML-specific preprocessing. Large-scale data pipelines (ETL, Spark, warehouses) belong in the planned data engineering folder.

**Level:** Foundation · **Time:** 2 weeks · **Prerequisites:** 04

---

## Learning Objectives
- Handle missing values, outliers, categorical and text features correctly
- Scale and transform features for the models that need it
- Engineer useful features from domain knowledge
- Build leakage-free preprocessing with scikit-learn pipelines

---

## 5.1 Handling Missing Data
- Deletion (rows or columns) and when it's acceptable
- Simple imputation: mean, median, mode, constant
- Advanced imputation: KNN imputer, iterative imputer (MICE)
- Missing-indicator features (missingness can itself be informative)
- Models that handle missing values natively (gradient boosting)

## 5.2 Outliers
- Detect: IQR, z-score, isolation forest
- Treat: remove, cap/winsorize, transform, or keep (they may be real)
- Domain judgment beats rules

## 5.3 Encoding Categorical Features
- One-hot encoding (and the dummy-variable trap)
- Ordinal encoding (for ordered categories)
- **Target / mean encoding** (with cross-fitting to avoid leakage)
- Frequency / count encoding
- Binary and hashing encoding (high cardinality)
- Handling rare and unseen categories
- Native categorical support (CatBoost, LightGBM)

## 5.4 Scaling & Transformations
- Standardization (z-score), min-max scaling, robust scaling
- Which models need scaling (linear models, SVM, kNN, neural nets) and which don't (trees)
- Log, square-root, Box-Cox, Yeo-Johnson transforms for skewed data
- Binning / discretization
- Normalization (unit vectors)

## 5.5 Feature Engineering
- **Domain features** (ratios, differences, per-unit values)
- Interaction features, polynomial features
- **Datetime features**: day of week, month, holidays, time since event, cyclical encoding (sin/cos)
- **Aggregation features** (customer-level stats: count, mean, last value, trends)
- Lag and rolling-window features (time series)
- Geospatial features (distances, clusters)
- Text features (length, counts, TF-IDF; see Section 16)
- Automated feature engineering (Featuretools) — awareness

## 5.6 Feature Selection
- Filter methods: variance threshold, correlation, mutual information, chi-squared
- Wrapper methods: recursive feature elimination (RFE)
- Embedded methods: L1 (Lasso), tree feature importance
- Permutation importance
- Removing redundant (highly correlated) features

## 5.7 Imbalanced Data
- Resampling: random over/under-sampling, SMOTE and variants (imbalanced-learn)
- Class weights
- Threshold tuning (often better than resampling)
- Choosing metrics that suit imbalance (Section 11)

## 5.8 Data Leakage (critical)
- Target leakage (features that contain the answer)
- Train-test contamination (fitting the scaler or imputer on all data)
- Temporal leakage (using future information)
- Group leakage (the same customer in train and test)
- Prevention: split first, fit on train only, use pipelines

## 5.9 scikit-learn Pipelines
- `Pipeline`, `ColumnTransformer`, `make_pipeline`
- Custom transformers (`BaseEstimator`, `TransformerMixin`, `FunctionTransformer`)
- Pipelines inside cross-validation and grid search
- Saving pipelines together with the model

## 5.10 Data Splitting
- Train / validation / test splits
- Stratified splits
- **Time-based splits**
- **Group splits** (GroupKFold)

---

## Hands-on Exercises
1. Show leakage: scale before splitting vs after, and compare the scores.
2. Compare one-hot, target encoding and CatBoost native handling on a high-cardinality feature.
3. Build a `ColumnTransformer` pipeline for mixed numeric, categorical and datetime data.
4. Compare SMOTE, class weights and threshold tuning on an imbalanced dataset.

## Mini Project — Feature Engineering for Loan Default Prediction
Starting from raw loan data: build a full preprocessing pipeline, engineer at least 10 domain features, select features, and show the gain over a baseline with raw features only.

## Recommended Resources
- *Feature Engineering and Selection* (Kuhn & Johnson) — free online
- scikit-learn user guide: preprocessing and pipelines
- Kaggle Learn: Feature Engineering

## Definition of Done
- [ ] All preprocessing lives inside a pipeline
- [ ] A written leakage check for your project
