"""
This module defines the operations CRUD for Material
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas.material
import models.material


def get_material(db: Session, material_id: int):
    """
    Retrieve a material by its ID.
    """
    return (
        db.query(models.material.Material)
        .filter(models.material.Material.material_id == material_id)
        .first()
    )


def get_material_status(db: Session, material_id: int):
    """
    Retrieve the status of a material by its ID.
    """
    material = (
        db.query(models.material.Material)
        .filter(models.material.Material.material_id == material_id)
        .first()
    )
    if material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return material.status


def update_material_status(db: Session, material_id: int, status: str):
    """
    Update the status of a material by its ID.
    """
    material = (
        db.query(models.material.Material)
        .filter(models.material.Material.material_id == material_id)
        .first()
    )
    if material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    material.status = status
    db.commit()
    db.refresh(material)
    return material


def get_material_by_details(db: Session, material_type: str, brand: str, model: str):
    """
    Retrieve a material by its details.
    """
    return (
        db.query(models.material.Material)
        .filter(
            models.material.Material.material_type == material_type,
            models.material.Material.brand == brand,
            models.material.Material.model == model,
        )
        .first()
    )


def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of materials with pagination.
    """
    return db.query(models.material.Material).offset(skip).limit(limit).all()


def create_material(db: Session, material: schemas.material.MaterialCreate):
    """
    Create a new material.
    """
    db_material = models.material.Material(
        material_type=material.material_type,
        brand=material.brand,
        model=material.model,
        status=material.status,
        registration_date=material.registration_date,
        update_date=material.update_date,
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def update_material(
    db: Session, material_id: int, material: schemas.material.MaterialUpdate
):
    """
    Update an existing material.
    """
    db_material = (
        db.query(models.material.Material)
        .filter(models.material.Material.material_id == material_id)
        .first()
    )
    if db_material:
        for var, value in vars(material).items():
            setattr(db_material, var, value) if value else None
        db.commit()
        db.refresh(db_material)
    return db_material


def delete_material(db: Session, material_id: int):
    """
    Delete a material by its ID.
    """
    db_material = (
        db.query(models.material.Material)
        .filter(models.material.Material.material_id == material_id)
        .first()
    )
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
