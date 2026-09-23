# 19 — Reinforcement Learning Basics  *(Bridge section)*

> **Goal:** Understand the RL problem framing and classical algorithms, as a foundation for the agentic RL content in the AI Agents syllabus (Section 34).
> **Note:** Deep RL (policy gradients with neural networks, PPO, GRPO applied to LLMs) belongs in the deep learning / LLM engineering folders and in AI Agents Section 34. This section covers the classical, tabular foundations.

**Level:** Bridge · **Time:** 1–2 weeks · **Prerequisites:** 02, 06

---

## Learning Objectives
- Frame a problem as a Markov Decision Process
- Explain the exploration-exploitation tradeoff and solve multi-armed bandit problems
- Implement tabular Q-learning and value iteration
- Understand where classical RL ends and deep/agentic RL begins

---

## 19.1 The RL Problem
- Agent, environment, state, action, reward, policy (link forward to AI Agents Section 34.2, which uses this exact vocabulary)
- Episodic vs continuing tasks
- The reward hypothesis: all goals expressible as reward maximization
- **Markov Decision Process (MDP)**: states, actions, transition probabilities, rewards, discount factor (γ)
- The Markov property

## 19.2 Value Functions & Bellman Equations
- State-value function V(s), action-value function Q(s, a)
- The **Bellman equation** (recursive decomposition of value)
- Optimal policy and optimal value function
- Discounting and why γ < 1 matters

## 19.3 Dynamic Programming (when the model is known)
- **Policy evaluation**, **policy iteration**, **value iteration**
- Why DP doesn't scale (requires a full model of the environment)

## 19.4 Model-Free Methods
- Monte Carlo methods (learning from complete episodes)
- **Temporal Difference (TD) learning**: the core idea of bootstrapping
- **Q-learning** (off-policy TD control)
- SARSA (on-policy TD control)
- Q-learning vs SARSA: the cliff-walking example (why they learn different policies)

## 19.5 Exploration vs Exploitation
- ε-greedy, decaying ε
- **Multi-armed bandits**: a simplified RL problem (no state transitions)
- Bandit algorithms: ε-greedy, UCB (Upper Confidence Bound), Thompson Sampling
- Where bandits are used in practice: A/B testing alternatives, recommendation ranking, ad serving

## 19.6 Function Approximation (bridge to deep RL)
- Why tabular methods fail with large/continuous state spaces
- Approximating Q(s, a) with a function (linear, then neural network — this is where Deep Q-Networks begin)
- Brief pointer to policy gradient methods (full treatment in AI Agents Section 34.5: PPO, GRPO)

## 19.7 RL vs Supervised Learning
- No fixed labeled dataset — the agent generates its own experience
- Delayed reward / credit assignment problem
- Non-i.i.d. data (sequential, correlated)
- Why this connects directly to training LLM agents (AI Agents Section 34)

---

## Hands-on Exercises
1. Solve a small grid-world MDP with value iteration; visualize the optimal policy.
2. Implement tabular Q-learning on FrozenLake or a custom grid world (Gymnasium).
3. Implement ε-greedy, UCB and Thompson Sampling on a multi-armed bandit simulation; compare cumulative regret.
4. Compare Q-learning vs SARSA on the cliff-walking environment and explain the difference in learned paths.

## Mini Project — Grid-World Agent
Build a grid-world environment (Gymnasium-style: `reset()`, `step()`) with obstacles and a goal. Solve it with value iteration, then with tabular Q-learning. Compare convergence speed and the learned policies. Visualize the value function as a heatmap.

## Recommended Resources
- *Reinforcement Learning: An Introduction* (Sutton & Barto) — free PDF, the standard reference
- David Silver's RL course (DeepMind/UCL, freely available lectures)
- Gymnasium documentation (the maintained fork of OpenAI Gym)

## Definition of Done
- [ ] Your Q-learning agent converges to the optimal policy on a known grid world
- [ ] You can explain the exploration-exploitation tradeoff with a concrete example
- [ ] You see the direct line from this section to AI Agents Section 34 (agentic RL, GRPO, reward design)
