# 09 — Domain and Multilingual Adaptation

> **Goal:** Apply everything from Sections 01–08 to the two adaptation problems you'll most often face in practice: making a model work well in a specialized domain, and making it work well in a language it wasn't primarily trained for.

**Level:** Applied · **Time:** 1–2 weeks · **Prerequisites:** Sections 01–06

---

## Learning Objectives
- Design a domain-adaptation strategy combining continued pretraining, SFT, and PEFT appropriately
- Evaluate and improve a model's performance in a specific low-resource or underrepresented language
- Recognize when adaptation should happen at the tokenizer level vs. the fine-tuning level
- Build a retrieval-aware fine-tuned model that complements rather than competes with RAG

---

## 9.1 The Domain Adaptation Decision Tree
- Recap Section 02.6's continued-pretraining content and Section 03.6's fine-tune-vs-prompt-vs-RAG framework — this section ties them together into one decision process
- Small vocabulary/style gap + enough labeled task data → SFT/PEFT is usually sufficient (Sections 03–04)
- Large vocabulary/style gap (e.g. legal, medical, low-resource-language text full of out-of-domain terms) → consider continued pretraining (Section 02.6) before task-specific fine-tuning
- Knowledge that changes frequently or needs source attribution → RAG (`AI_Agents\09-10`) instead of or alongside fine-tuning; fine-tuning teaches *behavior/style*, RAG supplies *current facts*

## 9.2 Domain-Specific Tokenizer and Vocabulary Adaptation
- Recap Section 01.3's tokenizer training — deciding when a domain needs its own tokenizer/vocabulary extension versus reusing the base model's tokenizer as-is
- Measuring domain token efficiency (recap Section 01's project) as the concrete signal for this decision
- Vocabulary extension: adding domain terms to an existing tokenizer and resizing/initializing the corresponding embedding rows

## 9.3 Multilingual and Low-Resource Language Adaptation
- Recap Section 01.4's tokenization-fairness content — the starting diagnostic for any multilingual adaptation project
- Why most open LLMs underperform outside a handful of high-resource languages: training data imbalance, tokenizer fragmentation compounding the problem
- Adaptation strategies: continued pretraining on target-language text, multilingual instruction-tuning datasets (including translated and natively-written data), and why natively-written data generally outperforms pure translation for naturalness
- Cross-lingual transfer: how instruction-following ability learned in one language partially transfers to others, and its limits

## 9.4 Evaluating Domain and Language Adaptation
- Recap Section 06's evaluation content, applied here: generic benchmarks (MMLU, etc.) often don't exist or don't transfer well for low-resource languages or specialized domains — building a custom eval set (Section 6.5) is usually mandatory, not optional, for this kind of project
- Native-speaker or domain-expert review as a necessary complement to automatic/LLM-judge evaluation when adapting to an underrepresented language or specialized domain
- Measuring regression on the model's original strong languages/domains, not just improvement on the target one (a domain/language-specific version of Section 03.4's catastrophic-forgetting check)

## 9.5 Combining Adaptation with RAG
- Fine-tuning a model to be a better *retrieval-aware* generator: trained to cite sources, handle retrieved-context-says-nothing-relevant gracefully, and resist being misled by irrelevant retrieved passages
- Recap `AI_Agents\10`'s advanced RAG content — this section is the model-training-side complement to that retrieval-engineering content
- Why "fine-tune vs. RAG" is usually a false choice in production systems: most serious deployments combine both

---

## Hands-on Exercises
1. Measure your target model's tokenizer efficiency and generation quality on a specific domain or low-resource language before doing any adaptation, establishing a baseline (recap Section 01's and 06's tooling).
2. Run continued pretraining on domain or target-language text, then SFT on top, and measure the improvement at each stage separately.
3. Build a native-speaker or domain-expert-reviewed eval set (even a small one) and compare its verdict against an LLM-as-judge verdict on the same outputs — note any disagreement.
4. Fine-tune a model to better handle retrieved context (citing sources, declining when context is irrelevant) and evaluate it inside a small RAG pipeline.

## Project — Domain or Low-Resource-Language Adaptation, End to End
Pick a specialized domain or an underrepresented language. Establish a baseline, then apply the appropriate combination of tokenizer adaptation, continued pretraining, SFT, and PEFT from earlier sections. Build a custom eval set with expert or native-speaker input, and measure both target-domain/language improvement and general-capability regression. If applicable, integrate your adapted model into a small RAG pipeline and evaluate the combination.

## Recommended Resources
- Gururangan et al., "Don't Stop Pretraining: Adapt Language Models to Domains and Tasks" (2020)
- Üstün et al., "Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model" (2024) — a concrete multilingual instruction-tuning case study
- Singh et al., "Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning" (2024)
- Papers/blog posts on retrieval-aware fine-tuning (e.g. RA-DIT, Self-RAG) for the Section 9.5 topic

## Definition of Done
- [ ] You can justify, for your chosen domain/language, exactly which adaptation techniques you used and why the alternatives were insufficient
- [ ] Your evaluation includes expert/native-speaker judgment, not just an automatic metric or an LLM judge
- [ ] You've measured regression on the model's original capabilities, not just improvement on the target domain/language
