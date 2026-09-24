from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Status = Literal["not_started", "in_progress", "completed", "skipped", "needs_revisit"]


class StatusUpdate(BaseModel):
    status: Status
    knowledge_level: int | None = Field(default=None, ge=1, le=5)


class SectionStatusRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    section_id: int
    status: Status
    knowledge_level: int | None
    updated_at: str


class SubsectionStatusRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    subsection_id: int
    status: Status
    knowledge_level: int | None
    updated_at: str
