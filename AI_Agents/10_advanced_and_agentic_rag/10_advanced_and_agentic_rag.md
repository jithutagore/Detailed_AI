# 10 — Advanced Retrieval & Agentic RAG

> **Goal:** Improve retrieval quality with advanced techniques, then let an agent decide *whether, where, and how* to retrieve.
> **Change from original:** "Advanced Retrieval" (old 4.3) and "Agentic RAG" (old Phase 5) are merged into one section, and GraphRAG is added.

**Level:** Core · **Time:** 2–3 weeks · **Prerequisites:** 08, 09

---

## Learning Objectives
- Apply query transformation, reranking and fusion to improve retrieval
- Build RAG over multiple sources (vectors, SQL, web, APIs)
- Implement adaptive, corrective and self-reflective RAG patterns
- Understand GraphRAG and when a knowledge graph helps

---

## Part A — Advanced Retrieval Techniques

### 10.1 Query Transformation
- **Query rewriting** (turning conversational follow-ups into standalone queries)
- **Query expansion** (synonyms, related terms)
- **Multi-query retrieval** (several paraphrases, then merge)
- Query decomposition (sub-questions)
- Step-back prompting
- **HyDE** (Hypothetical Document Embeddings)

### 10.2 Better Indexing
- **Parent-child retrieval** (retrieve small chunks, return the larger parent)
- Sentence-window retrieval
- **Contextual retrieval** (prepending document context to each chunk before embedding)
- Summary indexes and hierarchical indexes (RAPTOR)
- Multi-vector indexing (summaries + chunks + hypothetical questions)
- Late-interaction models (ColBERT) — concept
- **Advanced chunking in practice** (the basics are introduced in Section 9.2b):
  - **Hierarchical chunking** (multi-level: document → section → paragraph) with auto-merging retrieval (when several child chunks from the same parent are retrieved, return the parent instead)
  - **Late chunking** (long-context embedding first, then per-chunk pooling) vs contextual retrieval (an LLM writes context for each chunk): cost and quality comparison
  - **Propositional indexing** (atomic facts as retrieval units, linked back to the source chunk for the answer)
  - **Agentic / LLM chunking** for high-value corpora
  - **Adaptive chunking** (a different strategy per document type, chosen automatically from the parser's output)
  - **Query-aware chunking in production**: multi-granularity indexes + a query router (ties into Adaptive RAG, 10.7); re-tuning chunking as query logs change
  - Chunk-level deduplication and near-duplicate detection (MinHash) across versions of the same document
  - Re-chunking and re-indexing strategy when you change the chunker (versioned indexes, blue/green index swap)
  - Exercise: on the Section 09 eval set, compare recursive vs contextual retrieval vs late chunking vs propositional indexing (Recall@5, cost per 1,000 pages, latency)

### 10.3 Ranking & Fusion
- **Reranking** with cross-encoders (Cohere Rerank, BGE-reranker, Jina, Voyage)
- LLM-based reranking
- **Reciprocal Rank Fusion (RRF)** for hybrid results
- Diversity (MMR, Maximal Marginal Relevance)

### 10.4 Context Optimization
- **Context compression** (extracting only relevant sentences)
- Deduplication of retrieved chunks
- Ordering chunks (most relevant at the start and end)
- Token budgeting for retrieved context

### 10.5 GraphRAG & Knowledge Graphs *(added)*
- Entity and relationship extraction with LLMs
- Graph databases (Neo4j), Cypher basics
- Microsoft GraphRAG, LightRAG concepts
- Local vs global questions (why vector RAG struggles with "summarize themes across all documents")
- Hybrid vector + graph retrieval

### 10.6 Multimodal RAG *(added)*
- Retrieving images, tables and charts
- Multimodal embeddings, ColPali-style page-image retrieval

---

## Part B — Agentic RAG

Traditional:
```
Question → Retriever → Answer
```
Agentic:
```
Question
 ↓
Agent: Should I search? Which source?
 ↓
Query Rewrite
 ↓
Retrieve
 ↓
Evaluate documents (relevant? sufficient?)
 ↓
Need more information? ── yes ──→ rewrite / other source / web search
 ↓ no
Answer (with citations) → Check groundedness
```

### 10.7 Patterns
- **Adaptive RAG**: route by query complexity (no retrieval / single-step / multi-step)
- **Corrective RAG (CRAG)**: grade retrieved docs and fall back to web search if they're poor
- **Self-RAG**: the model reflects on whether to retrieve and whether its answer is supported
- **Agentic RAG**: retrieval as tools inside the agent loop
- Iterative / multi-hop retrieval
- **Query routing**: vector store vs SQL vs web vs API
- **Retrieval planning**: decide the sequence of lookups up front

### 10.8 Multi-Source RAG
- **Multi-source RAG** with source selection
- **SQL + RAG**: text-to-SQL for structured data, vectors for unstructured
- **Web + RAG**: internal knowledge first, web for freshness
- API sources (live data)
- Merging and citing results from different sources
- Handling conflicts between sources

### 10.9 Quality Controls
- Relevance grading (LLM-as-judge on retrieved docs)
- Hallucination / groundedness check after generation
- Answer completeness check
- Retry limits to avoid endless loops

---

## Project — Enterprise Research Agent
Sources: **PDF (vector DB) · SQL database · Company website · External API · Web search**
- The agent chooses the source(s) per question
- Implements Corrective RAG (grade → rewrite → web fallback)
- Hybrid search + reranking
- Every claim cited with its source type
- **Eval:** compare naive RAG vs advanced vs agentic on 40 questions (accuracy, faithfulness, latency, cost)

## Common Pitfalls
- Adding agentic loops before fixing basic retrieval quality
- Unbounded re-retrieval loops
- Paying agentic latency and cost on simple questions (use adaptive routing)

## Definition of Done
- [ ] A measured improvement over the Section 09 baseline
- [ ] A documented latency and cost trade-off for each technique
