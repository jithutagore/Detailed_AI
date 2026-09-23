# 01 — Math for Machine Learning

> **Goal:** Learn the linear algebra, calculus and optimization behind ML algorithms well enough to read their equations and implement them from scratch.

**Level:** Foundation · **Time:** 3–4 weeks · **Prerequisites:** High-school algebra

---

## Learning Objectives
- Work with vectors and matrices, and understand what the operations mean geometrically
- Compute derivatives and gradients, and apply the chain rule
- Explain gradient descent and its variants
- Implement the math in NumPy

---

## 1.1 Linear Algebra
- Scalars, vectors, matrices, tensors
- Vector operations: addition, scalar multiplication, **dot product**, norms (L1, L2, L∞)
- Geometric meaning: length, angle, projection, **cosine similarity**
- Matrix operations: multiplication, transpose, identity, inverse, determinant
- Linear transformations (a matrix as a function that moves space)
- Systems of linear equations, rank, linear independence, span, basis
- **Eigenvalues and eigenvectors** (and why they matter for PCA)
- **Singular Value Decomposition (SVD)**
- Matrix factorization concepts (for recommenders)
- Orthogonality, orthonormal bases
- Positive definite matrices (covariance matrices)

## 1.2 Calculus
- Functions, limits, continuity
- Derivatives and rules (power, product, quotient, **chain rule**)
- Partial derivatives
- **Gradient** (the direction of steepest increase)
- Jacobian and Hessian (concepts)
- Derivatives of common ML functions: sigmoid, softmax, log, squared error, cross-entropy
- Integrals (enough for probability densities)
- Taylor series intuition (why gradient descent works locally)

## 1.3 Optimization
- Objective / loss functions
- Convex vs non-convex functions, local vs global minima
- **Gradient descent**: learning rate, convergence, divergence
- Batch vs stochastic vs mini-batch gradient descent
- Momentum, RMSProp, **Adam** (intuition)
- Closed-form solutions (normal equation for linear regression)
- Constrained optimization and Lagrange multipliers (concept, needed for SVMs)
- Regularization as an optimization penalty

## 1.4 Information Theory (intro)
- Entropy
- Cross-entropy
- KL divergence
- Information gain (used by decision trees)

---

## Hands-on Exercises
1. Implement vector and matrix operations in plain Python, then in NumPy, and compare speed.
2. Visualize a 2×2 matrix transforming a grid of points.
3. Compute eigenvectors of a covariance matrix and plot them over the data.
4. Implement gradient descent to minimize `f(x, y) = x² + 3y²` and plot the path for 3 learning rates.
5. Derive and code the gradient of mean squared error for linear regression.

## Mini Project — Linear Regression from Scratch
Fit a linear regression with (a) the normal equation and (b) gradient descent in NumPy only. Compare with scikit-learn and plot the loss curve.

## Recommended Resources
- 3Blue1Brown: "Essence of Linear Algebra" and "Essence of Calculus"
- *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — free PDF
- Khan Academy (linear algebra, multivariable calculus)
- Gilbert Strang, MIT 18.06 Linear Algebra

## Definition of Done
- [ ] You can explain the dot product, eigenvectors and gradients geometrically
- [ ] Linear regression from scratch matches scikit-learn's result
