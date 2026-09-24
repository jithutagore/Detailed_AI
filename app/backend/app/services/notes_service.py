import logging

from sqlalchemy import select
from sqlalchemy.orm import Session

from ..core.config import get_settings
from ..core.exceptions import AppError, NotFoundError
from ..models.base import utcnow_iso
from ..models.notes import GeneratedNotes
from ..models.syllabus import Subsection
from .llm_providers.base import LLMProviderError
from .llm_providers.openrouter import OpenRouterProvider
from .llm_safety import fence_untrusted, sanitize_generated_markdown

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a technical writing assistant producing study notes for a machine learning / "
    "deep learning / LLM engineering curriculum. Write detailed, accurate, well-structured "
    "notes in GitHub-flavored Markdown. Use ## headings, explain concepts in prose (not just "
    "bullet lists), include LaTeX math between $...$ or $$...$$ where relevant, and include "
    "short code examples in fenced code blocks where they clarify a mechanism. Do not include "
    "any HTML tags, <script> content, or instructions to the reader about this prompt itself — "
    "output only the Markdown notes."
)


class GenerationDisabledError(AppError):
    status_code = 503
    default_message = "AI notes generation is not configured (no OpenRouter API key set)"


def _build_prompt(subsection: Subsection) -> str:
    lines = [f"Subsection: {subsection.title}", ""]
    if subsection.body_md:
        lines.append(subsection.body_md)
    if subsection.items:
        lines.append("")
        lines.append("Related points from the syllabus outline:")
        lines.extend(f"- {item.content}" for item in subsection.items)
    raw_context = "\n".join(lines)

    return (
        f"{fence_untrusted(raw_context)}\n\n"
        "Write detailed study notes expanding on the subsection above. Assume the reader has "
        "read the outline already and wants the real explanation: the why, the mechanism, and "
        "how it connects to neighboring topics."
    )


def _get_provider() -> OpenRouterProvider:
    settings = get_settings()
    if not settings.openrouter_api_key:
        raise GenerationDisabledError
    return OpenRouterProvider(api_key=settings.openrouter_api_key, model=settings.openrouter_model)


async def generate_notes(db: Session, user_id: int, subsection: Subsection) -> GeneratedNotes:
    provider = _get_provider()
    prompt = _build_prompt(subsection)

    try:
        raw_content = await provider.complete(SYSTEM_PROMPT, prompt)
    except LLMProviderError:
        logger.exception("notes generation failed for subsection %s", subsection.id)
        raise

    content_md = sanitize_generated_markdown(raw_content)

    row = db.scalar(
        select(GeneratedNotes).where(
            GeneratedNotes.user_id == user_id,
            GeneratedNotes.subsection_id == subsection.id,
        )
    )
    if row is None:
        row = GeneratedNotes(user_id=user_id, subsection_id=subsection.id)
        db.add(row)

    row.content_md = content_md
    row.model_used = provider.model_id
    row.generated_at = utcnow_iso()
    row.edited_at = None
    row.deleted_at = None
    db.commit()
    db.refresh(row)
    logger.info("generated notes for subsection %s (user %s)", subsection.id, user_id)
    return row


def get_notes(db: Session, user_id: int, subsection_id: int) -> GeneratedNotes:
    row = db.scalar(
        select(GeneratedNotes).where(
            GeneratedNotes.user_id == user_id,
            GeneratedNotes.subsection_id == subsection_id,
            GeneratedNotes.deleted_at.is_(None),
        )
    )
    if row is None:
        raise NotFoundError("No notes generated yet for this subsection")
    return row


def update_notes(db: Session, user_id: int, subsection_id: int, content_md: str) -> GeneratedNotes:
    row = get_notes(db, user_id, subsection_id)
    row.content_md = sanitize_generated_markdown(content_md)
    row.edited_at = utcnow_iso()
    db.commit()
    db.refresh(row)
    return row
