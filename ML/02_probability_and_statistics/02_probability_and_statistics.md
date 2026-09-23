# 02 — Probability & Statistics

> **Goal:** Reason about uncertainty, data distributions and experiments. Many ML models are probabilistic, and every evaluation is a statistical question.

**Level:** Foundation · **Time:** 3 weeks · **Prerequisites:** 01

---

## Learning Objectives
- Use probability rules, distributions and Bayes' theorem
- Summarize and describe data with descriptive statistics
- Run hypothesis tests and A/B tests correctly
- Understand maximum likelihood estimation, the basis of many loss functions

---

## 2.1 Probability Basics
- Sample spaces, events, axioms
- Conditional probability, independence
- **Bayes' theorem** (prior, likelihood, posterior)
- Law of total probability
- Random variables: discrete vs continuous
- PMF, PDF, CDF
- Expectation, variance, covariance, correlation
- Joint, marginal and conditional distributions

## 2.2 Common Distributions
- Discrete: Bernoulli, Binomial, Poisson, Geometric, Categorical/Multinomial
- Continuous: Uniform, **Normal (Gaussian)**, Exponential, Beta, Gamma, Student's t, Chi-squared
- Multivariate normal distribution
- When each distribution appears in real data

## 2.3 Descriptive Statistics
- Mean, median, mode; variance, standard deviation
- Percentiles, quartiles, IQR
- Skewness, kurtosis
- Correlation: Pearson vs Spearman; **correlation ≠ causation**
- Outliers and robust statistics

## 2.4 Sampling & Estimation
- Populations vs samples, sampling bias
- **Law of Large Numbers**, **Central Limit Theorem**
- Point estimates, standard error
- **Confidence intervals**
- Bootstrap resampling
- **Maximum Likelihood Estimation (MLE)**, and how it leads to MSE and cross-entropy losses
- Maximum a posteriori (MAP) estimation and its link to regularization

## 2.5 Hypothesis Testing
- Null and alternative hypotheses, p-values, significance level
- Type I and Type II errors, statistical power
- t-tests, chi-squared test, ANOVA, Mann-Whitney U
- Multiple-testing problem (Bonferroni, false discovery rate)
- Effect size vs statistical significance

## 2.6 Experimentation (A/B Testing)
- Designing an A/B test: metric, randomization unit, sample size
- Power analysis
- Peeking problems, sequential testing (concept)
- Common pitfalls: novelty effect, network effects, Simpson's paradox

## 2.7 Bayesian Thinking (intro)
- Priors and posteriors
- Conjugate priors (Beta–Binomial)
- Bayesian vs frequentist views
- Tools: PyMC (awareness)

## 2.8 Causal Inference (awareness)
- Confounders, randomized experiments vs observational data
- Causal graphs (DAGs), difference-in-differences, propensity scores (concepts)

---

## Hands-on Exercises
1. Simulate the Central Limit Theorem with dice rolls and plot the distribution of means.
2. Compute a bootstrap confidence interval for a median.
3. Run a t-test and a Mann-Whitney test on the same data and explain the difference.
4. Calculate the sample size needed for an A/B test detecting a 2% lift.
5. Show Simpson's paradox with a real dataset.

## Mini Project — A/B Test Analysis
Analyze a public A/B test dataset: check the randomization, compute the lift with a confidence interval, run the right test, and write a one-page decision memo.

## Recommended Resources
- *Think Stats* and *Think Bayes* (Allen Downey) — free
- StatQuest (Josh Starmer) videos
- *Practical Statistics for Data Scientists* (Bruce, Bruce, Gedeck)
- Seeing Theory (interactive visualizations)

## Definition of Done
- [ ] You can explain p-values and confidence intervals correctly
- [ ] You can derive MSE from a Gaussian MLE, at least intuitively
