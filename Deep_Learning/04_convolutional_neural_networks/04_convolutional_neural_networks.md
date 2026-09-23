# 04 — Convolutional Neural Networks (CNN)

> **Goal:** Understand and implement CNNs in full depth — the architecture that made deep learning work for vision. This is the section that was previously only a stub elsewhere in your syllabus; it's now taught properly, from the convolution operation through a working image classifier.

**Level:** Core · **Time:** 3 weeks · **Prerequisites:** 02, 03, `AI\07_classical_perception_and_computer_vision` (recommended, not required)

---

## Learning Objectives
- Explain why fully-connected networks fail on images and what convolution fixes
- Implement convolutional and pooling layers, and understand their parameters in detail
- Build a complete CNN image classifier from scratch in PyTorch
- Visualize and interpret what a CNN has learned

---

## 4.1 Why MLPs Fail on Images
- An MLP treats an image as a flat vector — it **destroys spatial structure** (a pixel and its neighbor become just two unrelated inputs)
- Parameter explosion: a fully-connected layer on a modest image has millions of weights per layer
- No **translation invariance**: an MLP must separately learn to recognize a cat in the top-left and a cat in the bottom-right
- This section's central idea: convolution encodes two priors directly into the architecture — **locality** (nearby pixels matter more) and **translation invariance** (the same feature detector slides across the whole image)

## 4.2 The Convolution Operation
- Recap `AI\07.2`: classical convolution (fixed filters like Sobel/Gaussian)
- **The key shift**: in a CNN, the filter's weights are **learned**, not hand-designed
- Convolution mechanics: kernel/filter, stride, padding (valid vs same), computing output size
- **Feature maps**: what a convolutional layer's output represents
- Multiple filters per layer → multiple feature maps → a "volume" of activations
- Channels: how convolution handles multi-channel input (RGB) and multi-channel intermediate feature maps

## 4.3 Pooling Layers
- **Max pooling**: downsampling by taking the maximum in each window — why it provides translation invariance and reduces computation
- Average pooling
- Global Average Pooling (GAP) — a modern alternative to flattening before the final classifier layer
- Why pooling is being phased out in some modern architectures in favor of strided convolutions (awareness)

## 4.4 Building a CNN
- Typical architecture pattern: `[Conv → Activation → Pool] × N → Flatten/GAP → Fully-Connected → Output`
- Receptive field: how it grows with depth, and why deeper layers "see" more of the original image
- Calculating output dimensions through a stack of conv/pool layers
- 1x1 convolutions ("network in network") — dimensionality reduction/channel mixing, a building block for later architectures (Section 05)

## 4.5 Training CNNs
- Applying Section 03's training toolkit specifically to CNNs: BatchNorm placement in conv blocks, appropriate weight initialization (He init, given ReLU is standard here)
- **Data augmentation for images**: random crop, flip, rotation, color jitter, cutout — why this is especially important for vision (limited data, strong translation/scale invariance priors help)
- Normalizing input images (mean/std normalization, per-channel)

## 4.6 Visualizing & Interpreting CNNs
- Visualizing learned filters (especially interpretable in the first layer — edges, colors, textures)
- Feature map visualization at different depths (recap the "edges → shapes → objects" hierarchy from Section 01.1)
- **Class Activation Maps (CAM) / Grad-CAM**: which parts of the image drove a prediction — a vision-specific parallel to `ML\17`'s explainability methods
- Adversarial examples (awareness): small perturbations that fool a CNN — a preview of robustness concerns

## 4.7 CNN Design Considerations
- Depth vs width trade-offs (revisited for conv architectures specifically)
- Computational cost: FLOPs, parameter count as a function of kernel size, channels, depth
- Why kernel size 3x3 became a near-universal default (stacking small kernels vs one large kernel — same receptive field, fewer parameters, more non-linearity)

---

## Hands-on Exercises
1. Implement a 2D convolution operation from scratch in NumPy (no PyTorch) and verify it matches `nn.Conv2d`'s output on the same input/weights.
2. Manually calculate output dimensions through a 4-layer conv/pool stack, then verify with PyTorch.
3. Train a small CNN on CIFAR-10 with and without data augmentation; compare validation accuracy and overfitting behavior.
4. Visualize first-layer filters and Grad-CAM heatmaps for a trained CNN classifier.

## Project — CNN Image Classifier from Scratch
Build and train a CNN (not a pretrained model — architecture designed and trained by you) for a multi-class image classification task (CIFAR-10 or a custom dataset). Include: a documented architecture design with reasoning for each choice, full training diagnostics (Section 03's toolkit), data augmentation, and Grad-CAM visualizations explaining several predictions (correct and incorrect). This is the direct prerequisite for Section 05's transfer learning and Section 13's CV applications.

## Recommended Resources
- CS231n (Stanford), "Convolutional Neural Networks for Visual Recognition" — the standard course for this exact topic, lecture notes freely available
- *Dive into Deep Learning* (d2l.ai) — CNN chapters
- Zeiler & Fergus, "Visualizing and Understanding Convolutional Networks" (2014)
- Selvaraju et al., "Grad-CAM" (2017)

## Definition of Done
- [ ] Your from-scratch convolution implementation matches PyTorch's output exactly
- [ ] You can compute the output shape of any conv/pool stack by hand
- [ ] Your CNN classifier's Grad-CAM visualizations make intuitive sense for at least 5 example predictions
