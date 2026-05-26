from fastapi import FastAPI
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.core.config import settings
from app.db.base import Base
from app import models
import bcrypt

salt = bcrypt.gensalt()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer(tokenUrl="token")


def get_password_hashed(password: str) -> str: 
    return pwd_context.hash(password)

def verify_password(password: str, hash_password:str) -> bool:
    return pwd_context.verify(password, hash_password)

def create_access_token(data: dict, expires_delta: int / None = None) -> str:
    if expires_delta is none:
        expires_delta = datetime.now(timezone.utc) + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(expires_delta)
    payload = {"sub": data, "exp": expires_delta}
    token =jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

def decode_access_token(token: str) -> dict / None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return none

