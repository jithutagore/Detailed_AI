import re
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints, field_validator

NamePart = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]

USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]+$")


class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    first_name: NamePart
    last_name: NamePart
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if not USERNAME_RE.match(value):
            raise ValueError("Username can only contain letters, numbers, and underscores")
        return value


class UserLogin(BaseModel):
    # Accepts either the email or the username in the same field.
    identifier: str = Field(min_length=1, max_length=255)
    password: str = Field(min_length=1, max_length=128)


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    username: str
    first_name: str
    last_name: str
    created_at: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserRead
