# 10 — Generative Models: GANs & VAEs

> **Goal:** Learn the two foundational approaches to deep generative modeling that predate and set up diffusion models: Variational Autoencoders (probabilistic, likelihood-based) and Generative Adversarial Networks (adversarial training). Understanding both makes Section 11's diffusion models far more intuitive.

**Level:** Applied · **Time:** 2 weeks · **Prerequisites:** 02, 03, 04

---

## Learning Objectives
- Explain what a generative model is and how it differs from the discriminative models built so far
- Implement autoencoders and variational autoencoders
- Implement a basic GAN and understand adversarial training dynamics
- Know each approach's specific failure modes

---

## 10.1 Discriminative vs Generative Modeling
- Recap: everything through Section 09 has been discriminative (learning P(y|x) — predict a label/next-token from input) or representation-focused
- **Generative modeling**: learning to produce new samples resembling the training data — modeling P(x) or P(x|z)
- Why this is harder: you need the model to capture the full data distribution, not just a decision boundary

## 10.2 Autoencoders
- Encoder-decoder architecture (recap Section 06's encoder-decoder framing, now applied to reconstruction instead of translation)
- Bottleneck/latent representation — forcing the network to learn a compressed, informative encoding
- Reconstruction loss (MSE typically)
- Applications: dimensionality reduction (compare to `ML\12.2`'s PCA — an autoencoder is a non-linear generalization), denoising autoencoders, anomaly detection (recap `ML\13.4`'s mention — reconstruction error as an anomaly score)
- Why a plain autoencoder is **not** a good generative model (the latent space has no structure guaranteeing that sampling randomly produces valid outputs)

## 10.3 Variational Autoencoders (VAEs)
- The key fix: force the latent space to follow a known distribution (typically Gaussian) so you *can* sample from it meaningfully
- Encoder outputs a distribution (mean, variance) instead of a single point
- **The reparameterization trick**: how you can backpropagate through a sampling operation (a genuinely clever piece of engineering worth understanding deeply)
- Loss function: reconstruction loss + **KL divergence** term (recap `ML\01.4`'s introduction to KL divergence, now used as a training loss) — the KL term pulls the learned latent distribution toward the prior
- The latent space trade-off: reconstruction quality vs latent space regularity
- Sampling new data: draw from the prior, decode

## 10.4 Generative Adversarial Networks (GANs)
- **The adversarial framing**: two networks in competition — a **Generator** (tries to produce realistic fake samples from random noise) and a **Discriminator** (tries to distinguish real from fake)
- This is a direct, practical instance of the **game theory** covered in `AI\11` — specifically a minimax game between two players; the GAN objective literally is a minimax objective
- Training dynamics: alternating updates to generator and discriminator
- **Mode collapse**: the generator finds a small set of outputs that fool the discriminator and stops exploring the full data distribution — the most notorious GAN failure mode
- Training instability: why GANs are famously hard to train (vanishing gradients when the discriminator becomes too good, oscillation instead of convergence)
- Evaluation: Inception Score, Fréchet Inception Distance (FID) — since there's no simple likelihood to evaluate

## 10.5 GAN Variants & Improvements (awareness)
- DCGAN (convolutional architecture guidelines that made GAN training more stable)
- Conditional GANs (generating samples conditioned on a class label or other input)
- CycleGAN (unpaired image-to-image translation — awareness)
- Progressive growing, StyleGAN (awareness — the lineage that produced highly realistic face generation before diffusion models took over)
- Why diffusion models (Section 11) have largely superseded GANs for state-of-the-art image generation, while GANs remain useful for fast, specific tasks

## 10.6 VAEs vs GANs — Comparison
| | VAE | GAN |
|---|---|---|
| Training stability | Stable (single loss, gradient descent) | Unstable (adversarial, two competing losses) |
| Sample quality | Often blurrier | Often sharper, more realistic |
| Latent space | Structured, interpretable, good for interpolation | Less structured by default |
| Likelihood | Has an explicit (approximate) likelihood | No explicit likelihood |
| Mode coverage | Better (less prone to mode collapse) | Prone to mode collapse |

---

## Hands-on Exercises
1. Build a plain autoencoder on MNIST/Fashion-MNIST; visualize the 2D latent space and show that random sampling from it produces mostly garbage.
2. Build a VAE on the same data; visualize the latent space (now roughly Gaussian) and show that random sampling now produces plausible digits.
3. Implement the reparameterization trick from scratch and verify gradients flow correctly through the sampling step.
4. Build a basic DCGAN on MNIST/Fashion-MNIST; deliberately under-train the discriminator and observe mode collapse; then fix the training balance and observe improved diversity.

## Project — Generative Model Comparison
Train a VAE and a GAN on the same image dataset (Fashion-MNIST or CIFAR-10 subset). Compare: sample quality (visual + FID score), latent space interpolation smoothness (VAE), training stability (loss curves), and mode coverage (do generated samples cover all classes?). Write a report explaining, with your own results as evidence, why each approach has the specific trade-offs described in 10.6.

## Recommended Resources
- Kingma & Welling, "Auto-Encoding Variational Bayes" (2013) — the original VAE paper
- Goodfellow et al., "Generative Adversarial Networks" (2014) — the original GAN paper
- *Dive into Deep Learning* (d2l.ai) — generative model chapters
- Lilian Weng, "From Autoencoder to Beta-VAE" and "From GAN to WGAN" (blog posts — excellent, precise explanations)

## Definition of Done
- [ ] Your VAE's latent space visibly differs from the plain autoencoder's (more structured, samples are usable)
- [ ] You can explain the reparameterization trick well enough to implement it without notes
- [ ] You've observed mode collapse firsthand and can describe what caused it and how you fixed it
