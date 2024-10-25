from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, status, Path

from models import Users
from database import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext


router = APIRouter(
    prefix='/users',
    tags=['users']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['sha256_crypt']) 


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)
    

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed!!")
    
    return db.query(Users).filter(Users.id == user.get('id')).first()


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_Verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed!!")
    
    model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_Verification.password, model.hashed_password):
        raise HTTPException(status_code=401, detail="Password Error - failed!!")
    
    model.hashed_password = bcrypt_context.hash(user_Verification.new_password)
    db.add(model)
    db.commit()