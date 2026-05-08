from fastapi import FastAPI
from app.db.base import Base
from app import models
import bcrypt

salt = bcrypt.gensalt()


def get_password_hashed(password: str) -> str: 
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(password: str, hash_password:str) -> bool:
    return bcrypt.checkpw(password.encode(), hash_password.encode())
