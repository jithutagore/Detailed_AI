# 12 — Deep Reinforcement Learning

> **Goal:** Combine the classical RL foundations (`ML\19`, `AI\10`) with deep neural networks to handle large/continuous state spaces — the technique behind everything from game-playing agents to RLHF and the agentic RL covered in `AI_Agents\34`.

**Level:** Applied · **Time:** 2 weeks · **Prerequisites:** `ML\19_reinforcement_learning_basics`, `AI\10_classical_reinforcement_learning_and_game_playing`, 02, 03

---

## Learning Objectives
- Explain why function approximation is necessary beyond tabular RL
- Implement Deep Q-Networks and understand their stabilization tricks
- Implement policy gradient methods
- Connect this section directly to RLHF and agentic RL in `AI_Agents\34`

---

## 12.1 Recap: Why Deep RL
- From `ML\19.6`: tabular Q-learning requires a table entry per (state, action) pair — infeasible for large or continuous state spaces (images, continuous control, language)
- The fix: approximate Q(s, a) or the policy π(a|s) with a neural network instead of a table
- This section is where `ML\19` (tabular theory) and Section 02–03 (neural network training) combine

## 12.2 Deep Q-Networks (DQN)
- Using a neural network to approximate Q(s, a), taking the state as input (recap Section 04 if the state is an image, e.g. Atari pixels)
- Why naively combining Q-learning with a neural network is unstable, and the fixes that made DQN work:
  - **Experience replay**: storing past transitions in a buffer and sampling randomly for training — breaks harmful correlation between consecutive experiences
  - **Target network**: a separate, slowly-updated copy of the network for computing target Q-values — stabilizes the moving-target problem
- Double DQN (reducing overestimation bias), Dueling DQN (separating state-value and advantage estimation) — awareness of the key improvements
- The Atari breakthrough (Mnih et al., 2013/2015): learning to play Atari games directly from pixels, historically significant as deep RL's first major success

## 12.3 Policy Gradient Methods
- Why value-based methods (DQN) struggle with continuous action spaces, and how policy gradient methods sidestep this by directly parameterizing and optimizing the policy
- **REINFORCE**: the basic policy gradient algorithm — increase the probability of actions that led to high reward
- High variance problem in REINFORCE, and the **baseline** fix (subtracting an expected value estimate to reduce variance without introducing bias)
- **Actor-Critic methods**: combining a policy (actor) with a learned value function (critic) that provides the baseline — the critic reduces variance, the actor selects actions

## 12.4 Modern Policy Optimization
- **Advantage Actor-Critic (A2C/A3C)**: using the advantage function (how much better an action was than average) instead of raw returns
- **Trust Region Policy Optimization (TRPO)** and **Proximal Policy Optimization (PPO)**: constraining how much the policy can change per update, for training stability — recap `AI_Agents\34.5`'s mention of PPO, now with the full mechanism explained
- Why PPO became the practical default: simpler to implement than TRPO, comparable performance, works well across many domains
- **GRPO** (Group Relative Policy Optimization): recap `AI_Agents\34.5` — sampling multiple outputs per prompt and comparing them against each other instead of using a separate value/critic network; this section gives you the actor-critic background needed to appreciate exactly what GRPO removes and why

## 12.5 Deep RL for Continuous Control (awareness)
- Continuous action spaces (robotics, physical control) vs discrete (games)
- DDPG, SAC (awareness — actor-critic variants designed for continuous actions)

## 12.6 Reward Design & Practical Challenges
- Recap `AI_Agents\34.4`'s treatment of reward design and reward hacking — same fundamental issues apply here, just for classical RL environments instead of LLM agent environments
- Sample efficiency: deep RL typically needs far more environment interactions than is practical outside simulation — why this matters for real-world (non-simulated) applications
- Exploration in large state spaces (recap `ML\19.5`'s bandit methods, now harder in high dimensions)

## 12.7 The Direct Line to RLHF and Agentic RL
- **RLHF** (Reinforcement Learning from Human Feedback, recap Section 09.2): a human preference model provides the reward signal, and PPO (from this section) is used to optimize the LLM's policy against it — this is literally the actor-critic/PPO machinery from 12.3–12.4, applied to next-token generation as the "action space"
- `AI_Agents\34` (agentic RL): environments, verifiers, and GRPO for training LLM-based agents — the direct modern extension of everything in this section, now applied to language models and tool-using agents instead of games/robotics
- This section is the last stop in the "classical → deep → agentic" RL progression that spans `ML\19` → `AI\10` → here → `AI_Agents\34`

---

## Hands-on Exercises
1. Implement DQN (with experience replay and a target network) for a classic control environment (e.g. CartPole); ablate by removing each stabilization trick and observe the training instability that results.
2. Implement REINFORCE from scratch on a simple environment; show the high variance problem empirically (run with different random seeds and compare learning curves).
3. Add a learned baseline (value function) to your REINFORCE implementation and show the variance reduction.
4. Implement a basic PPO agent (or use a well-documented reference implementation to study, then reimplement the clipped objective yourself) on a control task; compare stability and sample efficiency against your actor-critic implementation.

## Project — Deep RL Agent with Ablation Study
Train a DQN or PPO agent on a Gymnasium environment of your choice (a classic control task is sufficient scope). Conduct a systematic ablation study: for DQN, show the effect of removing experience replay and removing the target network separately; for PPO, show the effect of the clipping mechanism by comparing to an unclipped policy gradient. Present learning curves for every variant and write up what each component is actually responsible for.

## Recommended Resources
- Mnih et al., "Playing Atari with Deep Reinforcement Learning" (2013) and "Human-level control through deep reinforcement learning" (2015) — the DQN papers
- Schulman et al., "Proximal Policy Optimization Algorithms" (2017) — the PPO paper
- Sutton & Barto, *Reinforcement Learning: An Introduction* — policy gradient chapters (recap, now with neural network function approximation)
- OpenAI Spinning Up in Deep RL (excellent, code-first, free resource covering this entire section)
- Ouyang et al., "Training language models to follow instructions with human feedback" (RLHF paper — revisit after this section, it will read very differently)

## Definition of Done
- [ ] Your DQN ablation clearly shows why experience replay and the target network are both necessary
- [ ] Your PPO implementation trains more stably than plain policy gradient/actor-critic on the same task
- [ ] You can explain, in one paragraph, exactly how RLHF's use of PPO maps onto this section's actor-critic framework
- [ ] You can explain what GRPO (`AI_Agents\34.5`) removes relative to standard PPO, and why
