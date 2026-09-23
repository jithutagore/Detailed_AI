# 13 — LangChain

> **Goal:** Use LangChain as a component library, not as magic. By now you've built everything by hand, so you'll see exactly what each abstraction replaces.

**Level:** Frameworks · **Time:** 1–2 weeks · **Prerequisites:** 07–12

---

## Learning Objectives
- Use LangChain's standard interfaces for models, messages, tools and retrievers
- Build agents with `create_agent` and middleware (LangChain v1)
- Know when LangChain helps and when plain SDK code is simpler

---

## 13.1 Package Structure
- `langchain` (agents, high-level APIs)
- `langchain-core` (base abstractions, Runnables)
- Integration packages (`langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-ollama`, `langchain-qdrant`, …)
- `langchain-community`
- `langchain-classic` (legacy chains)
- Relationship to LangGraph (LangChain agents run on LangGraph)

## 13.2 Models & Messages
- Chat models, `init_chat_model` (provider-agnostic)
- Message types: `SystemMessage`, `HumanMessage`, `AIMessage`, `ToolMessage`
- Standard content blocks (text, reasoning, images, tool calls)
- Streaming (`stream`, `astream`, `astream_events`)
- Batching
- Token usage metadata
- Rate limiters and retries

## 13.3 Prompts
- `ChatPromptTemplate`, `MessagesPlaceholder`
- Partial variables
- LangSmith Prompt Hub

## 13.4 Structured Output
- `with_structured_output(PydanticModel)`
- Tool-strategy vs provider-native strategy
- Output parsers (legacy, and when you still need them)

## 13.5 Tools
- `@tool` decorator, `StructuredTool`
- Tool schemas from type hints and docstrings
- `ToolRuntime` / injected state and context
- Prebuilt integrations (search, SQL, file system)
- Returning artifacts vs content

## 13.6 Agents
- `create_agent(model, tools, system_prompt, ...)`
- Agent state and the message loop
- Structured final responses (`response_format`)
- Dynamic models and dynamic tools

## 13.7 Middleware (v1)
- What middleware is (hooks before/after model and tool calls)
- Built-in middleware: summarization, human-in-the-loop, PII redaction, model fallback, tool call limits, and similar
- Writing custom middleware (logging, guardrails, dynamic prompts)

## 13.8 Retrieval Components
- **Document loaders**
- **Text splitters**
- **Embeddings**
- **Vector stores** and **retrievers**
- Building a RAG agent with a retriever tool

## 13.9 LCEL / Runnables (for maintaining existing code)
- The `|` pipe syntax, `RunnableParallel`, `RunnablePassthrough`
- You'll see it in older codebases; know how to read it

## 13.10 When Not to Use LangChain
- Simple single-provider apps
- Places where abstraction hides important provider-specific features
- Debugging deep abstraction stacks

---

## Project — Rebuild Your Assistant with LangChain
Combine **LLM + Tools + RAG + Memory**:
- Port your Personal Assistant (07) and Knowledge Agent (09) into one LangChain agent
- Use middleware for summarization, HITL on write tools and PII redaction
- Trace with LangSmith
- **Compare** code size, readability and eval results against your hand-built version

## Definition of Done
- [ ] Same or better eval scores than the from-scratch version
- [ ] A written comparison: what the framework simplified, and what it hid
