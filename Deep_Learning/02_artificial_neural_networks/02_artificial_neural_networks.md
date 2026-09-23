# 02 — Artificial Neural Networks (ANN & MLP)

> **Goal:** Master the fully-connected neural network in depth — the foundation every other architecture in this folder builds on or departs from. `ML\18` introduced this at a bridge level; this section goes to full depth with PyTorch idioms, deeper networks, and production-grade training practices.

**Level:** Foundation · **Time:** 2 weeks · **Prerequisites:** 01, `ML\18_neural_network_basics`

---

## Learning Objectives
- Build and train multi-layer perceptrons for real classification/regression tasks
- Choose activation functions, initialization schemes, and architectures deliberately, not by default
- Diagnose training problems from loss curves
- Understand exactly how backpropagation scales to deep networks

---

## 2.1 The Artificial Neuron — Recap & Extension
- Recap from `ML\18.1`: a neuron as weighted sum + activation
- **The biological inspiration and its limits** — why "artificial neural network" is a loose analogy, not a brain simulation
- Perceptron vs modern neuron: the historical perceptron's linear-separability limitation (XOR problem) and why stacking layers solves it

## 2.2 Network Architecture
- Input layer, hidden layers, output layer
- **Fully-connected (dense) layers**: every neuron connects to every neuron in the next layer
- Width vs depth: wider layers vs more layers — different capacity/generalization trade-offs
- Output layer design by task: single sigmoid (binary classification), softmax (multiclass), linear (regression), multiple sigmoids (multi-label)

## 2.3 Activation Functions — Deep Dive
- Recap from `ML\18.1`: sigmoid, tanh, ReLU
- **ReLU variants**: Leaky ReLU, Parametric ReLU (PReLU), ELU, GELU, Swish/SiLU — what problem each variant fixes
- Dying ReLU problem and its fixes
- Softmax for multiclass output, and its relationship to cross-entropy loss
- Choosing activations by layer position (hidden vs output) and by architecture (GELU is now standard in Transformers — preview of Section 07)

## 2.4 Weight Initialization — Deep Dive
- Recap from `ML\18.2`: why zero/naive initialization fails
- **Xavier/Glorot initialization** (for tanh/sigmoid) — the math intuition (preserving variance across layers)
- **He initialization** (for ReLU) — why ReLU needs a different scaling
- PyTorch defaults and when to override them

## 2.5 Backpropagation — Full Depth
- Recap from `ML\18.2`: the chain rule applied layer by layer
- Computing gradients for a network with an arbitrary number of layers (generalizing beyond the 2-layer case)
- Computational graphs and automatic differentiation (how PyTorch's autograd implements this generally)
- Gradient checking (verifying analytical gradients against numerical gradients) — a debugging technique worth doing once by hand

## 2.6 Loss Functions — Deep Dive
- Regression: MSE, MAE, Huber loss (robust to outliers)
- Classification: binary cross-entropy, categorical cross-entropy, the relationship to Maximum Likelihood Estimation (recap `ML\02.4`)
- Label smoothing (a regularization technique for classification)
- Custom loss functions in PyTorch

## 2.7 Building Deeper MLPs
- Stacking many hidden layers — and immediately hitting the vanishing/exploding gradient problem (full treatment in Section 03)
- Skip/residual connections — a first look (full treatment in Section 05 with ResNet)
- When an MLP is still the right choice: tabular data (though `ML\09` gradient boosting often still wins there), the final layers of every other architecture in this folder

## 2.8 Practical PyTorch Patterns
- `nn.Sequential` vs custom `nn.Module` subclasses
- Parameter counting and model summaries
- Saving/loading model weights (`state_dict`)
- Reproducibility: seeding, deterministic operations

---

## Hands-on Exercises
1. Implement full backpropagation for a 4-layer MLP by hand in NumPy (extending `ML\18`'s 2-layer version) and verify with gradient checking.
2. Compare Xavier vs He vs naive initialization on a 10-layer MLP; plot activation statistics per layer to see which initialization keeps signal healthy.
3. Train the same MLP with sigmoid, ReLU and GELU activations; compare convergence speed and final accuracy.
4. Build an MLP for tabular data and compare it against your `ML\09` gradient-boosting model on the same dataset — document which wins and why.

## Project — Deep MLP Image Classifier
Build and tune a deep MLP (5+ hidden layers) for Fashion-MNIST classification. Systematically ablate: activation function, initialization scheme, network depth/width, and regularization (dropout, weight decay — recap `ML\06.4`). Produce a report showing how each choice affects the loss curve and final accuracy, with a clear recommendation and reasoning.

## Recommended Resources
- *Dive into Deep Learning* (d2l.ai) — Chapters on MLPs
- 3Blue1Brown: "Neural Networks" series (revisit — the visual intuition deepens on a second pass)
- Glorot & Bengio, "Understanding the difficulty of training deep feedforward neural networks" (2010) — the Xavier initialization paper

## Definition of Done
- [ ] Your from-scratch backprop passes gradient checking within numerical tolerance
- [ ] You can explain, concretely, why He initialization pairs with ReLU and Xavier with tanh
- [ ] Your deep MLP project report shows a clear, evidenced recommendation for each architectural choice
