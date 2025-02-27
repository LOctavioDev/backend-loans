"""
This module defines the operations CRUD for Loans
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.loans import Loan
from models.user import User
from models.material import Material
from schemas.loans import LoanCreate, LoanUpdate
from crud.material import get_material_status, update_material_status


def get_loan(db: Session, loan_id: int):
    """
    Retrieve a loan by its ID.
    """
    loan = db.query(Loan).filter(Loan.loan_id == loan_id).first()
    if loan is None:
        return None

    user = db.query(User).filter(User.id == loan.user_id).first()
    material = (
        db.query(Material).filter(Material.material_id == loan.material_id).first()
    )

    return {
        "loan_id": loan.loan_id,
        "user_id": loan.user_id,
        "material_id": loan.material_id,
        "user": {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
        "material": {
            "material_type": material.material_type,
            "brand": material.brand,
            "model": material.model,
        },
        "loan_date": loan.loan_date,
        "return_date": loan.return_date,
        "loan_status": loan.loan_status,
    }


def get_loans(db: Session, skip: int = 0):
    loans = db.query(Loan).offset(skip).all()
    result = []

    for loan in loans:
        user = db.query(User).filter(User.id == loan.user_id).first()
        material = (
            db.query(Material).filter(Material.material_id == loan.material_id).first()
        )

        result.append(
            {
                "loan_id": loan.loan_id,
                "user_id": loan.user_id,
                "material_id": loan.material_id,
                "user": {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                },
                "material": {
                    "material_type": material.material_type,
                    "brand": material.brand,
                    "model": material.model,
                },
                "loan_date": loan.loan_date,
                "return_date": loan.return_date,
                "loan_status": loan.loan_status,
            }
        )

    return result


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
