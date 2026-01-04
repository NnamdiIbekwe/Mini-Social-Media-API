import os
from fastapi import Depends
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.schemas.schema import UserCreate
from sqlalchemy.orm import Session
import bcrypt


load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL"),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

salt = bcrypt.gensalt()

response = {"message": "User created"}

def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit() # Commit the changes to the database
    db.refresh(new_user) # Refresh to get any DB-generated fields like the user ID
 
    return new_user
 