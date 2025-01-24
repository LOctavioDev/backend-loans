"""
Project CRUD practice with FastAPI
"""

from fastapi import FastAPI
from fastapi import HTTPException
from typing import List
from uuid import uuid4, UUID
from models import Gender, Role, User, UpdateUser


db: List[User] = [
    User(
        id=uuid4(),
        name="Marco",
        last_name="Ortiz Ramirez",
        gender=Gender.MALE,
        roles=[Role.ADMIN],
    ),
    User(
        id=uuid4(),
        name="Abdiel",
        last_name="Fosado Animas",
        gender=Gender.MALE,
        roles=[Role.USER],
    ),
    User(
        id=uuid4(),
        name="Rubi",
        last_name="Lobato",
        gender=Gender.FEMALE,
        roles=[Role.USER],
    ),
    User(
        id=uuid4(),
        name="Jaime",
        last_name="Vazquez Santiago",
        gender=Gender.OTHER,
        roles=[Role.USER],
    ),
]

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome FastAPI"}


@app.get("/users", response_model=List[User])
async def get_users():
    return db


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=User)
async def create_user(user: User):
    db.append(user)
    return user


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: UUID, user: UpdateUser):
    for db_user in db:
        if db_user.id == user_id:
            if user.name is not None:
                db_user.name = user.name
            if user.last_name is not None:
                db_user.last_name = user.last_name
            if user.gender is not None:
                db_user.gender = user.gender
            if user.roles is not None:
                db_user.roles = user.roles
            return db_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

