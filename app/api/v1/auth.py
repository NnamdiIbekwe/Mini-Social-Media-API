from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schema import Token, UserResponse
from app.models.users import User
from app.core.security import get_password_hashed, verify_password, create_access_token, decode_access_token
from app.api.depends import get_db, get_current_user


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/", response_model=UserResponse)
async def sign_up(user: User, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = get_password_hashed(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user}


@router.post("/login", response_model=Token)
async def log_in(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(password, user.hashed_password): #check this syntax later
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}