from pydantic import BaseModel, ConfigDict, Field


class NotesRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subsection_id: int
    content_md: str
    model_used: str
    generated_at: str
    edited_at: str | None


class NotesUpdate(BaseModel):
    content_md: str = Field(min_length=1, max_length=200_000)
