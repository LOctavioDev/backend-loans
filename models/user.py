"""
This module defines the User model and related enums for the database.
"""

from sqlalchemy import Integer, Column, String, DateTime, Enum
from sqlalchemy.sql import func
from config.db import Base
import enum


class MyStatus(str, enum.Enum):
    Active = "Active"
    Inactive = "Inactive"
    Blocked = "Blocked"
    Suspended = "Suspended"


class UserType(str, enum.Enum):
    Student = "Student"
    Teacher = "Teacher"
    Secretary = "Secretary"
    LabTechnician = "LabTechnician"
    Executive = "Executive"
    Administrative = "Administrative"


class User(Base):
    __tablename__ = "tbb_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(60))
    last_name = Column(String(60))
    middle_name = Column(String(60))
    user_type = Column(Enum(UserType))
    username = Column(String(60))
    email = Column(String(100))
    password = Column(String(100))
    phone_number = Column(String(20))
    status = Column(Enum(MyStatus))
    registration_date = Column(DateTime, default=func.now())
    update_date = Column(DateTime, default=func.now(), onupdate=func.now())
