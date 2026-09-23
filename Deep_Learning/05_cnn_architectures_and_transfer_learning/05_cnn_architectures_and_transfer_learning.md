# 05 — CNN Architectures & Transfer Learning

> **Goal:** Study the landmark CNN architectures that shaped the field, and learn transfer learning — the technique that makes deep learning practical without training from scratch on massive datasets.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** 04

---

## Learning Objectives
- Trace the evolution of CNN architectures and the specific problem each one solved
- Understand and implement residual connections
- Apply transfer learning and fine-tuning effectively
- Choose the right pretrained architecture for a given constraint (accuracy, speed, size)

---

## 5.1 The Architecture Evolution (learn each as "what problem did this solve?")
- **LeNet-5** (1998): the original CNN, digit recognition — historical starting point
- **AlexNet** (2012): the ImageNet breakthrough — ReLU, dropout, GPU training at scale; why this paper reignited the entire field (link back to `AI\01.2`)
- **VGGNet** (2014): the case for depth with small, uniform 3x3 kernels (recap Section 04.7)
- **GoogLeNet/Inception** (2014): the inception module — parallel convolutions at multiple kernel sizes, computational efficiency via 1x1 convolutions
- **ResNet** (2015): **residual/skip connections** solve the degradation problem (deeper networks getting *worse*, not from overfitting but from optimization difficulty) — this is arguably the single most influential architectural idea in deep learning, reused far beyond vision (Transformers use residual connections too — preview of Section 07)
- **DenseNet** (2017): connecting every layer to every other layer — feature reuse
- **MobileNet / EfficientNet**: designing for efficiency — depthwise separable convolutions, compound scaling (balancing depth/width/resolution together)
- **Vision Transformer (ViT)** (2020): applying the Transformer architecture (Section 07) directly to images, treating patches as tokens — awareness here, full understanding follows naturally after Section 07

## 5.2 Why Residual Connections Work
- Full mathematical intuition: `output = F(x) + x` lets the network learn a small correction instead of a full transformation, and lets gradients flow directly backward through the identity path
- Recap Section 03.5's introduction — this section makes it concrete with ResNet's actual results
- Residual blocks, bottleneck blocks (1x1 → 3x3 → 1x1, used in deeper ResNets for efficiency)

## 5.3 Transfer Learning — Core Concept
- Why train from scratch when a model already learned generic visual features (edges, textures, shapes) from millions of images?
- **Feature extraction**: freeze the pretrained backbone, train only a new classifier head
- **Fine-tuning**: unfreeze some or all pretrained layers, train with a small learning rate
- Choosing which layers to freeze based on dataset size and similarity to the pretrained domain
- Discriminative learning rates (different learning rates for different depth layers)

## 5.4 Practical Transfer Learning Workflow
- Loading pretrained weights (`torchvision.models`, Hugging Face `timm`)
- Adapting the input pipeline to match pretrained normalization statistics
- Replacing and training the final classification layer
- Progressive unfreezing strategy
- When transfer learning doesn't help (domain is too different from the pretraining data — e.g. medical imaging, satellite imagery)

## 5.5 Choosing an Architecture in Practice
- Accuracy vs latency vs model size trade-offs
- Benchmarks: ImageNet top-1 accuracy, FLOPs, parameter count, inference latency on target hardware
- Practical defaults: ResNet-50 as a strong general baseline, EfficientNet/MobileNet for edge deployment, ViT for large-data/large-compute settings

---

## Hands-on Exercises
1. Implement a residual block from scratch and build a small ResNet (e.g. ResNet-18-scale) for CIFAR-10; compare training stability against an equally deep plain CNN without skip connections.
2. Load a pretrained ResNet-50, freeze the backbone, and fine-tune only the classifier head on a small custom image dataset (feature extraction).
3. Repeat with full fine-tuning (unfrozen backbone, small learning rate) and compare accuracy and training time.
4. Compare 3 pretrained architectures (ResNet, EfficientNet, MobileNet) on the same custom dataset: accuracy, inference latency, model size.

## Project — Transfer Learning for a Custom Classification Task
Pick a real, specific image classification problem (plant disease, product defect detection, a personal photo category of your choice) with a modestly sized dataset (a few hundred to a few thousand images per class). Apply transfer learning end-to-end: pretrained backbone selection with justification, appropriate freezing/fine-tuning strategy, data augmentation (Section 04.5), and a final comparison against a from-scratch CNN (Section 04's project) on the same data — quantify the transfer learning advantage.

## Recommended Resources
- He et al., "Deep Residual Learning for Image Recognition" (2015) — the ResNet paper
- CS231n (Stanford) — transfer learning lecture and notes
- `torchvision.models` and Hugging Face `timm` documentation
- Sebastian Ruder, "Transfer Learning - Machine Learning's Next Frontier" (blog)

## Definition of Done
- [ ] Your ResNet-with-skip-connections trains more stably (deeper) than the plain CNN equivalent
- [ ] Your transfer learning project measurably outperforms training from scratch on limited data
- [ ] You can explain why residual connections matter beyond vision (name where else they're used)
