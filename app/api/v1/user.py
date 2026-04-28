from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import schema
from app.db.base import get_db
from app.core.security import get_password_harsh
from app import models

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
async def create_new_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_harsh(user.password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{username}")
async def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user