"""
This module defines the operations CRUD for Users
"""

from sqlalchemy.orm import Session
import bcrypt
import models.user
import schemas.user
import models
import schemas


def get_user(db: Session, id: int):
    """
    Retrive a user by its ID.
    """
    return db.query(models.user.User).filter(models.user.User.id == id).first()


def get_user_by_username(db: Session, username: str):
    """
    Retrieve a user by its username.
    """
    return (
        db.query(models.user.User).filter(models.user.User.username == username).first()
    )


def get_user_by_credentials(
    db: Session, username: str, email: str, phone_number: str, password: str
):
    """
    Retrieve a user by its credentials.
    """
    return (
        db.query(models.user.User)
        .filter(
            (models.user.User.username == username)
            | (models.user.User.email == email)
            | (models.user.User.phone_number == phone_number),
            models.user.User.password == password,
        )
        .first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of users.
    """
    return db.query(models.user.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.user.UserCreate):
    """
    Create a new user.
    """
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    db_user = models.user.User(
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        user_type=user.user_type,
        username=user.username,
        email=user.email,
        password=hashed_password.decode("utf-8"),
        phone_number=user.phone_number,
        status=user.status,
        registration_date=user.registration_date,
        update_date=user.update_date,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, id: int, user: schemas.user.UserUpdate):
    """
    Update an existing user.
    """
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, id: int):
    """
    Delete a user by its ID.
    """
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.user.User).filter(models.user.User.email == email).first()

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def authenticate_user(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email=email)
    if not db_user:
        return None
    if not verify_password(password, db_user.password):
        return None
    return db_user