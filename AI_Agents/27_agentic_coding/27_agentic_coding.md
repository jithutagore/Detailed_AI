# 27 — Agentic Coding

> **Goal:** Understand and build agents that work inside software repositories: read, plan, edit, test, debug and open pull requests. Also learn to *use* coding agents effectively.

**Level:** Specialization · **Time:** 2 weeks · **Prerequisites:** 07, 08, 12, 21 (sandboxing)

---

## Learning Objectives
- Build a coding agent with file, search, shell and test tools
- Apply repository understanding techniques (repo maps, AST, code search)
- Run an edit–test–fix loop safely in a sandbox
- Use existing coding agents productively in your own workflow

---

## 27.1 Using Coding Agents (practitioner skills)
- Claude Code, OpenAI Codex, GitHub Copilot agent mode, Cursor, Windsurf, Gemini CLI, Aider, Cline, OpenHands
- Project instruction files (`CLAUDE.md`, `AGENTS.md`, rules files)
- Custom commands, skills, hooks, sub-agents, MCP servers for coding agents
- Workflows: explore → plan → implement → test → commit; test-driven prompting
- Reviewing AI-written code critically
- Headless / CI usage (agents fixing issues from GitHub Actions)

## 27.2 Tools a Coding Agent Needs
- **Git** (status, diff, branch, commit)
- **GitHub** (issues, PRs, review comments; `gh` CLI or API)
- **File system** (read, write, edit with exact string replace or diffs/patches)
- **Shell** (sandboxed command execution)
- **Code search** (ripgrep, glob)
- **AST** tools (tree-sitter)
- **Test execution** (pytest, jest)
- **Linters / type checkers** (ruff, mypy, eslint, tsc)
- **Build systems** (make, npm, uv, gradle)
- LSP integration (go-to-definition, references, diagnostics)

## 27.3 Architecture
```
User / Issue
 ↓
Coding Agent
 ↓
Repository Analysis (structure, conventions, relevant files)
 ↓
Plan
 ↓
Modify Code (small, reviewable edits)
 ↓
Run Tests / Lint / Type-check
 ↓
Analyze Failure ── fail ──→ Fix → (loop, bounded)
 ↓ pass
Pull Request (description, test evidence)
```

## 27.4 Repository Understanding
- **Repository mapping** (Aider-style repo map: files + key symbols)
- **AST analysis** with tree-sitter
- **Dependency graphs** (imports, call graphs)
- **Code embeddings** and **semantic code search**
- Agentic search (grep/read as needed) vs index-based retrieval, and their trade-offs
- Reading project conventions before editing

## 27.5 Edit Strategies
- Whole-file rewrite vs search/replace blocks vs unified diffs
- Applying edits reliably (fuzzy matching, validation)
- Minimal diffs, keeping the existing style

## 27.6 Advanced Topics
- **Test generation**
- **Automated debugging** (reproduce → hypothesize → instrument → fix)
- **PR review agents**
- Issue triage agents
- Migrations and large refactors (parallel sub-agents per module)
- Security: sandboxed execution, network restrictions, secret protection, no `rm -rf` outside the workspace
- Benchmarks: SWE-bench (Verified), Terminal-Bench, and what they measure

---

## Project — Mini SWE Agent
- Input: a GitHub issue URL on a small repo you control
- Clones into a Docker sandbox, maps the repo, plans, edits, runs tests, iterates (max 5 loops)
- Opens a PR with a summary and test output
- Separate **PR review agent** that comments on diffs
- **Eval:** 15 seeded bugs in a sample repo; measure the fix rate and number of attempts

## Definition of Done
- [ ] Runs entirely sandboxed
- [ ] Fix rate measured
- [ ] You use a coding agent daily, with a project instruction file you've written
