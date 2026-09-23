# 07 — Function Calling & Tool Engineering

> **Goal:** Give LLMs safe, well-designed tools. Tools are what turn a chatbot into an agent, and tool design is one of the biggest factors in agent quality.

**Level:** Core · **Time:** 2 weeks · **Prerequisites:** 04, 06

---

## Learning Objectives
- Define tools with schemas and handle tool calls and results correctly
- Design tools that models use accurately
- Handle tool errors, timeouts and permissions
- Separate read tools from write (side-effect) tools

---

## 7.1 Tool Calling Mechanics
- **Function definitions**: name, description, input schema
- **Tool schemas** (JSON Schema) and generating them from Pydantic or Python signatures
- The request/response cycle: model emits `tool_call` → your code executes → you send `tool_result` → model continues
- **Arguments** parsing and validation
- **Tool results**: format, size, returning errors as results
- **Tool selection**: `tool_choice` = auto / required / specific tool / none
- **Parallel tool calls** (several calls in one turn)
- Tool call IDs and matching results to calls
- Provider differences (OpenAI vs Anthropic vs Gemini formats)

## 7.2 Built-in / Server-side Tools
- Provider-hosted tools: web search, code execution, file search, computer use
- Hosted tools vs your own client-side tools
- Remote MCP tools via the API (preview of Section 17)

## 7.3 Tool Robustness
- **Tool validation**: validate arguments with Pydantic before executing
- **Tool errors**: return clear, actionable error messages the model can recover from
- **Tool retries**: which errors to retry automatically and which to hand back to the model
- **Tool timeouts**: per-tool time budgets
- **Tool permissions**: which user and agent may call which tool
- Truncating or paginating large results

## 7.4 Tool Design Principles
- **Small tools vs giant tools**: one clear purpose per tool, but not so many tools that the model gets confused
- **Tool descriptions**: what it does, when to use it, when NOT to use it, examples; this is prompt engineering
- **Input schemas**: descriptive names, enums, sensible defaults, required vs optional
- **Output schemas**: concise, relevant, human-readable IDs instead of UUID noise
- Tool naming and namespacing (`github_create_issue`, `crm_search_contacts`)
- Returning only what the model needs (keeps the context lean)
- **Idempotency**: safe to call twice
- **Read vs write tools**: separate them, and gate the write tools
- **Side-effect management**: dry-run mode, confirmation step, undo/compensation
- **Tool authorization**: user-scoped credentials, OAuth on behalf of the user
- How many tools are too many? Tool search and dynamic tool loading

## 7.5 Build Your Own Tools
| Tool | Key lesson |
|---|---|
| Calculator | Deterministic tools beat LLM math |
| Web search (Tavily, Brave, Exa, SerpAPI) | Result formatting and snippet size |
| Weather / REST API | External API errors and timeouts |
| Database query (read-only) | Parameterized queries, row limits |
| SQL generator + executor | Read-only DB user, query validation |
| File search / read | Path restrictions (no `../`) |
| PDF parser | Large outputs, chunking |
| Python execution | **Sandboxing required** (Docker, E2B, gVisor) |
| Email (send) | Write tool, needs confirmation |
| Calendar | OAuth, time zones |
| GitHub | Scoped tokens |
| CRM | Pagination, user-scoped access |

## 7.6 Testing Tools
- Unit-test each tool without an LLM
- Test tool selection: given a query, does the model pick the right tool?
- Test argument accuracy

---

## Example Flow
```
User: "What is 18% tip on $247.50, and will it rain in Kochi tomorrow?"
 ↓
LLM → parallel tool calls: calculator(expr="247.50*0.18"), weather(city="Kochi", day="tomorrow")
 ↓
Tool results returned
 ↓
LLM → final answer
```

## Project — Personal Assistant Agent
Tools: `calculator`, `web_search`, `weather`, `calendar` (read + create), `database` (notes), `email` (draft + send with confirmation)
- Tool registry built from your `BaseTool` class
- Write tools require an explicit user "yes"
- Tool-selection eval: 25 queries → expected tool(s)
- Log every tool call with arguments, duration and result size

## Common Pitfalls
- Vague descriptions ("gets data")
- Returning 50 KB of JSON to the model
- Letting the model execute arbitrary SQL or shell commands without a sandbox
- Crashing the agent on a tool exception instead of returning the error

## Definition of Done
- [ ] Tool-selection accuracy ≥ 90% on your eval set
- [ ] All write tools gated
- [ ] All tools have timeouts and validated inputs
