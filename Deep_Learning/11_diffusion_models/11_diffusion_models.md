# 11 — Diffusion Models

> **Goal:** Understand and implement diffusion models — the generative approach behind current state-of-the-art image, audio and video generation (Stable Diffusion, DALL-E, Midjourney-class systems). This was entirely missing from the syllabus before; it's a core pillar of modern Generative AI alongside LLMs.

**Level:** Applied · **Time:** 2 weeks · **Prerequisites:** 10 (essential — diffusion is best understood in contrast to GANs/VAEs)

---

## Learning Objectives
- Explain the forward (noising) and reverse (denoising) diffusion process
- Implement a basic denoising diffusion model from scratch
- Understand how text conditioning enables text-to-image generation
- Know the modern diffusion landscape (Stable Diffusion, DALL-E, and the efficiency techniques that made them practical)

---

## 11.1 The Core Idea
- Recap Section 10.6: VAEs are stable but blurrier; GANs are sharp but unstable and prone to mode collapse
- Diffusion models' pitch: get GAN-level (or better) sample quality with VAE-level (or better) training stability, by reframing generation as a **gradual denoising process**
- The two processes:
  - **Forward process (fixed, not learned)**: gradually add Gaussian noise to a real image over many steps until it becomes pure noise
  - **Reverse process (learned)**: train a neural network to reverse this — predict and remove a small amount of noise, one step at a time, starting from pure noise and ending at a realistic image

## 11.2 Forward Diffusion Process
- Markov chain of noise-adding steps (why this connects back to `AI\06`'s Markov chain / HMM concepts — the same mathematical object, applied differently)
- The noise schedule (how much noise is added at each step)
- The closed-form shortcut: you can jump directly to any noise level at any timestep without simulating every intermediate step (a key practical/mathematical convenience)

## 11.3 Reverse Diffusion Process — Learning to Denoise
- Training objective: at a random timestep, given a noisy image, predict the noise that was added (not the clean image directly — this reparameterization, from the DDPM paper, trains much better in practice)
- The network architecture: **U-Net** — a CNN architecture with downsampling then upsampling paths and skip connections between matching resolutions (recap Section 04's convolutions and Section 05's residual connections — a U-Net is built from exactly these pieces)
- Why U-Net: it needs to output something the same spatial size as the input (the predicted noise), while still building up hierarchical features
- Sampling: starting from pure noise, iteratively applying the trained denoiser for many steps to produce a final image

## 11.4 Speeding Up Sampling
- The original DDPM approach requires hundreds to thousands of denoising steps — extremely slow
- **DDIM** and other fast samplers: reformulating the sampling process to skip steps while maintaining quality — how modern tools generate images in a handful of steps instead of a thousand
- This efficiency work is what made diffusion models practical for interactive, production use

## 11.5 Conditioning — From Unconditional to Text-to-Image
- Unconditional generation (just sampling from the learned distribution) vs **conditional generation** (steering generation toward a desired output)
- Class-conditional diffusion (condition on a label)
- **Text-to-image**: conditioning the denoising U-Net on a text embedding
  - Where the text embedding comes from: a pretrained text encoder (recap Section 08's BERT-family encoders, or CLIP's text encoder specifically)
  - **CLIP** (Contrastive Language-Image Pretraining): jointly training an image encoder and text encoder so matching image-text pairs have similar embeddings — this is what lets diffusion models understand a text prompt well enough to condition image generation on it, and it's also the technology behind text-based image search/retrieval
  - **Classifier-free guidance**: a technique for strengthening how closely generation follows the conditioning signal (the practical mechanism behind the "guidance scale" / "CFG scale" slider in image generation tools)

## 11.6 Latent Diffusion (Stable Diffusion's Key Innovation)
- The efficiency problem: running the full diffusion process directly on high-resolution pixel space is extremely expensive
- **Latent diffusion**: first compress the image into a smaller latent representation using a pretrained autoencoder (recap Section 10.2–10.3 — literally the VAE/autoencoder machinery from the previous section, reused here), then run the diffusion process in that compact latent space, then decode back to pixels at the end
- Why this is the specific architectural choice that made Stable Diffusion dramatically more efficient than pixel-space diffusion, and thus practical to run on consumer hardware

## 11.7 The Modern Diffusion Landscape (awareness)
- Stable Diffusion (open-weight, latent diffusion + CLIP conditioning + U-Net)
- DALL-E series (awareness of the architecture differences across versions)
- Imagen, Midjourney (awareness — proprietary, architecture details vary)
- Diffusion beyond images: audio generation, video generation (temporal extension, awareness), and diffusion-based approaches emerging in other domains
- Diffusion Transformers (DiT): replacing the U-Net backbone with a Transformer (recap Section 07) — the current direction for scaling diffusion models further

## 11.8 Practical Use
- Using pretrained diffusion pipelines (Hugging Face `diffusers` library): text-to-image, image-to-image, inpainting
- Fine-tuning approaches: full fine-tuning, DreamBooth (personalization with few images), LoRA for diffusion models (recap Section 09.5's LoRA concept, applied here to a different architecture)
- Prompt engineering for image generation (a distinct skill from `AI_Agents\05`'s text-prompting techniques, but built on the same underlying idea of steering a generative model through its input)

---

## Hands-on Exercises
1. Implement the forward diffusion (noising) process from scratch and visualize an image at several noise levels.
2. Implement a small U-Net and train a basic unconditional DDPM on MNIST/Fashion-MNIST; generate samples by running the full reverse process.
3. Implement DDIM sampling on your trained model and compare sample quality/speed against full DDPM sampling.
4. Use a pretrained Stable Diffusion pipeline (`diffusers`) to generate images from text prompts; experiment with classifier-free guidance scale and observe its effect.

## Project — Conditional Diffusion Model
Extend your Section 11.2–11.3 unconditional diffusion model to be class-conditional (e.g. on Fashion-MNIST's 10 classes): condition the U-Net on the class label, implement classifier-free guidance, and demonstrate controllable generation (specifying a class produces samples from that class). Compare generation quality and diversity against your Section 10 VAE and GAN on the same dataset — complete the three-way comparison across all of this folder's generative modeling approaches.

## Recommended Resources
- Ho et al., "Denoising Diffusion Probabilistic Models" (DDPM, 2020) — the paper that reignited diffusion models
- Song et al., "Denoising Diffusion Implicit Models" (DDIM, 2020)
- Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models" (the Stable Diffusion paper, 2022)
- Radford et al., "Learning Transferable Visual Models From Natural Language Supervision" (CLIP, 2021)
- Lilian Weng, "What are Diffusion Models?" (the best single blog-post explanation)
- Hugging Face `diffusers` library documentation and course

## Definition of Done
- [ ] Your from-scratch DDPM generates recognizable samples after training
- [ ] You can explain, concretely, what latent diffusion changes relative to pixel-space diffusion and why it matters for efficiency
- [ ] Your conditional generation project demonstrates controllable output (not just quality, but *steerable* quality)
- [ ] You've completed the three-way VAE/GAN/Diffusion comparison and can recommend each for a specific use case
