"""
This module defines the Schema Material
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class MaterialBase(BaseModel):
    material_type: str
    brand: str
    model: str
    status: str
    registration_date: Optional[datetime] = None
    update_date: Optional[datetime] = None


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(MaterialBase):
    pass


class Material(MaterialBase):
    material_id: int

    class Config:
        from_attributes = True
