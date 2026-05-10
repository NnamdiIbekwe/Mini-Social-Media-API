from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.db.base import get_db
from app.core.security import get_password_hashed, verify_password
from app.models.users import User
from app.models.posts import Post

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schema.UserResponse)
async def create_new_user(user: schema.UserCreate, db: Session = Depends(get_db)):
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
    return new_user


@router.post("/login")
async def log_in(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(password, user.hashed_password): #check this syntax later
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    return {"message": "Login successful"}

@router.get("/{username}", response_model=schema.UserResponse)
async def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[schema.UserResponse])
async def all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{username}/posts")
async def get_user_posts(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts

