from datetime import datetime, timezone

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def utcnow_iso() -> str:
    # Matches the format the syllabus importer writes: strftime('%Y-%m-%dT%H:%M:%fZ', 'now').
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + f"{datetime.now(timezone.utc).microsecond // 1000:03d}Z"


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    """created_at / updated_at / deleted_at on every table, matching db/schema.sql."""

    created_at: Mapped[str] = mapped_column(default=utcnow_iso)
    updated_at: Mapped[str] = mapped_column(default=utcnow_iso, onupdate=utcnow_iso)
    deleted_at: Mapped[str | None] = mapped_column(default=None)
