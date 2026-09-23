# 06 — LLM Evaluation and Benchmarking

> **Goal:** Rigorously measure whether a pretraining run, fine-tune, or alignment step actually made a model better — and know the specific ways LLM evaluation can mislead you.

**Level:** Core · **Time:** 1–2 weeks · **Prerequisites:** Sections 03–05

---

## Learning Objectives
- Choose and run appropriate benchmarks for a given model capability claim
- Build a custom eval set for a specific fine-tuning task
- Use LLM-as-judge evaluation correctly, including its known biases
- Explain benchmark contamination and why public leaderboard numbers deserve skepticism

---

## 6.1 Why LLM Evaluation Is Hard
- Recap `AI_Agents\22`'s agent-evaluation content — this section is the model-level counterpart, one layer down
- Open-ended generation has no single correct answer, unlike classical ML's labeled test sets (recap `ML\11`'s evaluation content as the contrast case)
- The gap between benchmark performance and real-world usefulness for your specific task

## 6.2 Standard Benchmark Categories
- **Knowledge/reasoning**: MMLU, GPQA, ARC — broad academic-style knowledge and reasoning
- **Math and code**: GSM8K, MATH, HumanEval, MBPP
- **Instruction-following and chat quality**: MT-Bench, AlpacaEval, Chatbot Arena
- **Safety/alignment**: TruthfulQA, toxicity and bias benchmarks
- Reading a model card's benchmark table critically: what was actually measured, under what prompting conditions (zero-shot, few-shot, chain-of-thought)

## 6.3 Benchmark Contamination
- Recap Section 01.5's decontamination content from the data-pipeline side — this section covers detecting contamination from the eval side
- How benchmark data leaks into pretraining corpora (the benchmark's questions/answers appear verbatim or near-verbatim in web-scraped training data)
- Detecting contamination: n-gram overlap search between benchmark data and training corpus
- Why a suspiciously high benchmark score on a popular public benchmark should raise, not lower, your suspicion

## 6.4 LLM-as-Judge Evaluation
- Using a strong model to score or compare outputs when no automatic metric exists (recap Section 05.6's win-rate evaluation use case)
- Known biases: **position bias** (favoring whichever response is shown first/second), **verbosity bias** (favoring longer responses regardless of quality), self-preference bias (a model favoring outputs in its own style)
- Mitigations: randomizing response order, controlling for length, using multiple judge models, calibrating judge scores against a small human-labeled sample
- Pairwise comparison vs. absolute (Likert-scale) scoring, and why pairwise is generally more reliable

## 6.5 Building Custom Eval Sets
- Why generic benchmarks often don't measure what you actually care about for a fine-tuned, task-specific model
- Constructing a task-specific eval set: coverage of edge cases, difficulty stratification, held-out from any training/fine-tuning data
- Automatic metrics where applicable (exact match, F1, BLEU/ROUGE for specific structured tasks) vs. where LLM-as-judge or human eval is necessary
- Recap `AI_Agents\22`'s "write a 10–20 case eval set for every project" habit — this section is where that habit gets formalized for model-level work

## 6.6 Statistical Rigor in Model Comparison
- Why a small eval set's score difference between two models may not be statistically significant
- Confidence intervals / bootstrapping over eval results
- Running evals multiple times where sampling is stochastic (temperature > 0) and reporting variance, not a single number

---

## Hands-on Exercises
1. Run a standard benchmark subset (e.g. a slice of MMLU) on a base model and a fine-tuned/aligned version of it; report the delta with a confidence interval.
2. Search for benchmark contamination between a public benchmark and an open pretraining corpus using n-gram overlap; report the contamination rate found.
3. Build an LLM-as-judge pairwise evaluator; deliberately test it for position bias by swapping response order and checking for score consistency.
4. Build a 20-case custom eval set for a task-specific model from an earlier section's project, including at least 5 deliberately difficult edge cases.

## Project — Evaluation Suite for a Fine-Tuned Model
Take a model you fine-tuned or aligned in Sections 03–05. Build a complete evaluation suite: a relevant standard benchmark subset, a custom task-specific eval set with automatic metrics where possible, and an LLM-as-judge comparison against the base model with bias mitigations applied. Report results with confidence intervals and at least one honest finding of where your fine-tuned model is *worse* than the base model.

## Recommended Resources
- Hendrycks et al., "Measuring Massive Multitask Language Understanding" (MMLU, 2020)
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023) — the reference paper on LLM-judge biases
- EleutherAI `lm-evaluation-harness` — the standard open tool for running benchmark suites
- Hugging Face Open LLM Leaderboard methodology pages (read critically, per 6.3)

## Definition of Done
- [ ] You can name at least three specific ways an LLM benchmark score can be misleading
- [ ] You've built and run a custom eval set for at least one fine-tuned model, not just relied on a public benchmark
- [ ] Your LLM-as-judge setup has an explicit bias mitigation (order randomization at minimum) and you can explain why it's needed
