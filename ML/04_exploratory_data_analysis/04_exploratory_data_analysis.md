# 04 — Exploratory Data Analysis (EDA)

> **Goal:** Understand a dataset before modeling it: its structure, quality, distributions, relationships and possible problems.

**Level:** Foundation · **Time:** 1–2 weeks · **Prerequisites:** 02, 03

---

## Learning Objectives
- Follow a systematic EDA process on any new dataset
- Spot data quality issues, leakage risks and biases early
- Form hypotheses that guide feature engineering and model choice
- Communicate findings clearly

---

## 4.1 The EDA Process
1. Understand the problem and what each row represents (the "unit of analysis")
2. Read the data dictionary; check the column types
3. Data quality checks
4. Univariate analysis
5. Bivariate / multivariate analysis
6. Target analysis
7. Write down findings, hypotheses and next steps

## 4.2 Data Quality Checks
- Shape, types, memory
- Missing values: counts, patterns, missingness mechanisms (MCAR, MAR, MNAR)
- Duplicates (exact and near-duplicates)
- Invalid values (negative ages, future dates, impossible combinations)
- Inconsistent categories ("NY", "New York", "new york")
- Outliers: IQR, z-score, domain rules
- Cardinality of categorical columns
- Constant or near-constant columns

## 4.3 Univariate Analysis
- Numeric: histograms, KDE, box plots, summary statistics, skewness
- Categorical: frequency tables, bar charts, rare categories
- Datetime: ranges, gaps, seasonality

## 4.4 Bivariate & Multivariate Analysis
- Numeric vs numeric: scatter plots, correlation matrices (Pearson, Spearman)
- Categorical vs numeric: grouped box plots, violin plots
- Categorical vs categorical: crosstabs, chi-squared, Cramér's V
- Pair plots
- Multicollinearity (VIF)
- Dimensionality reduction for visualization (PCA, t-SNE, UMAP; details in Section 12)

## 4.5 Target Analysis
- Class balance (classification) or target distribution (regression)
- Relationship of each feature with the target
- **Leakage detection**: features that are "too good" or only known after the outcome
- Time trends in the target

## 4.6 Bias & Representativeness
- Is the sample representative of the population the model will serve?
- Group imbalances (by region, gender, age, device)
- Data collection biases

## 4.7 Automated EDA Tools
- ydata-profiling (formerly pandas-profiling), Sweetviz, D-Tale
- Useful for a first look, but no substitute for thinking

## 4.8 Communicating Findings
- An EDA summary: key facts, issues found, decisions taken
- Charts with a clear message (title = the takeaway)

---

## Hands-on Exercises
1. Run a full EDA on the Titanic or House Prices dataset following the 7-step process.
2. Find a leakage feature in a provided dataset and explain why it leaks.
3. Compare an automated profiling report with your manual EDA: what did each miss?

## Mini Project — EDA Report for a Business Stakeholder
Pick a real-world dataset (e.g. customer churn, loans, e-commerce). Deliver a notebook plus a 1-page summary: data quality issues, key drivers of the target, risks, and recommended next steps.

## Definition of Done
- [ ] A reusable EDA checklist you apply to every new dataset
- [ ] Findings written for a non-technical reader
