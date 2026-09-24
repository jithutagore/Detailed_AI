from pydantic import BaseModel, ConfigDict


class SubsectionItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    kind: str
    content: str
    is_checkbox: bool


class SubsectionSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    kind: str
    number: str | None
    slug: str
    title: str
    status: str
    knowledge_level: int | None


class SubsectionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    kind: str
    number: str | None
    slug: str
    title: str
    body_md: str
    items: list[SubsectionItemRead]
    status: str
    knowledge_level: int | None


class SectionSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: str
    slug: str
    title: str
    level: str | None
    est_time: str | None
    status: str
    knowledge_level: int | None


class SectionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: str
    slug: str
    title: str
    goal: str | None
    level: str | None
    est_time: str | None
    intro_md: str | None
    subsections: list[SubsectionSummary]
    status: str
    knowledge_level: int | None


class TrackSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    description: str | None
    section_count: int
    completed_count: int


class TrackRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    description: str | None
    sections: list[SectionSummary]
