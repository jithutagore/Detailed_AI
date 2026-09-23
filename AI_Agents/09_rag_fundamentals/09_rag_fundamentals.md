# 09 — RAG Fundamentals

> **Goal:** Build a reliable Retrieval-Augmented Generation pipeline, from document ingestion to cited answers.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** 03 (embeddings), 07

---

## Learning Objectives
- Build the full ingestion pipeline: load, parse, clean, chunk, embed, index
- Implement dense, sparse and hybrid retrieval
- Use at least three vector stores
- Generate grounded answers with citations and measure retrieval quality

---

## 9.1 Why RAG
- Knowledge cutoff, private data, hallucination reduction
- RAG vs long context vs fine-tuning, and when to use each

## 9.2 Document Pipeline
```
Documents → Loader → Parsing → Cleaning → Chunking → Embedding → Vector DB (+ metadata)
```
- **Loaders**: PDF, DOCX, HTML, Markdown, CSV, email, Notion/Confluence, databases
- **Parsing** *(added — most RAG failures start here)*:
  - Text-based vs scanned PDFs, OCR (Tesseract, cloud OCR)
  - Layout-aware parsing: **Docling**, **Unstructured**, **LlamaParse**, **PyMuPDF**, Marker
  - Tables, headers and footers, multi-column layouts, images
  - Vision-LLM parsing for complex documents
- **Cleaning**: boilerplate removal, deduplication, normalization, language detection
- **Chunking**: see 9.2b below
- **Metadata**: source, page, section, date, author, access control labels
- **Embedding**: choosing a model (MTEB leaderboard, dimensions, language, cost), batching, normalization
- **Incremental indexing**: updates, deletes, re-embedding when the model changes

## 9.2b Chunking Strategies *(expanded)*
Chunking decides what a "unit of retrieval" is. It's one of the highest-impact choices in RAG and one of the most often ignored.

### Quick-reference map (learn top to bottom)
| Technique | Main idea | Difficulty | Where |
|---|---|---:|---|
| Fixed-size | N characters/tokens | ⭐ | 9.2b |
| Sentence | Sentence boundaries | ⭐ | 9.2b |
| Paragraph | Paragraph boundaries | ⭐ | 9.2b |
| Recursive | Hierarchical separators | ⭐⭐ | 9.2b |
| Token-based | Token limits (tokenizer-aware sizing) | ⭐⭐ | 9.2b |
| Sliding window | Overlapping windows | ⭐⭐ | 9.2b |
| Structure-based | Document hierarchy (parser elements) | ⭐⭐ | 9.2b |
| Markdown/HTML | Markup hierarchy | ⭐⭐ | 9.2b |
| Semantic | Meaning boundaries | ⭐⭐⭐ | 9.2b |
| Table-aware | Preserve tables | ⭐⭐⭐ | 9.2b |
| Code/AST | Program structure | ⭐⭐⭐ | 9.2b |
| Parent-child | Search small, return parent | ⭐⭐⭐ | 9.2b, 10.2 |
| Sentence-window | Search a sentence, return its neighbors | ⭐⭐⭐ | 9.2b, 10.2 |
| Contextual | Add surrounding context to each chunk | ⭐⭐⭐⭐ | 9.2b, 10.2 |
| Proposition | Atomic facts | ⭐⭐⭐⭐ | 9.2b, 10.2 |
| Hierarchical | Multi-level retrieval (+ auto-merging) | ⭐⭐⭐⭐ | 10.2 |
| RAPTOR | Recursive summary tree | ⭐⭐⭐⭐ | 10.2 |
| Agentic | LLM decides boundaries | ⭐⭐⭐⭐ | 9.2b, 10.2 |
| Adaptive | Strategy chosen per document type | ⭐⭐⭐⭐ | 10.2 |
| Late chunking | Contextual embeddings first, then split | ⭐⭐⭐⭐⭐ | 9.2b, 10.2 |
| Query-aware | Optimize chunks for expected query types | ⭐⭐⭐⭐⭐ | 9.2b, 10.2 |

### Why chunking matters
- Embedding models have input limits, and one vector can't represent a long document well
- Too small: chunks lose context ("it increased by 20%": what increased?)
- Too large: the embedding blurs several topics, retrieval gets less precise, and tokens are wasted
- Chunk boundaries that cut sentences, tables or code in half break meaning

