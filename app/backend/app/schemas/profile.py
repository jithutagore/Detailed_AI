from pydantic import BaseModel, ConfigDict

from .user import NamePart


class ProfileUpdate(BaseModel):
    first_name: NamePart
    last_name: NamePart


class ProfileRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    username: str
    first_name: str
    last_name: str
