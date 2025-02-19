from fastapi import APIRouter, Depends
from utils.jwt_config import get_current_user

protected_route = APIRouter(dependencies=[Depends(get_current_user)])
