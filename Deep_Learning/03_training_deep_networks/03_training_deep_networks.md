# 03 — Training Deep Networks

> **Goal:** Master the practical engineering of training deep networks reliably — optimizers, normalization, regularization, and debugging. This is the "why deep learning actually works in practice" section, and every architecture in Sections 04–11 depends on these techniques.

**Level:** Foundation · **Time:** 2 weeks · **Prerequisites:** 02

---

## Learning Objectives
- Explain and use modern optimizers beyond vanilla SGD
- Apply normalization techniques and explain why they stabilize training
- Regularize deep networks against overfitting
- Systematically debug a network that won't train

---

## 3.1 The Vanishing/Exploding Gradient Problem — Full Treatment
- Recap: why this happens mathematically (repeated multiplication of small/large gradients through many layers via the chain rule)
- Why it gets worse with depth and with sigmoid/tanh activations
- Symptoms: loss plateaus immediately, or loss becomes NaN
- This single problem motivates most of what follows in this section

## 3.2 Optimizers — Deep Dive
- Recap `ML\01.3`: SGD, momentum
- **RMSProp**: adapting the learning rate per parameter based on recent gradient magnitudes
- **Adam**: combining momentum + RMSProp-style adaptive rates — why it's the default choice for most deep learning
- AdamW (decoupled weight decay — now standard, especially for Transformers)
- Learning rate schedules: step decay, cosine annealing, **warmup** (critical for Transformers, Section 07)
- Learning rate finders (a practical technique for picking a starting learning rate)
- Gradient clipping (capping gradient norm — essential for RNNs, Section 06)

## 3.3 Normalization Techniques
- **Batch Normalization**: normalizing activations across the batch dimension, why it stabilizes and accelerates training, train vs eval mode behavior
- **Layer Normalization**: normalizing across features instead of the batch — why Transformers use this instead of BatchNorm (independence from batch size, works for sequences)
- Group Normalization, Instance Normalization (awareness — used in specific vision/style-transfer contexts)
- Where to place normalization layers (before or after activation — a genuinely debated practical choice)

## 3.4 Regularization for Deep Networks
- Recap `ML\06.4`: L1/L2 weight decay
- **Dropout**: randomly zeroing activations during training, why it acts like implicit ensembling, dropout rate tuning
- **Data augmentation** as regularization (full technique details in Section 05 for images, awareness for text/audio)
- Early stopping (recap, applied to deep nets specifically)
- Label smoothing (recap from Section 02.6)
- Mixup / CutMix (awareness — advanced augmentation-as-regularization for vision)

## 3.5 Residual Connections & Deep Network Training
- **Skip/residual connections**: `output = F(x) + x` — how this lets gradients flow directly through many layers
- Why this was the key unlock for training very deep networks (preview of ResNet, Section 05)
- Highway networks (historical precursor, awareness)

## 3.6 Hyperparameter Tuning for Deep Learning
- What to tune: learning rate (most important), batch size, network depth/width, regularization strength
- Learning rate vs batch size relationship (linear scaling rule, awareness)
- Random search over grid search (recap `ML\11.5`) — even more true for deep learning given training cost
- Practical budget-aware tuning: coarse-to-fine search

## 3.7 Debugging Training
- A systematic checklist: can the model overfit a tiny subset (sanity check)? Is the loss decreasing at all? Are gradients flowing (check gradient norms per layer)? Is data being loaded/labeled correctly?
- Common bugs: forgetting `.zero_grad()`, mismatched loss function and output activation, learning rate too high (NaN loss) or too low (no progress), data leakage between train/val
- Visualizing training: loss curves, gradient norm histograms, activation distributions

## 3.8 Experiment Tracking for Deep Learning
- TensorBoard and Weights & Biases (recap `ML\20.2`, applied here to training curves, sample predictions, gradient histograms)
- Logging what matters: train/val loss, learning rate schedule, sample outputs over training

---

## Hands-on Exercises
1. Train a deep MLP with and without BatchNorm on the same task; compare training speed and stability.
2. Implement dropout from scratch (manual masking) and verify it matches PyTorch's `nn.Dropout` behavior in train vs eval mode.
3. Deliberately break training 4 different ways (too-high LR, no gradient clipping on an unstable model, wrong loss/activation pairing, frozen weights) and diagnose each from the loss curve alone.
4. Compare SGD, SGD+momentum, RMSProp and Adam on the same network; plot convergence speed.

## Project — Training Diagnostics Toolkit
Build a reusable PyTorch training wrapper that automatically logs gradient norms per layer, activation statistics, and loss curves to TensorBoard/W&B, and includes a "sanity check" mode that overfits a single batch to verify the pipeline is correct before a full run. Use it to systematically debug 3 intentionally broken training runs.

## Recommended Resources
- Andrej Karpathy, "A Recipe for Training Neural Networks" (essential practical debugging guide)
- Ioffe & Szegedy, "Batch Normalization" (2015) — the original paper
- *Dive into Deep Learning* (d2l.ai) — optimization and normalization chapters

## Definition of Done
- [ ] You can diagnose a broken training run from its loss curve alone, without seeing the code
- [ ] Your training wrapper catches at least one of the 4 intentional bugs automatically (via the sanity-check overfitting test)
