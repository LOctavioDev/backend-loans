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


class LoanBase(BaseModel):
    user_id: int
    material_id: int
    loan_date: datetime
    return_date: datetime
    loan_status: LoanStatus


class LoanCreate(LoanBase):
    pass


class LoanUpdate(LoanBase):
    pass


class LoanInDBBase(LoanBase):
    loan_id: int

    class Config:
        from_attributes: True


class Loan(LoanInDBBase):
    pass


class LoanInDB(LoanInDBBase):
    pass
