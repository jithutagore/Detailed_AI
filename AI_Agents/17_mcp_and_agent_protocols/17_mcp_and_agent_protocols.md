# 17 — MCP & Agent Protocols

> **Goal:** Build and consume Model Context Protocol (MCP) servers, and understand agent-to-agent protocols (A2A).
> **Changes from original:** Added A2A and other protocols. The claim about a "July 2026 spec" couldn't be verified; the spec versions I can confirm are `2024-11-05`, `2025-03-26`, `2025-06-18` and `2025-11-25`. **Always check the current spec at modelcontextprotocol.io**, because it changes quickly.

**Level:** Advanced · **Time:** 1–2 weeks · **Prerequisites:** 07, 02 (auth)

---

## Learning Objectives
- Explain the MCP architecture and its primitives
- Build MCP servers (local and remote) and connect them to clients
- Secure MCP servers with proper authorization
- Understand A2A and when to use it instead of MCP

---

## Part A — Model Context Protocol

### 17.1 Architecture
- **Host** (the app, e.g. Claude Desktop, Claude Code, an IDE, your agent)
- **Client** (one per server connection, inside the host)
- **Server** (exposes capabilities)
- JSON-RPC 2.0 message format
- Lifecycle: initialize → capability negotiation → operation → shutdown
- Protocol versioning

### 17.2 Server Primitives
- **Tools** (model-controlled actions)
- **Resources** (application-controlled data, URIs, templates, subscriptions)
- **Prompts** (user-controlled templates, often exposed as slash commands)

### 17.3 Client Primitives
- **Sampling** (the server asks the client's LLM for a completion)
- **Roots** (filesystem boundaries)
- **Elicitation** (the server asks the user for input)

### 17.4 Transports
- **stdio** (local subprocess)
- **Streamable HTTP** (remote; replaced the older HTTP+SSE transport)
- Session management, resumability
- Keep up with spec evolution (for example, work on stateless operation and scaling)

### 17.5 Authentication & Authorization
- OAuth 2.1 for remote servers
- Protected resource metadata, authorization server discovery
- Dynamic client registration / client ID metadata documents
- Token audience validation and why **token passthrough is forbidden**
- Scopes and least privilege

### 17.6 Tool Discovery & Ecosystem
- `tools/list`, list-changed notifications
- MCP registries and server catalogs
- Official SDKs: Python (including FastMCP), TypeScript, and others
- MCP Inspector for debugging
- Using MCP in LangChain (`langchain-mcp-adapters`), OpenAI Agents SDK, Claude Agent SDK, and via provider APIs (remote MCP connectors)

### 17.7 MCP Security
- **Tool poisoning** (malicious instructions in tool descriptions)
- Rug pulls (tool definitions changing after approval)
- Tool-name shadowing across servers
- Confused-deputy problems
- Prompt injection through tool results and resources
- Over-privileged servers, credential storage
- Only install trusted servers; pin versions; review tool descriptions
- Sandboxing local servers

---

## Part B — Agent-to-Agent & Other Protocols *(added)*

### 17.8 A2A (Agent2Agent Protocol)
- Purpose: agents from different vendors or frameworks collaborating
- Agent Cards (capability discovery)
- Tasks, messages, artifacts, task lifecycle
- Streaming and push notifications
- **MCP vs A2A**: MCP connects agent ↔ tools/data; A2A connects agent ↔ agent

### 17.9 Other Protocols (awareness)
- AG-UI (agent ↔ frontend UI events)
- Agent payment and commerce protocols (emerging)
- OpenAPI as a tool source

---

## Build — Custom MCP Server
```
AI Agent (LangGraph or Claude/OpenAI SDK)
    ↓
MCP Client
    ↓
Your MCP Server (Python, FastMCP)
 ├── Database   (read-only query tool + schema resource)
 ├── Files      (restricted to one root directory)
 ├── GitHub     (list issues, create issue — write tool)
 └── Internal API
```
- Local (stdio) **and** remote (Streamable HTTP) modes
- OAuth-protected remote deployment
- Prompts exposed as reusable templates
- Tested with MCP Inspector and connected to at least 2 different hosts
- **Security review** of your own server against the threats in 17.7

## Stretch Project
Two agents built in different frameworks that talk over A2A (e.g. a LangGraph "research agent" serving an ADK "report agent").

## Definition of Done
- [ ] The server works in 2+ MCP hosts
- [ ] The remote server requires auth
- [ ] A written threat model for the server
