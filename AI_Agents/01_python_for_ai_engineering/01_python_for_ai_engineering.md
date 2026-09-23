# 01 — Python for AI Engineering

> **Goal:** Write clean, typed, async Python that talks to APIs, validates data and is easy to test. Almost every agent framework is Python-first.

**Level:** Foundation · **Time:** 2–3 weeks · **Prerequisites:** Basic programming

---

## Learning Objectives
By the end of this section you can:
- Write modern Python 3.11+ with type hints, dataclasses and Pydantic models
- Use `async`/`await` to call many APIs concurrently
- Structure a project with virtual environments, dependency management, logging and config
- Use Git and GitHub for version control and collaboration

---

## 1.1 Language Core
- Python 3.11 / 3.12 / 3.13 features (faster runtime, better error messages, `match` statements)
- Data types: `list`, `dict`, `set`, `tuple`, comprehensions
- Functions: `*args`, `**kwargs`, default args, keyword-only args
- Closures and higher-order functions
- **Decorators**: writing your own (timing, retry, logging), `functools.wraps`, decorators with arguments
- Generators and `yield` (you'll need these for streaming LLM output)
- Context managers (`with`, `contextlib.contextmanager`, `async with`)
- Iterators and `itertools`

## 1.2 Object-Oriented Python
- Classes, instances, `__init__`, `__repr__`, `__eq__`
- Inheritance vs composition
- Abstract base classes (`abc.ABC`) and building a `BaseTool` interface
- `Protocol` for structural typing (duck typing with type safety)
- `@property`, `@classmethod`, `@staticmethod`
- Enums (`enum.Enum`, `StrEnum`)

## 1.3 Type Hints & Data Modeling
- Basic hints: `int`, `str`, `list[str]`, `dict[str, Any]`, `Optional`, `X | None`
- `Literal`, `TypedDict`, `Annotated`, `Generic`, `TypeVar`
- `Callable` and `Awaitable` types
- `dataclasses`: `field`, `frozen`, `slots`, `asdict`
- **Pydantic v2** (critical for agents):
  - `BaseModel`, `Field`, validators (`field_validator`, `model_validator`)
  - `model_dump`, `model_dump_json`, `model_validate`, `model_json_schema()`
  - Nested models, discriminated unions
  - `pydantic-settings` for config and environment variables
- Static checking with `mypy` or `pyright`

## 1.4 Async Programming
- Event loop concepts: concurrency vs parallelism
- `async def`, `await`, `asyncio.run`
- `asyncio.gather`, `asyncio.TaskGroup` (3.11+), `asyncio.wait_for` (timeouts)
- `asyncio.Semaphore` for limiting concurrent API calls
- `asyncio.Queue` for producer/consumer pipelines
- Async generators (`async for`) for streaming tokens
- Mixing sync and async (`asyncio.to_thread`)
- Common pitfalls: blocking calls inside async code, forgotten `await`

## 1.5 HTTP, APIs & JSON
- HTTP basics: methods, status codes, headers, auth headers
- REST API concepts
- `httpx` (sync and async) and `requests`
- Timeouts, retries (`tenacity`), connection pooling
- JSON: `json.loads`/`dumps`, serializing custom types
- Server-Sent Events (SSE), the streaming format most LLM APIs use

## 1.6 Configuration, Logging & Errors
- Environment variables, `.env` files, `python-dotenv`
- Never commit secrets: `.gitignore`, secret scanning
- `logging` module: levels, handlers, formatters
- Structured logging (`structlog` or JSON logs)
- Exception handling: `try/except/else/finally`, custom exception hierarchies
- Exception groups (`except*`) with `TaskGroup`

## 1.7 Tooling & Packaging
- Virtual environments: `venv`, **`uv`** (recommended, fast), `poetry`
- `pyproject.toml` and dependency pinning
- Project layout (`src/` layout, packages, `__init__.py`)
- Linting and formatting with **`ruff`**
- Testing with **`pytest`**: fixtures, parametrize, `pytest-asyncio`, mocking (`unittest.mock`, `respx` for httpx)
- Jupyter notebooks for experimentation, and when to move code out of them

## 1.8 Git & GitHub
- `init`, `add`, `commit`, `branch`, `merge`, `rebase`, `stash`
- Pull requests, code review, `.gitignore`
- GitHub Actions basics (run tests and lint on every push)
- Conventional commit messages

---

## Hands-on Exercises
1. Write a `@retry(max_attempts=3, backoff=2)` decorator that works on both sync and async functions.
2. Fetch 50 URLs concurrently with `httpx.AsyncClient`, capped at 5 concurrent requests with a semaphore.
3. Model an API response with nested Pydantic models and reject invalid payloads.
4. Build a `BaseTool` abstract class with `name`, `description`, `input_model` and `run()`. You'll reuse it in Section 07.
5. Write pytest tests with a mocked HTTP client.

## Mini Project — Async API Aggregator CLI
A CLI that takes a city name, calls 3 public APIs concurrently (weather, time zone, country info), validates each response with Pydantic, logs structured output, handles timeouts and failures gracefully, and prints a combined report.

## Common Pitfalls
- Calling blocking `requests` inside async code
- Using `dict` everywhere instead of typed models
- Hard-coded API keys
- No timeouts on HTTP calls

## Definition of Done
- [ ] Project uses `uv`/`venv`, `pyproject.toml`, `ruff` and `pytest`
- [ ] All public functions have type hints
- [ ] At least 5 passing tests, including one async test
- [ ] Code on GitHub with CI running tests
