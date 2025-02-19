"""
This module defines the Routes Material
"""

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.material
import config.db
import models.material
import schemas.material
from .base_url import protected_route

models.material.Base.metadata.create_all(bind=config.db.engine)


def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@protected_route.get(
    "/materials", response_model=List[schemas.material.Material], tags=["Materials"]
)
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_materials = crud.material.get_materials(db=db, skip=skip, limit=limit)
    return db_materials


@protected_route.get(
    "/material/{id}", response_model=schemas.material.Material, tags=["Materials"]
)
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.get_material(db=db, material_id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material


@protected_route.post(
    "/materials", response_model=schemas.material.Material, tags=["Materials"]
)
def create_material(
    material: schemas.material.MaterialCreate, db: Session = Depends(get_db)
):
    existing_material = crud.material.get_material_by_details(
        db=db,
        material_type=material.material_type,
        brand=material.brand,
        model=material.model,
    )
    if existing_material:
        raise HTTPException(status_code=400, detail="Material already exists")

    return crud.material.create_material(db=db, material=material)


@protected_route.put(
    "/material/{id}", response_model=schemas.material.Material, tags=["Materials"]
)
async def update_material(
    id: int, material: schemas.material.MaterialUpdate, db: Session = Depends(get_db)
):
    db_material = crud.material.update_material(
        db=db, material_id=id, material=material
    )
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material


@protected_route.delete(
    "/material/{id}", response_model=schemas.material.Material, tags=["Materials"]
)
async def delete_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.delete_material(db=db, material_id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