### Chunk parameters
- **Chunk size**: measured in **tokens** (preferred) or characters; common starting ranges are 256–1,024 tokens
- **Chunk overlap** (e.g. 10–20%) so ideas that cross a boundary aren't lost; the trade-off is more storage and duplicate hits
- Matching chunk size to the embedding model's max input and to the question type (factoid questions → smaller chunks; "explain" questions → larger chunks)

### Basic strategies
| Strategy | How it works | Good for | Weakness |
|---|---|---|---|
| **Fixed-size** (character or token) | Cut every N tokens, with overlap | Baseline, uniform text | Cuts mid-sentence or mid-idea |
| **Sentence-based** | Split on sentence boundaries (NLTK, spaCy, regex), group N sentences | Prose, FAQs | Sentences vary a lot in length |
| **Paragraph-based** | Split on blank lines / paragraphs | Well-written documents | Paragraphs can be huge or tiny |
| **Recursive character/token splitting** | Try separators in order (`\n\n` → `\n` → `. ` → ` `) until chunks fit | Good general default | Still ignores document structure |
| **Sliding window** | Fixed window moving by a step smaller than its size | Dense technical text | Lots of duplication |

### Structure-aware (document-specific) strategies
| Content type | Strategy |
|---|---|
| **Markdown** | Split by headers (`#`, `##`), keep the header path as metadata (e.g. `Guide > Install > Windows`) |
| **HTML** | Split by tags/sections (`<h1>`–`<h3>`, `<section>`, `<article>`); strip navigation and boilerplate |
| **PDF** | Split by layout elements from the parser (titles, sections, lists); page-level chunks when page citations matter |
| **Tables** | Keep a table whole if small; otherwise chunk by rows **with the header row repeated** in every chunk; or convert rows to sentences; store a table summary as well |
| **Code** | Split by functions/classes using the **AST** (tree-sitter, language-aware splitters); keep imports and class signatures as context |
| **JSON / structured data** | Split by object/record; keep key paths |
| **Emails / chats** | Split by message or thread; keep sender, date and subject as metadata |
| **Legal / contracts** | Split by clause/section numbering |
| **Slides** | One slide per chunk, plus speaker notes |
| **Transcripts** (calls, meetings, audio) | Split by speaker turns or time windows, keeping timestamps |

