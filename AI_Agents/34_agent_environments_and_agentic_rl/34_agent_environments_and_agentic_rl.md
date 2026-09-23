# 34 — Agent Environments & Agentic RL  *(NEW section)*

> **Goal:** Understand how agents are *trained* to use tools: environments, verifiers, rewards and reinforcement learning. Then apply it to improve a small open model on your own agent task.
> **Why added:** Section 25 covers supervised fine-tuning only. RL in environments is how current models learn agentic behavior, and it's increasingly practical for teams that train small, cheap, specialized agent models.
> **When to study:** after 22 (Evaluation) and 25 (Cost / Fine-tuning). An eval harness and an RL environment are almost the same thing. This section is optional for application-focused engineers and important for anyone going toward ML/research engineering.

**Level:** Advanced / ML · **Time:** 2–3 weeks · **Prerequisites:** 03, 22, 25; basic PyTorch helps

---

## Learning Objectives
- Explain environments, rollouts, verifiers and rewards
- Turn an eval set into an RL environment
- Understand the main RL algorithms used for LLMs (PPO, GRPO) at a conceptual level
- Run a small RL fine-tuning job on an open model and measure the gain
- Recognize reward hacking and other failure modes

---

## 34.1 Why RL for Agents
- Supervised fine-tuning (SFT) imitates demonstrations; RL optimizes for **outcomes**
- Multi-step tasks have many valid paths, and RL rewards any path that succeeds
- Pre-training → SFT → RL (RLHF, RLAIF, **RLVR**: RL with verifiable rewards)
- How reasoning and tool-use skills in frontier models come largely from RL at scale
- When RL is worth it for you vs prompting, RAG or SFT (usually: narrow, high-volume task, clear success check, cost pressure to use a small model)

## 34.2 Core Concepts
| Term | Meaning for agents |
|---|---|
| **Environment** | The task + tools + state the agent interacts with (a repo, a DB, a browser, a simulated customer) |
| **Episode / rollout** | One full attempt: prompt → tool calls → observations → final answer |
| **Trajectory** | The recorded sequence of that rollout |
| **Verifier / grader** | Code (or a model) that checks the outcome |
| **Reward** | The score given to a trajectory (binary, partial, shaped) |
| **Policy** | The model being trained |

- Relation to OpenAI Gym / Gymnasium: `reset()`, `step(action)`, observation, reward, done
- **Eval harness ≈ environment**: your Section 22 datasets + graders become training environments

## 34.3 Building Environments
- Task datasets (prompts with ground truth or success checks)
- Tool implementations inside the environment (sandboxed, resettable, deterministic where possible)
- State reset between episodes (fresh DB, fresh repo checkout, fresh container)
- Multi-turn environments with **simulated users** (an LLM playing the customer, as in τ-bench)
- Scaling rollouts (parallel sandboxes)
- Environment examples: SWE-Gym / SWE-bench-style repos, τ-bench (tau-bench, support tasks), WebArena / BrowserGym (web), OSWorld (computer use), text-to-SQL with execution checks
- Environment hubs and frameworks: Prime Intellect **verifiers** + Environments Hub, OpenAI Gym-style wrappers, and the environment components of agent-RL libraries

## 34.4 Verifiers & Reward Design
- **Verifiable rewards**: unit tests pass, SQL result matches, JSON validates, answer equals ground truth, final DB state correct
- **Rubric / LLM-judge rewards** for open-ended tasks (and their noise and bias)
- Outcome rewards vs process rewards (grading intermediate steps)
- Partial credit and reward shaping
- Penalties: too many steps, forbidden tool use, format violations, cost
- **Reward hacking**: the model finds loopholes (deleting failing tests, hard-coding answers, fooling the judge). Detect it by reading trajectories.

## 34.5 RL Algorithms (conceptual)
- Policy gradient intuition: make good trajectories more likely
- **PPO** (with a value model)
- **GRPO** (group-relative: sample several rollouts per prompt, compare them against each other; no value model). Widely used for reasoning and agent RL.
- DPO and preference optimization (offline, from pairs); how it differs from online RL
- KL penalty (staying close to the base model)
- Rejection sampling fine-tuning / expert iteration (a simple, strong baseline: keep only successful trajectories and SFT on them)

## 34.6 Tooling
- **Hugging Face TRL** (GRPOTrainer, PPO, DPO)
- **Unsloth** (memory-efficient RL/LoRA on a single GPU)
- Agent-RL frameworks: OpenPipe **ART**, **veRL**, **SkyRL**, **rLLM**, Prime Intellect **verifiers**, and others (fast-moving space; check current activity)
- **Provider RL fine-tuning**: e.g. OpenAI reinforcement fine-tuning (RFT) with custom graders
- Inference servers for fast rollouts: vLLM, SGLang
- Experiment tracking: Weights & Biases, MLflow

## 34.7 Trajectory Data
- Logging production traces as training data (Section 23 → training)
- Filtering successful trajectories for SFT
- Privacy and consent for training data (Section 30)
- Synthetic task generation to scale environments
- Data contamination between train and eval sets

## 34.8 Evaluating Trained Agents
- Held-out eval set (never trained on)
- Compare: base model, base + prompting, SFT, RL, and a frontier model
- Watch for regressions on general abilities
- Check for reward hacking by reading sampled trajectories
- Cost/latency benefit of the small trained model (Section 25)

---

## Hands-on Exercises
1. Wrap your Section 06 classifier eval as an environment with a `reward()` function.
2. Rejection-sampling baseline: sample 8 answers per prompt, keep correct ones, SFT a small model with LoRA.
3. Run GRPO with TRL/Unsloth on a small open model (roughly 0.5B–3B) for a verifiable task such as text-to-SQL, and plot reward over training steps.
4. Deliberately write a weak reward and find the model's hack.

## Project — Train a Small Specialist Agent
- Task: text-to-SQL agent (Section 29, Lab 2) or a tool-calling support agent on a τ-bench–style simulated environment
- Build the environment: sandboxed DB reset per episode, tool implementations, verifier comparing result sets or final DB state
- Baselines: small base model, small model + best prompt, frontier model
- Train: rejection-sampling SFT, then GRPO
- Report: success rate, cost per task, latency, and examples of reward hacking found and fixed
- Target: the small trained model closes most of the gap to the frontier model at a fraction of the cost

## Recommended Reading
- DeepSeekMath paper (introduced GRPO) and DeepSeek-R1 report
- Hugging Face TRL docs (GRPO trainer)
- τ-bench paper (simulated-user environments)
- SWE-Gym / SWE-smith (environments for coding agents)
- Lilian Weng, "Reward Hacking in Reinforcement Learning"

## Definition of Done
- [ ] One working, resettable environment with a verifier
- [ ] A measured improvement from RL or rejection sampling over the base model on held-out data
- [ ] A written list of reward-hacking behaviors you observed
