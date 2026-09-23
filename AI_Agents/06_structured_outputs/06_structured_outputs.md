# 06 — Structured Outputs

> **Goal:** Make LLM output machine-readable and guaranteed-valid so the rest of your code can trust it.

**Level:** Foundation · **Time:** 1 week · **Prerequisites:** 01 (Pydantic), 05

---

## Learning Objectives
- Define output schemas with JSON Schema and Pydantic
- Use native structured-output features of providers
- Validate, retry and repair invalid outputs
- Design schemas that improve model accuracy

---

## 6.1 Schema Basics
- **JSON Schema**: types, `required`, `enum`, `anyOf`, `$defs`, `additionalProperties`
- **Pydantic models** → JSON Schema (`model_json_schema()`)
- Typed responses end to end

## 6.2 Ways to Get Structured Output
1. Prompt-only ("respond in JSON") — least reliable
2. JSON mode (valid JSON, but no schema guarantee)
3. **Native structured outputs / constrained decoding** (schema-guaranteed)
4. Tool calling as a structured-output mechanism
5. Libraries: **Instructor**, **Pydantic AI**, LangChain `with_structured_output`, Outlines (for local models)

## 6.3 Validation & Recovery
- Pydantic validation errors
- **Retry on invalid output**, feeding the error message back to the model
- Repair strategies (partial JSON parsing, re-asking only for missing fields)
- Semantic validation (valid JSON but wrong content, e.g. a date in the future)
- Maximum retry limits

## 6.4 Schema Design Patterns
- **Enum-based classification** (fixed labels instead of free text)
- **Nested structured responses**
- Optional fields vs required with `null`
- Put a `reasoning` field **before** the answer field so the model "thinks" first
- Confidence scores (and why raw LLM confidence is poorly calibrated)
- Lists of entities (extraction)
- Field descriptions as instructions (`Field(description=...)`)
- Keep schemas flat and small when you can

## 6.5 Common Use Cases
- Classification (intent, sentiment, priority, routing)
- Information extraction (invoices, resumes, emails)
- Data normalization
- Generating structured plans for agents
- LLM-as-judge outputs (score + rationale)

## 6.6 Streaming Structured Output
- Partial object streaming
- Showing fields in the UI as they arrive

---

## Example

```python
from enum import Enum
from pydantic import BaseModel, Field

class Intent(str, Enum):
    payment_failure = "payment_failure"
    refund_request = "refund_request"
    account_access = "account_access"
    other = "other"

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class CustomerRequest(BaseModel):
    reasoning: str = Field(description="Brief reasoning before classifying")
    intent: Intent
    priority: Priority
    requires_human: bool
    entities: list[str] = Field(default_factory=list, description="Order IDs, amounts, dates")
```

**Input:** `"My payment failed twice."`

**Output:**
```json
{
  "reasoning": "Repeated payment failure blocks purchase; urgent.",
  "intent": "payment_failure",
  "priority": "high",
  "requires_human": true,
  "entities": []
}
```

---

## Project — Customer Request Classifier
- FastAPI endpoint `POST /classify`
- Pydantic schema with enums and nested entities
- Native structured output + retry-on-validation-error fallback
- **Eval set of 30 labeled messages**, reporting accuracy per intent and a confusion matrix
- Compare 2 models on accuracy vs cost

## Common Pitfalls
- Free-text labels that drift ("Payment Failure", "payment-failed")
- Huge deeply-nested schemas that lower accuracy
- Trusting valid JSON as correct data

## Definition of Done
- [ ] 100% schema-valid responses on the eval set
- [ ] Accuracy measured and reported
- [ ] **Start of the habit:** this is your first eval set; keep one for every project from here on
