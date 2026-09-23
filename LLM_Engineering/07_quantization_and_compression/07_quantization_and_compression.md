# 07 — Quantization and Compression

> **Goal:** Shrink a trained LLM's memory and compute footprint for practical deployment, and understand the specific quantization techniques the LLM ecosystem has converged on beyond generic neural network compression.

**Level:** Production · **Time:** 2 weeks · **Prerequisites:** `Deep_Learning\16_model_optimization_and_efficiency`, Section 04

---

## Learning Objectives
- Explain post-training quantization techniques specific to LLMs (GPTQ, AWQ, GGUF) and how they differ from generic quantization
- Quantize a model and measure the accuracy/size/speed trade-off
- Explain KV-cache memory growth and cache-specific compression techniques
- Choose an appropriate quantization format and bit-width for a given deployment target

---

## 7.1 Recap and What's LLM-Specific
- Recap `Deep_Learning\16.2`'s generic quantization coverage (post-training quantization, quantization-aware training, INT8) — this section covers what's specific to billion-parameter Transformers
- Why LLMs are unusually quantization-friendly at the weight level but sensitive at the activation level, and why naive INT8 quantization of activations often fails on LLMs specifically (outlier features)

## 7.2 Weight-Only Post-Training Quantization
- **GPTQ**: layer-by-layer quantization that minimizes reconstruction error using second-order (Hessian-based) information, applied after training with a small calibration dataset
- **AWQ (Activation-aware Weight Quantization)**: identifying and preserving the small fraction of "salient" weight channels that matter most for accuracy, quantizing the rest aggressively
- Comparing GPTQ and AWQ on quantization speed, calibration data needs, and resulting accuracy
- 4-bit and lower: how far quantization can go before quality degrades unacceptably, and how this varies by model size (larger models tolerate lower bit-widths better)

## 7.3 GGUF and CPU/Edge-Oriented Quantization
- The GGUF format (successor to GGML) and its role in CPU and consumer-hardware inference (`llama.cpp` ecosystem)
- Mixed-precision quantization schemes within GGUF (different bit-widths for different tensor types)
- When GGUF/CPU inference is the right choice vs. GPU-oriented formats: local/offline deployment, consumer hardware, cost-sensitive low-throughput use cases

## 7.4 KV-Cache Memory and Compression
- Recap Section 02.2's GQA/MQA coverage as an architectural mitigation — this section covers *inference-time* KV-cache compression
- Why KV-cache memory grows linearly with sequence length and batch size, and why it (not model weights) is often the binding memory constraint for long-context serving
- KV-cache quantization (e.g. to 8-bit or 4-bit) and its accuracy trade-off
- KV-cache eviction/sparsification strategies for very long contexts (windowed attention, importance-based eviction)

## 7.5 Structured Compression: Pruning and Distillation for LLMs
- Recap `Deep_Learning\16.3-16.4`'s pruning and distillation coverage — applied here to LLM-scale models
- Structured pruning (removing whole attention heads, layers, or FFN blocks) vs. unstructured pruning, and why structured pruning is generally preferred for actual speedup on standard hardware
- Knowledge distillation from a large teacher LLM to a smaller student — recap `AI_Agents\25`'s mention of small models for cost optimization as the motivating use case
- Combining techniques: a distilled, then quantized, then LoRA-fine-tuned small model as a common production pattern

## 7.6 Measuring the Trade-off Honestly
- Benchmarking quantized models: perplexity delta, task-specific benchmark delta (recap Section 06), inference speed, memory footprint — always report all four together, never accuracy alone or speed alone
- Hardware-dependent results: a quantization format's speedup is not portable across GPU generations/vendors; always benchmark on your actual target hardware

---

## Hands-on Exercises
1. Quantize the same model with GPTQ and AWQ at 4-bit; compare perplexity degradation and quantization time between the two methods.
2. Convert a fine-tuned model to GGUF and run it with `llama.cpp` on CPU; measure tokens/second and compare against GPU full-precision inference.
3. Implement or use an existing KV-cache quantization option and measure the maximum context length that now fits in a fixed memory budget, before and after.
4. Distill a small student model from a larger fine-tuned teacher on a narrow task; compare student accuracy and inference speed against both the teacher and a same-size student trained from scratch without distillation.

## Project — Deployment-Ready Compressed Model
Take a fine-tuned model from an earlier section and produce a deployment-ready compressed version for a specific target (pick one: CPU/edge via GGUF, or GPU-served via GPTQ/AWQ). Report a full trade-off table: model size, perplexity/task-benchmark delta (using Section 06's eval suite), inference latency, and throughput, comparing full precision against at least two quantization bit-widths.

## Recommended Resources
- Frantar et al., "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers" (2022)
- Lin et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration" (2023)
- `llama.cpp` / GGUF documentation
- Hooper et al., "KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization" (2024)
- Hinton et al., "Distilling the Knowledge in a Neural Network" (2015) — foundational distillation paper, recap from `Deep_Learning\16.4`

## Definition of Done
- [ ] You can explain why activation quantization is harder than weight quantization for LLMs specifically
- [ ] You've quantized at least one model with two different methods and can compare them with real numbers
- [ ] Your project's trade-off table reports size, accuracy, and speed together, on hardware you actually measured
