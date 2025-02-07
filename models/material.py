"""
This module defines the Material model and related enums for the database.
"""

from sqlalchemy import Integer, Column, String, DateTime, Enum
from sqlalchemy.sql import func
from config.db import Base
import enum


class MaterialStatus(str, enum.Enum):
    Available = "Available"
    Borrowed = "Borrowed"
    UnderMaintenance = "Under Maintenance"
    NotAvailable = "Not Available"


class Material(Base):
    __tablename__ = "tbb_materials"

    material_id = Column(Integer, primary_key=True, autoincrement=True)
    material_type = Column(String(60))
    brand = Column(String(60))
    model = Column(String(60))
    status = Column(Enum(MaterialStatus))
    registration_date = Column(DateTime, default=func.now())
    update_date = Column(DateTime, default=func.now(), onupdate=func.now())
