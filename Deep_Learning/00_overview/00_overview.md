# Deep Learning — Syllabus Overview

This folder is the index for the **Deep Learning** curriculum: neural networks from the ground up through CNNs, RNNs/LSTMs, Transformers, BERT/GPT, Diffusion Models, and their computer vision and NLP applications.

**Scope:** the full deep learning stack that sits between classical Machine Learning and LLM Engineering / Gen AI Agent engineering.
**Not in scope here:** classical (non-neural) ML — see `ML\`; training/fine-tuning/serving LLMs specifically — see `LLM_Engineering\`; LLM agent engineering (tools, RAG orchestration, multi-agent, MCP) — see `AI_Agents\`.

---

## Why This Folder Exists

`ML\18_neural_network_basics` introduces the MLP as a bridge, and `AI_Agents\03_llm_foundations` covers Transformer *theory* for LLMs — but nothing in either folder teaches CNNs, RNN architectures, or Transformers/BERT/GPT **as a hands-on, buildable curriculum**, and Diffusion Models weren't covered anywhere. This folder is that missing middle layer:

```
Data Engineering → ML (classical) → DEEP LEARNING (this folder) → LLM Engineering → AI Agents
                                            ↓
                    ANN/MLP → CNN → RNN/LSTM/GRU → Transformers → BERT/GPT → Diffusion
                                            ↓
                              CV Applications · NLP Applications
```

## Relationship to Your Other Folders
| Topic | Where it lives |
|---|---|
| Classical ML algorithms (regression, trees, boosting) | `ML\` |
| MLP basics, backprop from scratch (bridge-level) | `ML\18_neural_network_basics` (this folder goes much deeper) |
| Classical RL (Q-learning, bandits) | `ML\19_reinforcement_learning_basics` |
| Deep RL (policy gradients, PPO/GRPO on LLMs) | `AI_Agents\34_agent_environments_and_agentic_rl` (builds on this folder's Section 12) |
| Training/fine-tuning/aligning/serving LLMs (SFT, LoRA, RLHF/DPO, quantization, vLLM-style serving) | `LLM_Engineering\` (assumes you understand Sections 07 and 09 here) |
| LLM application engineering (prompting, tools, RAG, agents) | `AI_Agents\` (assumes you understand Sections 07–08 here, and typically `LLM_Engineering\`) |
| Voice agents (STT/TTS integration) | `AI_Agents\28_voice_agents` (builds on this folder's Section 11) |

---

## Section Map

| # | Folder | Level | Suggested time |
|---|---|---|---|
| 01 | `01_deep_learning_foundations` | Foundation | 1 week |
| 02 | `02_artificial_neural_networks` | Foundation | 2 weeks |
| 03 | `03_training_deep_networks` | Foundation | 2 weeks |
| 04 | `04_convolutional_neural_networks` | Core | 3 weeks |
| 05 | `05_cnn_architectures_and_transfer_learning` | Core | 2 weeks |
| 06 | `06_recurrent_neural_networks` | Core | 2–3 weeks |
| 07 | `07_attention_and_transformers` | Core | 3 weeks |
| 08 | `08_bert_and_encoder_models` | Core | 1–2 weeks |
| 09 | `09_gpt_and_decoder_models` | Core | 1–2 weeks |
| 10 | `10_generative_models_gans_vaes` | Applied | 2 weeks |
| 11 | `11_diffusion_models` | Applied | 2 weeks |
| 12 | `12_deep_reinforcement_learning` | Applied | 2 weeks |
| 13 | `13_computer_vision_applications` | Applied | 2–3 weeks |
| 14 | `14_nlp_applications` | Applied | 2–3 weeks |
| 15 | `15_speech_and_audio_deep_learning` | Applied | 2 weeks |
| 16 | `16_model_optimization_and_efficiency` | Production | 2 weeks |
| 17 | `17_training_at_scale` | Production | 1–2 weeks |
| 18 | `18_capstone_projects` | Portfolio | 4–6 weeks |

**Total:** about 9–11 months part-time (10–15 hrs/week), or 5–6 months full-time.

---

## Learning Path

```
DL Foundations → Artificial Neural Networks (ANN/MLP) → Training Deep Networks
   ↓
Convolutional Neural Networks → CNN Architectures & Transfer Learning
   ↓
Recurrent Neural Networks (RNN → LSTM → GRU)
   ↓
Attention & Transformers → BERT (encoder) → GPT (decoder)
   ↓
Generative Models (GANs/VAEs) → Diffusion Models
   ↓
Deep Reinforcement Learning
   ↓
Applications: Computer Vision · NLP · Speech/Audio
   ↓
Model Optimization & Efficiency → Training at Scale → Capstones
   ↓
                                                    forward into LLM_Engineering\ (then AI_Agents\03_llm_foundations)
```

### Core track (if time is short)
01 → 02 → 03 → 04 → 06 → 07 → 08 → 09 → 13 → 14 → 18.
Sections 10–12 and 15–17 are valuable specializations — pick based on your goals (generative art/vision needs 10–11; voice/speech given your background needs 15; production ML engineering needs 16–17).

### Why Sections 06–09 matter most for your path
Given your speech/voice background and the `AI_Agents` syllabus already assuming Transformer knowledge, **Sections 06 (RNN/LSTM) → 07 (Attention/Transformers) → 08–09 (BERT/GPT)** form the single most important arc in this folder. This is the direct, hands-on path from "sequence has memory problems" to "attention solves them" to "here's GPT." Do not skip this arc even if you skim other sections.

---

## Habits to Keep Throughout
- **Always implement the core mechanism from scratch once** (backprop, a conv layer, self-attention) before relying on a framework — this is where real understanding comes from.
- **Track experiments** (Weights & Biases or TensorBoard) from Section 03 onward.
- **Use pretrained models and fine-tuning** wherever practical — training from scratch is for learning, not for every project.
- **Publish each project on GitHub** with a README, training curves, and sample outputs.

---

## Guiding Principle

> Every architecture in this folder exists because the previous one had a specific, nameable limitation. MLPs can't handle spatial structure → CNNs. Feedforward nets can't handle sequences → RNNs. RNNs forget over long distances and can't parallelize → Transformers. Learn each architecture by learning the exact problem it was invented to solve, not just its equations.
