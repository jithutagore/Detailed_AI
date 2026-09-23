# 17 — Training at Scale

> **Goal:** Understand how training moves from a single GPU to many — the engineering that makes training large models (including LLMs) possible. This is systems knowledge, not new modeling theory, but it's essential for understanding what happens beneath `AI_Agents\` when a model is described as "trained on thousands of GPUs."

**Level:** Production · **Time:** 1–2 weeks · **Prerequisites:** 01, 03, 09

---

## Learning Objectives
- Explain the major parallelism strategies for distributed training
- Use mixed-precision training and understand memory-saving techniques
- Reason about compute/memory/communication trade-offs at scale
- Know what "training an LLM from scratch" actually requires, even if you'll rarely do it yourself

---

## 17.1 Why Scale Requires New Engineering
- Recap Section 09.3's scaling laws: bigger models/data/compute generally means better performance, up to a compute budget
- The practical wall: a large model (or dataset) doesn't fit in one GPU's memory, and training on one GPU is too slow regardless
- This section is about the engineering that makes "just add more compute" actually work

## 17.2 Mixed Precision Training
- Recap Section 01.3's mention and Section 16.2's quantization (inference-time) — this section covers precision reduction **during training**, a different problem
- FP16/BF16 training: faster computation, less memory, at the risk of numerical instability
- **Loss scaling**: a technique to prevent small gradient values from underflowing to zero in FP16
- Why BF16 (same exponent range as FP32, less precision) is often preferred over FP16 for training stability
- Automatic Mixed Precision (AMP) tooling in PyTorch

## 17.3 Data Parallelism
- The simplest scaling strategy: replicate the full model on each GPU, split the data batch across GPUs, average gradients after each step
- `DistributedDataParallel` (DDP) in PyTorch
- Gradient synchronization overhead, and why this strategy alone doesn't help once the *model itself* doesn't fit on one GPU

## 17.4 Model Parallelism
- **Tensor parallelism**: splitting individual layers' computations (e.g. a large matrix multiply) across multiple GPUs
- **Pipeline parallelism**: splitting the model's layers across GPUs, with different GPUs handling different stages of the forward/backward pass — introduces the "pipeline bubble" idle-time problem, and micro-batching as its mitigation
- When model parallelism becomes necessary: the model's parameters alone exceed a single GPU's memory (common for large Transformers, recap Section 09)

## 17.5 Combining Strategies
- **3D parallelism**: combining data + tensor + pipeline parallelism together — how modern large-model training actually works in practice
- **ZeRO (Zero Redundancy Optimizer)** / DeepSpeed and FSDP (Fully Sharded Data Parallel): sharding optimizer states, gradients, and even parameters across GPUs to eliminate memory redundancy from naive data parallelism
- Why these techniques matter even for you: fine-tuning a mid-sized model (Section 09.5's LoRA territory) on limited hardware often uses simplified versions of these same ideas

## 17.6 Memory-Saving Techniques
- **Gradient checkpointing / activation recomputation**: trading extra compute for reduced memory by not storing all intermediate activations, recomputing them during the backward pass instead
- **Gradient accumulation**: simulating a larger batch size than fits in memory by accumulating gradients over several forward/backward passes before updating weights
- Optimizer memory: why Adam (recap Section 3.2) uses significantly more memory than SGD (it stores two extra moment estimates per parameter) — directly relevant to why memory-efficient optimizer variants exist

## 17.7 Data Pipeline at Scale
- Why data loading can become the bottleneck even with enough compute: efficient data loading, prefetching, sharding datasets across workers
- Streaming datasets (for data too large to fit on disk/in memory at once)
- Deduplication and data quality at scale (recap `AI_Agents\09.2`'s cleaning concepts, applied to pretraining-scale corpora)

## 17.8 Practical Reality for Most Practitioners
- Full from-scratch large-model pretraining is done by a small number of well-resourced labs — most practitioners fine-tune existing models (recap Section 09.5) instead
- What you're likely to actually use from this section: mixed precision (nearly always), gradient accumulation/checkpointing (often, on limited hardware), basic DDP (for any multi-GPU fine-tuning job)
- Why understanding the full picture still matters: it explains cost, capability differences between organizations, and design decisions you'll see referenced throughout `AI_Agents\` (e.g. why training your own frontier-scale model isn't a realistic option, motivating the fine-tuning/RAG/prompting alternatives covered there)

---

## Hands-on Exercises
1. Train a model from an earlier section with and without mixed precision (AMP); compare training speed and peak memory usage.
2. Implement gradient accumulation to simulate a batch size larger than your GPU can hold in one pass; verify the resulting gradients approximate the large-batch result.
3. Implement gradient checkpointing on a deep network (Section 02's deep MLP or Section 04/05's CNN) and measure the memory savings and the compute-time cost.
4. If multi-GPU hardware is available (including free-tier multi-GPU cloud notebooks), run the same training job with `DistributedDataParallel` across 2 GPUs and compare wall-clock time to single-GPU training.

## Project — Efficient Fine-Tuning Under a Memory Budget
Take a mid-sized pretrained model (larger than comfortably fits your available GPU memory with standard full fine-tuning) and fine-tune it successfully using a combination of techniques from this section and Section 09.5: mixed precision, gradient accumulation, gradient checkpointing, and LoRA. Document the memory budget before and after each technique is added, and the final training throughput and result quality.

## Recommended Resources
- Hugging Face, "Efficient Training on a Single GPU" and "Model Parallelism" documentation guides (practical, current)
- Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models" (2019)
- PyTorch documentation: Automatic Mixed Precision, `DistributedDataParallel`, Fully Sharded Data Parallel (FSDP)
- Weng, "How to Train Really Large Models on Many GPUs?" (Lilian Weng's blog — an excellent systems-level overview)

## Definition of Done
- [ ] You can explain the difference between data, tensor, and pipeline parallelism and when each is needed
- [ ] Your memory-budget fine-tuning project succeeds on hardware that couldn't run naive full fine-tuning
- [ ] You can explain, concretely, why most practitioners fine-tune rather than pretrain from scratch
