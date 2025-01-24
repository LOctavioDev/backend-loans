from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    last_name: str
    gender: Gender
    roles: List[Role]


class UpdateUser(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    roles: Optional[List[str]]
