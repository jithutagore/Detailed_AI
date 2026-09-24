from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimestampMixin
from .base import utcnow_iso


class GeneratedNotes(TimestampMixin, Base):
    __tablename__ = "generated_notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    subsection_id: Mapped[int] = mapped_column(ForeignKey("subsections.id"), nullable=False)
    content_md: Mapped[str] = mapped_column(Text, nullable=False)
    model_used: Mapped[str] = mapped_column(String(255), nullable=False)
    generated_at: Mapped[str] = mapped_column(default=utcnow_iso)
    edited_at: Mapped[str | None] = mapped_column(default=None)