### Semantic & model-based strategies
- **Semantic chunking**: embed each sentence, then start a new chunk where the similarity between neighboring sentences drops (a topic shift). Thresholds: percentile, standard deviation, gradient.
- **LLM-based / agentic chunking**: an LLM decides the boundaries and can title and summarize each chunk. Highest quality, highest cost; use it for small, high-value corpora.
- **Propositional chunking**: an LLM rewrites the text into atomic, self-contained facts ("propositions"), and each becomes a retrieval unit (from the "Dense X Retrieval" paper)
- **Late chunking**: embed the **whole document** with a long-context embedding model first, then pool the token embeddings per chunk, so every chunk vector "knows" the full document context (Jina AI's approach)
- **Query-aware chunking**: design chunks around the questions users actually ask, not only around the document
  - Analyze real or expected queries (from query logs or a generated question set): factoid lookups, comparisons, procedures, summaries
  - Pick the granularity per query type: small chunks/propositions for facts, whole sections for "how do I…", document summaries for "overview of…"
  - **Multi-granularity indexing**: index the same corpus at several chunk sizes, then **route** each query to the right index (or search all and fuse with RRF)
  - Question-aligned chunks: generate "questions this chunk answers" and index them (links to multi-vector indexing, Section 10.2)
  - Keep the answer to a common question together in one chunk (e.g. a full procedure with all its steps)
  - Needs a good query set and ongoing re-evaluation as query patterns change

### Hierarchical & multi-granularity strategies
Covered in depth in Section 10.2. Know the names now:
- **Small-to-big / parent-child** (retrieve small chunks, return the parent)
- **Sentence-window** (retrieve a sentence, return the neighboring sentences)
- **Hierarchical chunking** (document → section → paragraph levels)
- **Contextual chunk headers / contextual retrieval** (prepend the document title, section path or an LLM-written context sentence to each chunk)
- **RAPTOR** (recursive summary tree)

### Chunk enrichment
- Metadata: source, page, section path, date, author, language, doc type, access labels
- Chunk title / section path prepended to the text before embedding
- Chunk summary, keywords, and "questions this chunk answers" (used for multi-vector indexing)
- Stable **chunk IDs** (hash of doc ID + position + content) for citations and for updating without duplicates
- Links to previous/next chunks (enables sentence-window style expansion)

### Evaluating chunking strategies
- Never pick a strategy by intuition; **measure it** with Recall@K / MRR on your Q&A set
- Chunk-size sweep (e.g. 256 / 512 / 1,024 tokens × 0% / 10% / 20% overlap)
- Compare strategies per document type (the best strategy for code isn't the best for contracts)
- Watch the index size and ingestion cost of LLM-based methods
- Inspect chunks by eye: print 20 random chunks and check that each one makes sense on its own

### Tools
- LangChain text splitters (`RecursiveCharacterTextSplitter`, `MarkdownHeaderTextSplitter`, `HTMLHeaderTextSplitter`, language-aware code splitters, `SemanticChunker`)
- LlamaIndex node parsers (`SentenceSplitter`, `SemanticSplitterNodeParser`, `HierarchicalNodeParser`, `MarkdownNodeParser`, `CodeSplitter`)
- **Chonkie** (a dedicated chunking library), Unstructured and Docling chunkers (element-based), tiktoken for token counting

### Chunking exercise
Take 3 document types (a PDF report, a Markdown doc site, a Python repo). For each, compare 4 strategies (fixed, recursive, structure-aware, semantic) on a 20-question eval set. Report Recall@5, number of chunks, and ingestion time and cost.

## 9.3 Retrieval
- **Dense retrieval** (vector similarity)
- **Sparse retrieval**: TF-IDF, **BM25**, learned sparse (SPLADE)
- **Semantic search** vs keyword search, and when each wins
- **Hybrid search** (dense + sparse)
- **Metadata filtering** (date, department, user permissions)
- **Top-K** selection
- **Similarity thresholds**
- Distance metrics: cosine, dot product, L2
- ANN indexes: HNSW, IVF, and the recall vs speed trade-off

## 9.4 Vector Databases
Learn at least these hands-on:
- **FAISS**: in-memory library, good for learning
- **Chroma**: simple local development
- **Qdrant**: production vector DB with filtering and hybrid search
- **pgvector**: vectors inside PostgreSQL (often the best default when you already run Postgres)

Understand the concepts behind:
- Pinecone, Weaviate, Milvus, Elasticsearch/OpenSearch vector search, LanceDB

Comparison criteria: hosting, filtering, hybrid support, scale, cost, multi-tenancy.

## 9.5 Generation
- Prompt template: instructions + retrieved chunks + question
- **Citations**: chunk IDs → source references
- "Answer only from the context; otherwise say you don't know"
- Handling conflicting sources
- Native citation features in provider APIs

## 9.6 Measuring RAG (intro)
- Retrieval: Recall@K, Precision@K, MRR
- Generation: faithfulness, answer relevance
- Build a golden Q&A set with source references
- Tools: Ragas, DeepEval (in depth in Section 22)

---

## Project — Enterprise Knowledge Agent (v1)
```
PDF, DOCX, Web pages, Database rows
        ↓
Ingestion pipeline (parse, chunk, embed, metadata)
        ↓
Qdrant or pgvector (hybrid search)
        ↓
Retrieval tool used by the agent from Section 08
        ↓
Answer with citations (document + page)
```
- Ingestion is a CLI or background job
- Retrieval is exposed as an agent **tool**
- **Eval:** 30 Q&A pairs; report Recall@5 and faithfulness
- Compare 2 chunking strategies and 2 embedding models

## Common Pitfalls
- Skipping parsing quality checks (garbage in, garbage out)
- Chunks without metadata
- Never measuring retrieval separately from generation
- Ignoring document-level access control

## Definition of Done
- [ ] Every answer cites a source
- [ ] Retrieval metrics measured and documented
- [ ] Re-ingestion is idempotent (no duplicates)
