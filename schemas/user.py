"""
This module defines the Schema User
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    user_type: str
    username: str
    email: str
    password: str
    phone_number: str
    status: str
    registration_date: datetime = None
    update_date: datetime = None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str
    phone_number: Optional[str] = None
