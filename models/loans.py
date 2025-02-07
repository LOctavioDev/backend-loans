"""
This module defines the Loans model and related enums for the database.
"""

from sqlalchemy import Integer, Column, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from config.db import Base
import enum


class LoanStatus(str, enum.Enum):
    Active = "Active"
    Returned = "Returned"
    Overdue = "Overdue"


class Loan(Base):
    __tablename__ = "tbb_loans"

    loan_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("tbb_users.id"))
    material_id = Column(Integer, ForeignKey("tbb_materials.material_id"))
    loan_date = Column(DateTime, default=func.now())
    return_date = Column(DateTime)
    loan_status = Column(Enum(LoanStatus))
