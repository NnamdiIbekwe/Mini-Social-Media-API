from fastapi import FastAPI
from app.db.base import Base, SessionLocal, engine, get_db, salt
from app import models
import bcrypt

salt = bcrypt.gensalt()


async def get_password_harsh(password: str) -> str: 
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
