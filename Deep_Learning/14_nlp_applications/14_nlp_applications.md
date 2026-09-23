# 14 — NLP Applications

> **Goal:** Apply the encoder (Section 08) and decoder (Section 09) architectures to the standard production NLP tasks: classification, generation, translation, and conversational systems — comparing deep learning approaches against the classical baselines from `ML\16` throughout.

**Level:** Applied · **Time:** 2–3 weeks · **Prerequisites:** 07, 08, 09

---

## Learning Objectives
- Apply the right architecture (encoder, decoder, or encoder-decoder) to each NLP task family
- Build production-grade text classification, generation, and translation systems
- Evaluate each task type with its correct metric
- Build a basic chatbot pipeline and understand where it connects to `AI_Agents\`

---

## 14.1 Text Classification — Deep Learning Approaches
- Recap the full progression now available to you: `ML\16` (TF-IDF + classical ML) → Section 06 (LSTM) → Section 08 (fine-tuned BERT) — you've now built all three
- When each is the right choice in production: latency/cost budget, data volume, accuracy requirements (recap `ML\16.8`'s framing, now with deep learning options included)
- Multi-label and hierarchical text classification (recap `ML\10.5`, applied with transformer encoders)

## 14.2 Natural Language Generation (NLG)
- Distinguishing NLG from classification/understanding: producing novel, coherent text as output
- Recap Section 09: decoder-only models as the core NLG engine
- Task framings: open-ended generation, constrained/controllable generation (conditioning on style, length, topic), data-to-text generation (structured data → natural language description)
- Evaluation challenges: why exact-match metrics don't work for generation
  - **BLEU**, **ROUGE** (recap link to Section 06's NMT project) — n-gram overlap metrics, their well-known limitations
  - **Perplexity** (recap Section 09.4) as a model-quality proxy, not a generation-quality metric
  - Human evaluation and LLM-as-judge approaches — direct link forward to `AI_Agents\22.3`'s full treatment of this exact problem

## 14.3 Machine Translation — Production Systems
- Recap Section 06's seq2seq+attention NMT project and Section 07's Transformer architecture — translation is the task that historically drove both
- Modern neural MT: Transformer encoder-decoder (recap Section 07.6), multilingual models (one model handling many language pairs)
- Practical evaluation: BLEU score standards, and its limitations for morphologically rich languages (relevant given your background — Indic languages in particular)
- Low-resource translation challenges: transfer learning from high-resource language pairs, back-translation (a data augmentation technique for MT specifically)

## 14.4 Summarization
- **Extractive summarization**: selecting existing sentences/phrases from the source (can be framed as a classification task per sentence — recap Section 08's token/sentence classification)
- **Abstractive summarization**: generating novel summary text (a decoder or encoder-decoder generation task — recap Sections 06/09)
- Evaluation with ROUGE, and its known weaknesses for abstractive summaries

## 14.5 Conversational AI / Chatbots — The Pre-LLM-Agent Approach
- **Retrieval-based chatbots**: matching user input to a database of canned responses (a classification/similarity task — recap Section 08.5's sentence embeddings)
- **Generative chatbots**: seq2seq or decoder-only generation conditioned on conversation history (recap Sections 06 and 09)
- Task-oriented dialogue systems: intent classification (recap `ML\06`'s customer request classifier example) + slot filling (a token classification task, recap Section 08.4's NER treatment) + dialogue state tracking + response generation — the classical pipeline architecture for chatbots before end-to-end LLM agents
- **Why this is the direct historical predecessor to `AI_Agents\`**: everything here (intent classification, retrieval, generation) still happens inside a modern LLM agent, just handled implicitly by one large decoder-only model (Section 09) instead of a pipeline of separate specialized models — building the classical pipeline once makes it much clearer what an LLM agent is actually doing under the hood

## 14.6 Named Entity Recognition & Information Extraction — Applied
- Recap Section 08.4's token classification treatment; this subsection focuses on production applications
- Extracting structured data from unstructured text: entities, relations, events
- Applications: resume parsing, invoice extraction (link forward to `AI_Agents\19.2`'s document intelligence, which covers the vision-model-based version of this same problem)

## 14.7 Where This Hands Off to AI_Agents
- Everything in this section (classification, generation, translation, dialogue, extraction) is now handled, in practice, by prompting a single large decoder-only model (Section 09) rather than training separate task-specific models
- `AI_Agents\05_prompt_engineering` and `AI_Agents\06_structured_outputs` cover exactly how to get the same outputs (classification labels, structured extraction) from an LLM via prompting instead of fine-tuning
- Understanding the "old way" (this section) makes it clear exactly what capability an LLM is substituting for, and why fine-tuning (Section 09.5) is still sometimes the better choice for a narrow, high-volume task

---

## Hands-on Exercises
1. Build a text summarizer two ways: extractive (sentence scoring + selection) and abstractive (fine-tuned encoder-decoder generation); compare ROUGE scores and read the outputs yourself to judge quality beyond the metric.
2. Build a simple task-oriented dialogue pipeline: intent classifier + slot-filling NER + templated response generation, for a narrow domain (e.g. restaurant reservations).
3. Fine-tune a small encoder-decoder model (recap Section 07.6) for translation on a small parallel corpus; report BLEU and compare against your Section 06 LSTM-based NMT project on the same data.
4. Build a retrieval-based chatbot using sentence embeddings (recap Section 08.5) over a small FAQ dataset; compare its behavior to what an LLM would produce for the same queries.

## Project — Task-Oriented Dialogue System (Pre-LLM Architecture)
Build a complete classical pipeline chatbot for a narrow domain of your choice (e.g. a pizza-ordering bot, a simple booking assistant): intent classification (Section 08's fine-tuned encoder), slot filling / entity extraction (Section 08's token classification), a simple dialogue state tracker, and templated or lightly generative response construction. Then, write a comparison document: reimplement the same domain's behavior with a single prompted LLM (using techniques from `AI_Agents\05`–`06`) and compare accuracy, development time, flexibility, and latency/cost between the two approaches.

## Recommended Resources
- *Speech and Language Processing* (Jurafsky & Martin) — chapters on dialogue systems, MT, and summarization (free draft online)
- Lin, "ROUGE: A Package for Automatic Evaluation of Summaries" (2004)
- Hugging Face `transformers` course — summarization, translation, and token classification chapters
- Papers with Code — NLP task leaderboards (useful for seeing current state-of-the-art per task)

## Definition of Done
- [ ] Your dialogue pipeline correctly handles at least 10 varied conversation flows in its narrow domain
- [ ] Your classical-pipeline vs single-LLM comparison has real numbers (accuracy, latency, cost, dev time), not just impressions
- [ ] You can explain, concretely, which classical NLP component (intent classification, slot filling, generation) an LLM agent is implicitly performing at each step of a conversation
