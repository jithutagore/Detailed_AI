# 04 — LLM APIs & Providers  *(NEW section)*

> **Goal:** Be fluent with the major LLM APIs and local model runtimes, and write provider-agnostic code.
> **Why added:** The original learning order said "LLM APIs", but no phase taught them.

**Level:** Foundation · **Time:** 1 week · **Prerequisites:** 01, 03

---

## Learning Objectives
- Call closed-model APIs (OpenAI, Anthropic, Google Gemini) and open-weight models
- Use streaming, token usage and error handling correctly
- Run models locally
- Build a thin abstraction so you can swap providers

---

## 4.1 Chat/Message API Anatomy
- Messages: `system`, `user`, `assistant`, tool messages
- Content blocks (text, image, document, tool_use/tool_result)
- Parameters: `model`, `max_tokens`, `temperature`, `top_p`, `stop`
- Response structure: content, stop/finish reason, **usage** (input/output tokens)
- Stateless API: you send the full history every call
- Stateful APIs (e.g. OpenAI Responses API with stored conversations) vs stateless ones

## 4.2 Major Providers
- **OpenAI**: Chat Completions vs Responses API, built-in tools
- **Anthropic (Claude)**: Messages API, tool use, extended thinking, prompt caching, the Claude Agent SDK
- **Google Gemini**: Gemini API / Vertex AI
- **Cloud platforms**: AWS Bedrock, Azure AI Foundry / Azure OpenAI, Google Vertex AI (enterprise access, data residency)
- **Aggregators**: OpenRouter, LiteLLM (one API for many models)

## 4.3 Open-Weight & Local Models
- Model families: Llama, Qwen, Mistral, Gemma, DeepSeek, gpt-oss, and others
- Model hubs: Hugging Face
- Local runtimes: **Ollama**, LM Studio, llama.cpp
- Serving at scale: **vLLM**, SGLang, TGI
- Quantization (GGUF, AWQ, 4-bit/8-bit) and the trade-off between memory and quality
- OpenAI-compatible endpoints (why most tools "speak OpenAI")

## 4.4 Streaming
- SSE event types (text delta, tool-call delta, message stop)
- Accumulating deltas into a final message
- Streaming tool-call arguments
- Forwarding a stream through FastAPI to a frontend

## 4.5 Production API Concerns
- Rate limits (RPM, TPM), `429` handling, `Retry-After`
- Errors: `400` (bad request), `401`, `429`, `500`/`529` overloaded; which ones to retry
- Timeouts and cancellation
- **Token counting** before sending a request
- **Prompt caching** (provider-side): cache breakpoints, TTL, savings
- Batch APIs (roughly 50% cheaper, asynchronous)
- Cost calculation per request
- Data privacy: zero-data-retention options, regional endpoints

## 4.6 Provider-Agnostic Design
- Writing an `LLMClient` interface with `generate()` / `stream()`
- LiteLLM or framework-level abstractions (LangChain `init_chat_model`)
- What doesn't port cleanly: tool formats, thinking blocks, caching and multimodal inputs differ between providers

## 4.7 Model Selection Basics
- Benchmarks and why you shouldn't trust them blindly
- Leaderboards (LMArena, Artificial Analysis)
- Your own eval is the real benchmark (Section 22)
- Context length, price, latency, tool-use quality, license

---

## Hands-on Exercises
1. Send the same prompt to 3 providers and 1 local Ollama model. Log latency, tokens and cost.
2. Implement streaming output in the terminal with the token count shown at the end.
3. Implement exponential-backoff retry for `429`/`5xx` errors only.
4. Enable prompt caching on a long system prompt and measure the cost and latency difference.

## Project — Multi-Provider LLM Gateway
A FastAPI service (extending Section 02) with:
- `POST /generate` with a `provider` and `model` parameter
- Streaming support
- Unified usage/cost logging to Postgres
- Automatic fallback to a second provider on failure

## Definition of Done
- [ ] Works with at least 2 cloud providers + 1 local model
- [ ] Cost is calculated and stored for every call
- [ ] Retries only on retryable errors
