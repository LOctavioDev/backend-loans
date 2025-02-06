import models.user
import schemas.user
from sqlalchemy.orm import Session
import models
import schemas
import bcrypt

def get_user(db: Session, id: int):
    return db.query(models.user.User).filter(models.user.User.id == id).first()


def get_user_by_username(db: Session, username: str):
    return (
        db.query(models.user.User).filter(models.user.User.username == username).first()
    )


def get_user_by_credentials(
    db: Session, username: str, email: str, phone_number: str, password: str
):
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
    return db.query(models.user.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.user.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.user.User(
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        user_type=user.user_type,
        username=user.username,
        email=user.email,
        password=hashed_password.decode('utf-8'),
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
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, id: int):
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
