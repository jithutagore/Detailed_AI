# 01 — Deep Learning Foundations

> **Goal:** Understand what makes deep learning different from classical ML, set up a proper environment, and get comfortable with the core framework (PyTorch) before building any architecture.

**Level:** Foundation · **Time:** 1 week · **Prerequisites:** `ML\01_math_for_ml`, `ML\18_neural_network_basics` (MLP basics)

---

## Learning Objectives
- Explain what "deep" means and why depth matters
- Set up a GPU-enabled PyTorch environment
- Understand tensors, autograd, and the training loop at a framework level
- Know the deep learning landscape before diving into specific architectures

---

## 1.1 What Makes Learning "Deep"
- Recap: a single neuron/MLP (`ML\18`) vs stacking many layers
- **Representation learning**: instead of hand-engineering features (`ML\05`), the network learns its own hierarchical features
- Why depth matters: each layer builds more abstract representations on top of the last (edges → shapes → objects, in vision; characters → words → phrases, in text)
- The historical unlock: more data, more compute (GPUs), and architectural/training fixes (Section 03) made depth practical after decades of theory

## 1.2 The Deep Learning Landscape
- Supervised deep learning (classification, regression on unstructured data)
- Self-supervised learning (learning from the data's own structure — pretext tasks, masked prediction) — this is how modern foundation models are pretrained
- Generative deep learning (GANs, VAEs, diffusion — Sections 10–11)
- Deep reinforcement learning (Section 12)
- Where classical ML (`ML\`) still wins: tabular data, small datasets, interpretability needs
- Where deep learning wins: images, audio, text, video — unstructured, high-dimensional data with local/sequential structure

## 1.3 Environment & Tooling
- **PyTorch** as the primary framework for this syllabus (dominant in research and increasingly in production)
- TensorFlow/Keras (awareness — still common in some production stacks)
- GPU setup: CUDA basics, checking GPU availability, Google Colab/Kaggle for free GPU access
- Mixed precision training (concept, full treatment in Section 17)

## 1.4 PyTorch Fundamentals
- **Tensors**: creation, indexing, reshaping, broadcasting (parallels `ML\03` NumPy, but with GPU support)
- Moving tensors between CPU and GPU (`.to(device)`)
- **Autograd**: `requires_grad`, `.backward()`, computational graphs built automatically
- `nn.Module`: defining custom layers and models
- `nn.Parameter` vs regular tensors
- Loss functions (`nn.CrossEntropyLoss`, `nn.MSELoss`) and optimizers (`torch.optim`)
- The standard training loop: forward → loss → `zero_grad()` → `backward()` → `step()`
- `DataLoader` and `Dataset` for batching and data pipelines
- `model.train()` vs `model.eval()`, and why it matters (dropout, batch norm behave differently)

## 1.5 Datasets & Benchmarks You'll Use Throughout
- Vision: MNIST, Fashion-MNIST, CIFAR-10/100, ImageNet (awareness — too large for most personal projects)
- Text: IMDB reviews, AG News, small parallel corpora
- Standard train/val/test splits and why benchmark datasets matter for comparing architectures fairly

## 1.6 Reading Papers & Staying Current
- How to read a DL paper efficiently: abstract → figures → results → method
- arXiv, Papers with Code, and following the pace of the field
- Why this syllabus teaches the "why" behind each architecture — papers assume you already know the problem being solved

---

## Hands-on Exercises
1. Set up PyTorch with GPU support (locally or Colab) and verify `torch.cuda.is_available()`.
2. Recreate 3 NumPy operations from `ML\03` in PyTorch tensors and confirm identical results, then time CPU vs GPU for a large matrix multiply.
3. Build a `Dataset` and `DataLoader` for a small image folder; iterate through batches and visualize a few samples.
4. Rewrite your `ML\18` from-scratch NumPy MLP training loop using PyTorch's autograd instead — confirm matching results with far less code.

## Mini Project — PyTorch Training Loop Template
Build a reusable, well-structured PyTorch training script (train/validate loop, checkpointing, logging with TensorBoard or W&B, config via a YAML/dataclass) that you'll reuse as the base for every project in this folder.

## Recommended Resources
- PyTorch official "Deep Learning with PyTorch: A 60 Minute Blitz"
- *Dive into Deep Learning* (d2l.ai) — free, code-first, the best companion for this entire folder
- Andrej Karpathy, "Neural Networks: Zero to Hero" (micrograd — builds autograd from scratch)

## Definition of Done
- [ ] Your reusable training loop template works end-to-end on a toy dataset
- [ ] You can explain what autograd does without looking it up
