"""
This module defines the Routes Loans
"""

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.loans
import crud.material
import config.db
import models.loans
import schemas.loans

from .base_url import protected_route


models.loans.Base.metadata.create_all(bind=config.db.engine)


def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@protected_route.get("/loans", response_model=List[schemas.loans.Loan], tags=["Loans"])
async def read_loans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_loans = crud.loans.get_loans(db=db, skip=skip)
    return db_loans


@protected_route.get("/loan/{id}", response_model=schemas.loans.Loan, tags=["Loans"])
async def read_loan(id: int, db: Session = Depends(get_db)):
    db_loan = crud.loans.get_loan(db=db, loan_id=id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@protected_route.post("/loans", response_model=dict, tags=["Loans"])
def create_loan(loan: schemas.loans.LoanCreate, db: Session = Depends(get_db)):
    material_status = crud.material.get_material_status(db, loan.material_id)
    if material_status != "Available":
        raise HTTPException(status_code=400, detail="Material not available for loan")
    crud.loans.create_loan(db=db, loan=loan)
    return {"message": "Loan created successfully"}


@protected_route.put("/loan/{id}", response_model=schemas.loans.Loan, tags=["Loans"])
async def update_loan(
    id: int, loan: schemas.loans.LoanUpdate, db: Session = Depends(get_db)
):
    db_loan = crud.loans.update_loan(db=db, loan_id=id, loan=loan)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@protected_route.delete("/loan/{id}", response_model=schemas.loans.Loan, tags=["Loans"])
async def delete_loan(id: int, db: Session = Depends(get_db)):
    db_loan = crud.loans.delete_loan(db=db, loan_id=id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan
