# 03 — Python for Machine Learning

> **Goal:** Become fluent in the Python data stack used in every ML project: NumPy, pandas, visualization, scikit-learn basics and notebooks.
> **Note:** General Python (OOP, typing, async) is covered in the AI Agents syllabus, Section 01. This section focuses on data and ML libraries.

**Level:** Foundation · **Time:** 2 weeks · **Prerequisites:** Basic Python

---

## Learning Objectives
- Manipulate arrays with NumPy using vectorized code instead of loops
- Load, clean, reshape and aggregate data with pandas (and know Polars)
- Create clear plots with Matplotlib and Seaborn
- Set up reproducible ML environments

---

## 3.1 Environment Setup
- `uv` / `venv` / conda environments
- Jupyter Notebook, JupyterLab, VS Code notebooks, Google Colab, Kaggle notebooks
- When to move code from notebooks into `.py` modules
- Reproducibility: pinned dependencies, random seeds

## 3.2 NumPy
- `ndarray`: shape, dtype, reshaping, indexing, slicing
- **Vectorization** and **broadcasting**
- Universal functions, aggregations along axes
- Boolean masks, fancy indexing
- Linear algebra: `@`, `np.linalg` (inv, eig, svd, solve)
- Random numbers (`np.random.default_rng`)
- Memory and speed: views vs copies

## 3.3 pandas
- `Series` and `DataFrame`, reading CSV/Excel/Parquet/JSON/SQL
- Selecting: `loc`, `iloc`, boolean filtering, `query`
- Missing values: `isna`, `fillna`, `dropna`
- Data types, categoricals, datetime handling
- `groupby` + aggregation, `pivot_table`, `melt`, `stack`/`unstack`
- `merge`/`join`/`concat`
- `apply` vs vectorized operations (and why `apply` is slow)
- Method chaining
- Time-series tools: `resample`, `rolling`, `shift`
- Working with large data: chunks, Parquet, dtype optimization

## 3.4 Polars & Other Tools (awareness)
- **Polars** (fast, lazy DataFrames)
- DuckDB (SQL on local files)
- When pandas is too slow and what to switch to

## 3.5 Visualization
- **Matplotlib**: figure/axes model, line, bar, scatter, histogram, subplots
- **Seaborn**: distributions, categorical plots, pair plots, heatmaps
- **Plotly**: interactive charts
- Choosing the right chart; labeling axes and units; avoiding misleading charts

## 3.6 scikit-learn Basics
- The estimator API: `fit`, `predict`, `transform`, `fit_transform`
- `train_test_split`
- Built-in datasets for practice
- Pipelines (preview of Section 05)

## 3.7 Good Practices
- Project structure for ML (data/, notebooks/, src/, models/, reports/)
- Git for ML projects (don't commit large data; `.gitignore`)
- Unit tests for data functions (pytest)

---

## Hands-on Exercises
1. Rewrite a loop-based distance calculation using broadcasting and measure the speedup.
2. Clean a messy CSV (wrong types, missing values, duplicates) with pandas method chaining.
3. Answer 10 business questions on a sales dataset with `groupby` and `pivot_table`.
4. Recreate the same analysis in Polars or DuckDB and compare speed.

## Mini Project — Exploratory Report on a Public Dataset
Pick a Kaggle dataset, clean it, answer 5 questions with pandas, and produce 6 clear charts in a notebook with written conclusions.

## Recommended Resources
- *Python for Data Analysis* (Wes McKinney, creator of pandas)
- *Python Data Science Handbook* (Jake VanderPlas) — free online
- Kaggle Learn: Python, pandas, Data Visualization

## Definition of Done
- [ ] No Python loops where vectorized code would work
- [ ] A clean, reproducible notebook on GitHub
