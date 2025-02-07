"""
This module defines the operations CRUD for Loans
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.loans import Loan
from schemas.loans import LoanCreate, LoanUpdate
from crud.material import get_material_status, update_material_status


def get_loan(db: Session, loan_id: int):
    """
    Retrieve a loan by its ID.
    """
    return db.query(Loan).filter(Loan.loan_id == loan_id).first()


def get_loans(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of loans with pagination.
    """
    return db.query(Loan).offset(skip).limit(limit).all()


def create_loan(db: Session, loan: LoanCreate):
    """
    Create a new loan.
    """
    material_status = get_material_status(db, loan.material_id)
    if material_status != "Available":
        raise HTTPException(status_code=400, detail="Material not available for loan")

    db_loan = Loan(
        user_id=loan.user_id,
        material_id=loan.material_id,
        loan_date=loan.loan_date,
        return_date=loan.return_date,
        loan_status=loan.loan_status,
    )
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)

    update_material_status(db, loan.material_id, "Not Available")

    return db_loan


def update_loan(db: Session, loan_id: int, loan: LoanUpdate):
    """
    Update an existing loan.
    """
    db_loan = db.query(Loan).filter(Loan.loan_id == loan_id).first()
    if db_loan is None:
        return None
    for key, value in loan.dict().items():
        setattr(db_loan, key, value)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def delete_loan(db: Session, loan_id: int):
    """
    Delete a loan by its ID.
    """
    db_loan = db.query(Loan).filter(Loan.loan_id == loan_id).first()
    if db_loan is None:
        return None
    db.delete(db_loan)
    db.commit()
    return db_loan
