# 19 — Multimodal, Browser & Computer-Use Agents  *(NEW section)*

> **Goal:** Build agents that see (images, documents, screens), browse the web and operate software interfaces.
> **Why added:** Vision, document understanding, browser automation and computer use are major agent categories that the original syllabus missed.

**Level:** Advanced · **Time:** 1–2 weeks · **Prerequisites:** 07, 08, 21 (read the security basics first)

---

## Learning Objectives
- Use vision-capable models for images, charts, and documents
- Build browser-automation agents
- Understand computer-use agents and how to run them safely

---

## 19.1 Multimodal Inputs
- Image inputs (base64, URLs), resolution and token cost
- PDF / document inputs sent directly to models
- Charts, tables, diagrams, screenshots, handwriting
- Audio and video inputs (overview; voice is covered in Section 28)
- Image generation as a tool (overview)

## 19.2 Document Intelligence
- Invoice, receipt, ID and form extraction with a vision model + structured output
- Vision models vs OCR pipelines: accuracy, cost, when to combine them
- Validation of extracted fields
- Bounding boxes and grounding (where the answer came from on the page)

## 19.3 Browser Agents
- Classic automation: **Playwright**, Selenium
- DOM-based vs screenshot-based vs accessibility-tree-based agents
- Frameworks: **Browser Use**, Stagehand, Playwright MCP
- Hosted browsers: Browserbase and similar
- Handling logins, CAPTCHAs (don't bypass them), pop-ups, dynamic pages
- Web scraping ethics, robots.txt, terms of service

## 19.4 Computer-Use Agents
- Screenshot → action (click, type, scroll) loop
- Provider computer-use tools (Anthropic computer use, OpenAI computer-use agent)
- Running in isolated VMs or containers **only**
- Coordinate accuracy, latency and cost
- When to prefer APIs over UI automation (almost always, when an API exists)

## 19.5 Safety for Acting Agents
- Prompt injection from web pages and screen content
- Confirming irreversible actions (purchases, sending, deleting)
- Credential handling (never type real passwords from context)
- Domain allowlists
- Session recording for audit

---

## Hands-on Exercises
1. Extract structured data from 20 varied invoices with a vision model; measure field accuracy.
2. Build a Playwright tool that returns a cleaned accessibility tree instead of raw HTML.
3. Run a computer-use demo inside a Docker VM and complete a 5-step form-filling task.

## Project — Web Research & Form-Filling Agent
- Browses to gather product information from 3 sites
- Extracts a structured comparison table (including a vision pass over screenshots)
- Fills a sandbox form with the result, pausing for human approval before submit
- Runs fully sandboxed, with a domain allowlist

## Definition of Done
- [ ] Runs in isolation
- [ ] All irreversible actions require approval
- [ ] Injection test (a malicious page) is handled safely
