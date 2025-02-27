"""
This module defines the Schema Loans
"""

from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class LoanStatus(str, Enum):
    Active = "Active"
    Returned = "Returned"
    Overdue = "Overdue"


class User(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class Material(BaseModel):
    material_type: str
    brand: str
    model: str

    class Config:
        orm_mode = True


class LoanBase(BaseModel):
    user_id: int
    material_id: int
    loan_date: datetime
    return_date: datetime
    loan_status: LoanStatus



class LoanCreate(BaseModel):
    user_id: int
    material_id: int
    loan_date: datetime
    return_date: datetime
    loan_status: LoanStatus



class LoanUpdate(LoanBase):
    pass


class LoanInDBBase(LoanBase):
    loan_id: int

    class Config:
        orm_mode = True


class Loan(LoanInDBBase):
    user: User
    material: Material

    class Config:
        orm_mode = True


class LoanInDB(LoanInDBBase):
    pass

class LoanSimple(BaseModel):
    loan_id: int
    user_id: int
    material_id: int
    loan_date: datetime
    return_date: datetime
    loan_status: LoanStatus

    class Config:
        orm_mode = True