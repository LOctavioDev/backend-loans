from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import crud.users
import config.db
from utils.jwt_config import get_token

auth = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth.post("/login", tags=["Auth"])
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = crud.users.authenticate_user(db, email=request.email, password=request.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    token = get_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}