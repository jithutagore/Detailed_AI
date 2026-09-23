# 16 — Model Optimization & Efficiency

> **Goal:** Make trained models fast, small, and cheap enough to actually deploy — on servers at scale, or on edge/mobile devices. A model that only works in a research notebook isn't finished.

**Level:** Production · **Time:** 2 weeks · **Prerequisites:** 03; at least one of Sections 04–09 (something trained to optimize)

---

## Learning Objectives
- Reduce model size and inference cost without unacceptable accuracy loss
- Apply quantization, pruning, and distillation
- Choose the right optimization technique for a given deployment constraint
- Benchmark models correctly (not just accuracy — latency, memory, throughput)

---

## 16.1 Why Optimization Matters
- The gap between a research model (large, trained on a powerful GPU cluster) and a deployable model (latency budget, memory budget, cost budget)
- Recap `AI_Agents\25`'s cost optimization framing — this section is the model-level counterpart to that application-level content
- Metrics that matter beyond accuracy: inference latency (P50/P95), throughput (requests/sec), memory footprint, model file size, energy consumption (mobile/edge)

## 16.2 Quantization
- Reducing numeric precision: FP32 → FP16/BF16 → INT8 → lower (INT4 and below)
- **Post-training quantization**: converting an already-trained model, fast but can lose accuracy
- **Quantization-aware training (QAT)**: simulating quantization effects during training so the model adapts, better accuracy retention
- Why lower precision works: neural networks are generally robust to some numeric imprecision (redundancy in learned representations)
- Recap `AI_Agents\04.3`'s mention of GGUF/AWQ quantization for LLMs — same underlying technique, applied to any architecture in this folder (CNNs, encoders, decoders)

## 16.3 Pruning
- **Unstructured pruning**: zeroing out individual low-magnitude weights — high compression, but requires specialized sparse-computation hardware/libraries to actually speed things up
- **Structured pruning**: removing entire channels, filters, or attention heads — directly reduces computation on standard hardware, at the cost of being less fine-grained
- Magnitude-based pruning, iterative pruning + fine-tuning cycles
- The Lottery Ticket Hypothesis (awareness — the finding that small, well-chosen subnetworks can match full-network performance)

## 16.4 Knowledge Distillation
- Recap Section 08.3's mention (DistilBERT) — this section gives the full technique
- **Teacher-student framework**: a large, accurate "teacher" model trains a smaller "student" model, using the teacher's soft output probabilities (not just hard labels) as a richer training signal
- Why soft labels help: they encode the teacher's learned notion of *similarity* between classes, not just the correct answer
- Temperature scaling in distillation (softening the teacher's probability distribution)
- Recap `AI_Agents\25.5`'s distillation discussion — same technique, now with the full mechanism understood

## 16.5 Efficient Architecture Design
- Recap Section 05.1's MobileNet/EfficientNet mention — designing for efficiency from the start, rather than compressing after training
- Depthwise separable convolutions (the core MobileNet trick — factorizing a standard convolution into cheaper steps)
- Neural Architecture Search (NAS) — awareness (automatically searching for efficient architectures)
- Efficient attention variants for Transformers (recap Section 07 — sparse attention, linear attention approximations) — awareness, relevant to why long-context LLMs need architectural tricks beyond naive full attention

## 16.6 Inference Optimization
- Graph optimization and operator fusion (combining multiple operations into one kernel)
- **ONNX** (recap `ML\20.6`) as a framework-independent deployment format, enabling optimized runtimes
- Hardware-specific compilation: TensorRT (NVIDIA GPUs), Core ML (Apple), TFLite (mobile/edge)
- Batching strategies for throughput (recap `AI_Agents\04.5`'s batch API discussion, at the infrastructure level here)
- KV cache optimization for Transformers (recap Section 09.6) — paged attention and similar serving-level techniques (awareness)

## 16.7 Benchmarking Correctly
- Measuring latency: cold start vs warm, P50 vs P95/P99 (recap `ML\11`'s statistical rigor applied to systems metrics)
- Measuring on the actual target hardware, not just a development machine
- Accuracy-efficiency trade-off curves (Pareto frontier — recap `AI_Agents\25.4`'s model-selection method, applied here to optimization technique selection)

---

## Hands-on Exercises
1. Quantize a trained CNN (Section 04/05) to INT8 with post-training quantization; measure the accuracy drop and the inference speedup.
2. Apply structured pruning (remove a percentage of filters per layer) to a trained CNN; fine-tune afterward and compare the accuracy-recovery curve against the unpruned baseline.
3. Distill a fine-tuned BERT model (Section 08) into a much smaller architecture (e.g. a small BiLSTM or a 2-layer Transformer); compare accuracy, size, and inference latency of teacher vs student.
4. Export a trained model to ONNX and benchmark inference latency against the native PyTorch model.

## Project — Edge-Deployable Model
Take a model from an earlier section (an image classifier from Section 04/05, or a small NLP classifier from Section 08) and optimize it for edge/mobile deployment: apply quantization, pruning, or distillation (or a combination), export to a deployment-ready format (ONNX/TFLite), and produce a full trade-off report: original vs optimized model's accuracy, size, and latency on a size/speed-constrained target (simulate this even without physical edge hardware, using model size and FLOP count as proxies).

## Recommended Resources
- Han et al., "Deep Compression" (2015) — pruning + quantization + Huffman coding, an influential early compression paper
- Hinton et al., "Distilling the Knowledge in a Neural Network" (2015) — the original distillation paper
- Frankle & Carbin, "The Lottery Ticket Hypothesis" (2019)
- PyTorch official quantization and pruning tutorials
- ONNX Runtime documentation

## Definition of Done
- [ ] Your optimized model's accuracy-vs-efficiency trade-off is documented with real numbers, not estimates
- [ ] You can recommend the right optimization technique (quantization vs pruning vs distillation) for a stated deployment constraint, with reasoning
