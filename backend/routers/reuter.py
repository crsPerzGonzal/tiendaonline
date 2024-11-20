from fastapi import APIRouter
from fastapi import Depends 
from backend import Crud as crud
from backend.core.confi import get_db
from sqlalchemy.orm import Session
from backend.schemas.response import UserSchema, Response

router = APIRouter


