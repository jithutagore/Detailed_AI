# 11 — Memory

> **Goal:** Give agents memory across turns and sessions, without polluting context or leaking data between users.

**Level:** Core · **Time:** 1–2 weeks · **Prerequisites:** 08, 09

---

## Learning Objectives
- Manage short-term conversation state within context limits
- Design long-term memory (what to store, how to retrieve and update it)
- Handle memory quality, contradictions and privacy
- Use memory libraries and frameworks

---

## 11.1 Short-Term Memory
- Conversation history (message lists)
- State (task variables, intermediate results)
- Threads / sessions
- Context-window management:
  - Sliding window (last N messages)
  - Token-based trimming
  - **Summarization** (running summary + recent messages)
  - Tool-result clearing (dropping old, bulky tool outputs)
- Persisting sessions (Postgres, Redis)

## 11.2 Long-Term Memory
What to store:
- **User preferences** (tone, language, formats)
- **Facts** (about the user, the organization, the domain)
- **Previous tasks** and outcomes
- **Important interactions**
- Learned procedures ("how this user likes reports built")

## 11.3 Memory Types (cognitive framing)
```
Agent
 ↓
Memory Manager
 ├── Short-term / working memory   (current context)
 ├── Episodic memory               (past events and experiences)
 ├── Semantic memory               (facts and knowledge)
 ├── Procedural memory             (skills, instructions, learned rules)
 └── User profile                  (structured preferences)
```

## 11.4 Memory Operations
- **Write**: when to save (every turn? on explicit request? in the background after the conversation?)
- **Extraction**: LLM extracts candidate memories from the conversation
- **Consolidation**: merge duplicates, update existing memories
- **Retrieval**: semantic search, recency, importance scoring
- **Forgetting**: TTLs, decay, explicit deletion
- Hot-path (in-loop) vs background memory writing
- Memory as a tool (the agent calls `save_memory` / `search_memory`) vs automatic memory
- File-based memory (Markdown notes the agent reads and edits)

## 11.5 Storage Options
- Key-value / JSON documents (profiles)
- Vector store (semantic memories)
- Relational DB (structured facts, audit trail)
- Knowledge graph (entities and relations, e.g. Zep/Graphiti)

## 11.6 Memory Problems
- **Memory pollution** (storing trivia)
- **Incorrect memories** (misunderstood facts)
- **Contradictions** (old vs new preference)
- **Stale information**
- **Privacy**: PII, sensitive data, right to be forgotten
- **Multi-user isolation**: strict namespacing by user and tenant
- Memory-based prompt injection (malicious content saved as memory)
- Transparency: letting users view, edit and delete their memories

## 11.7 Tools & Frameworks
- LangGraph checkpointers (short-term) + Store (long-term)
- LangMem
- Mem0
- Zep / Graphiti
- Letta (formerly MemGPT): the self-editing memory concept
- Provider memory features (e.g. memory tools in agent SDKs)

---

## Project — Personal AI Assistant with Long-Term Memory
- Remembers preferences and facts across sessions
- Background memory extraction after each conversation
- Conflict resolution (newer fact replaces older, history kept)
- `/memories` endpoint: list, edit, delete
- Strict per-user isolation, with a test proving user A can't retrieve user B's memories
- **Eval:** 20 multi-session scenarios checking correct recall and correct forgetting

## Definition of Done
- [ ] Context size stays bounded in long conversations
- [ ] Isolation test passes
- [ ] The user can delete all their memories
