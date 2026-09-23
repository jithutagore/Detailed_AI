# 08 — Inference Serving and Optimization

> **Goal:** Take a trained (and optionally quantized) model and serve it efficiently to real traffic — the engineering layer that sits directly beneath every LLM API you've consumed in `AI_Agents\`.

**Level:** Production · **Time:** 2 weeks · **Prerequisites:** Section 07, `AI_Agents\04_llm_apis_and_providers`

---

## Learning Objectives
- Explain autoregressive decoding's core inference bottleneck and the techniques built to address it
- Deploy a model with a production-grade serving engine (vLLM or equivalent)
- Apply batching, caching, and speculative decoding to improve throughput and latency
- Reason about latency/throughput trade-offs and choose serving configuration for a given workload

---

## 8.1 Why LLM Inference Is Different
- Autoregressive decoding: each output token requires a full forward pass conditioned on all previous tokens, making generation inherently sequential and memory-bandwidth-bound rather than compute-bound
- The prefill/decode split: prefill (processing the prompt) is compute-bound and parallelizable; decode (generating tokens one at a time) is memory-bandwidth-bound — this distinction motivates most of this section's techniques
- Recap `AI_Agents\04`'s streaming coverage from the consumer side — this section covers what makes streaming possible/efficient on the server side

## 8.2 The KV Cache
- Recap Section 07.4's KV-cache memory/compression content — this section covers the KV cache's role in serving *speed*
- Why caching past keys/values avoids recomputing the entire sequence at every decoding step
- KV-cache memory as the primary constraint on batch size and context length in production serving

## 8.3 Continuous Batching
- The naive approach (static batching: wait for a full batch, run it together, return only when all sequences finish) and why it wastes GPU time on requests that finish early
- **Continuous (in-flight) batching**: dynamically adding new requests and evicting finished ones at each decoding step, keeping the GPU saturated
- Why this single technique is responsible for most of the throughput gains in modern serving engines (vLLM, TGI) over naive implementations

## 8.4 PagedAttention and Memory Management
- The KV-cache memory fragmentation problem with naive contiguous allocation
- **PagedAttention**: managing the KV cache in fixed-size blocks (like OS virtual memory paging), enabling near-zero memory waste and efficient memory sharing
- Prefix caching: sharing KV-cache blocks across requests with a common prompt prefix (e.g. a shared system prompt) — direct link to `AI_Agents\04`'s prompt-caching coverage from the API-consumer side

## 8.5 Speculative Decoding
- The core idea: use a small, fast "draft" model to propose several tokens ahead, then verify them in a single forward pass of the large target model, accepting the ones that match what the large model would have generated
- Why this speeds up generation despite doing extra compute: verification is parallelizable even though generation isn't
- Variants: a separate small draft model vs. self-speculation techniques (e.g. Medusa-style extra prediction heads) that don't require a second model

## 8.6 Serving Engines in Practice
- **vLLM**: the reference open-source implementation of continuous batching + PagedAttention; deploying a model with it
- **Text Generation Inference (TGI)**, **TensorRT-LLM**, and **SGLang** as alternatives, and their relative strengths (ecosystem, hardware vendor optimization, structured-generation support)
- Multi-LoRA serving: serving many task-specific adapters (recap Section 04.5) against one shared base model efficiently, without loading a full model copy per adapter
- Structured output / constrained decoding at the serving layer (recap `AI_Agents\06`'s structured-outputs content from the consumer side — this is how it's implemented underneath)

## 8.7 Latency, Throughput, and Cost Trade-offs
- Time-to-first-token (TTFT) vs. inter-token latency vs. total throughput (tokens/second across all concurrent requests) as distinct metrics that trade off against each other
- Batch size and concurrency tuning for a target SLA
- Recap `AI_Agents\25`'s cost-optimization content — this section is where the underlying serving-cost numbers actually come from (GPU-hours per million tokens, the effect of quantization and batching on that number)

---

## Hands-on Exercises
1. Deploy a model with vLLM (or an equivalent serving engine) and benchmark throughput/latency against a naive Hugging Face `generate()` loop on the same hardware.
2. Measure the throughput improvement from continuous batching by comparing static-batch vs. continuous-batch serving under a simulated stream of requests with varying arrival times.
3. Implement or configure speculative decoding with a draft model and measure the speedup and the token acceptance rate.
4. Serve multiple LoRA adapters against a shared base model simultaneously and measure the memory savings versus loading separate full model copies.

## Project — Production Serving Benchmark
Deploy a fine-tuned (and optionally quantized, from Section 07) model with a production serving engine. Build a load-testing harness that simulates realistic concurrent traffic. Report TTFT, inter-token latency, and total throughput across a range of concurrency levels, and identify the concurrency point where latency SLAs start to degrade. Compare at least two configurations (e.g. with/without prefix caching, or with/without speculative decoding).

## Recommended Resources
- Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (vLLM paper, 2023)
- Leviathan et al., "Fast Inference from Transformers via Speculative Decoding" (2022)
- vLLM, TGI, and SGLang official documentation
- Pope et al., "Efficiently Scaling Transformer Inference" (2022) — Google's inference-serving systems paper

## Definition of Done
- [ ] You can explain the prefill/decode distinction and why it shapes every technique in this section
- [ ] You've deployed a model with a real serving engine and produced actual latency/throughput numbers, not estimates
- [ ] You can explain PagedAttention and continuous batching well enough to justify why they replaced naive serving approaches
