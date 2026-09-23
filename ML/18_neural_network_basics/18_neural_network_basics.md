# 18 — Neural Network Basics  *(Bridge section)*

> **Goal:** Understand the fundamentals of neural networks well enough to know when to reach for deep learning instead of classical ML, and to make the jump into a dedicated Deep Learning syllabus a small step instead of a cliff.
> **Note:** This is a bridge section, not a full deep learning course. Full coverage (CNNs, RNNs, transformers, computer vision, speech, training at scale) belongs in the planned Deep Learning folder.

**Level:** Bridge · **Time:** 2 weeks · **Prerequisites:** 01, 06, 07

---

## Learning Objectives
- Explain how a neural network computes a prediction and learns via backpropagation
- Build a simple feedforward network from scratch and in PyTorch
- Recognize overfitting-control techniques specific to neural nets
- Decide when a neural network is (and isn't) the right tool versus gradient boosting

---

## 18.1 From Linear Models to Neural Networks
- A single neuron = logistic regression with an activation function
- Stacking neurons into layers: the multilayer perceptron (MLP)
- **Activation functions**: sigmoid, tanh, ReLU, Leaky ReLU, GELU — why ReLU largely replaced sigmoid/tanh in hidden layers
- Universal approximation theorem (concept, not proof)

## 18.2 Forward & Backward Pass
- Forward propagation: computing the output layer by layer
- Loss functions revisited: MSE (regression), cross-entropy (classification)
- **Backpropagation**: the chain rule applied layer by layer (link to Section 01.2)
- Computational graphs (concept — this is what PyTorch/TensorFlow automate)
- Weight initialization (why zeros/large values break training; Xavier/He initialization)

## 18.3 Training Neural Networks
- Gradient descent variants revisited: SGD, momentum, **Adam** (Section 01.3)
- Learning rate schedules (step decay, cosine annealing, warmup)
- Batch size effects
- Epochs, iterations, monitoring train/validation loss curves
- Vanishing and exploding gradients (why deep networks are hard to train)

## 18.4 Regularization for Neural Networks
- **Dropout**
- **Batch normalization** / layer normalization (concept)
- Weight decay (L2, revisited in the neural-net context)
- Early stopping (revisited)
- Data augmentation (concept — full treatment in deep learning)

## 18.5 Architecture Basics (awareness only — depth in the DL folder)
- Feedforward / fully-connected networks — this section's main focus
- Convolutional Neural Networks (CNNs) — what they're for (images), why convolution matters
- Recurrent Neural Networks (RNNs, LSTM, GRU) — what they're for (sequences)
- The Transformer / attention mechanism — link back to the AI Agents syllabus, Section 03 (LLM Foundations), which covers this in depth

## 18.6 Frameworks
- **PyTorch** basics: tensors, autograd, `nn.Module`, optimizers, training loops
- TensorFlow/Keras (awareness — know it exists, many production systems still use it)
- GPU vs CPU training (why it matters, when it's necessary)

## 18.7 Neural Networks vs Classical ML
- Tabular data: gradient boosting (Section 09) usually still wins — neural nets need much more data and tuning to compete
- Unstructured data (images, audio, text, video): neural networks are the default
- Data volume, interpretability needs, and training infrastructure as deciding factors

---

## Hands-on Exercises
1. Implement a 2-layer MLP with forward and backward pass in plain NumPy (no autograd) for a binary classification toy dataset.
2. Rebuild the same network in PyTorch using `nn.Module` and an optimizer; confirm matching results.
3. Visualize training/validation loss with and without dropout to see overfitting control in action.
4. Train the same MLP with SGD vs Adam and compare convergence speed.
5. On one tabular dataset, compare a tuned MLP against your Section 09 gradient-boosting model.

## Mini Project — MLP from Scratch, Then in PyTorch
Implement, train and evaluate a feedforward neural network on the MNIST or Fashion-MNIST dataset: once in raw NumPy (forward/backward pass, no autograd), then in PyTorch. Compare code complexity, training time and final accuracy.

## Recommended Resources
- 3Blue1Brown: "Neural Networks" series (the best visual intuition)
- Andrej Karpathy, "Neural Networks: Zero to Hero" (micrograd, makemore)
- *Deep Learning* (Goodfellow, Bengio, Courville) — free online, Chapters 6–8
- PyTorch official "60 Minute Blitz" tutorial

## Definition of Done
- [ ] Your from-scratch MLP trains and its gradients match PyTorch's autograd (checked numerically)
- [ ] You can explain, without notes, why ReLU helps with vanishing gradients
- [ ] You know, for your own next project, whether it calls for classical ML or deep learning — and why
