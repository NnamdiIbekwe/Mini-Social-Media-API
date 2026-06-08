from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.core.config import settings
import bcrypt



def get_password_hashed(password: str) -> str: 
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(password: str, hash_password:str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hash_password.encode("utf-8"))

def create_access_token(data: dict, expires_delta: int | None = None) -> str:
    if expires_delta is None:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    else:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    
    token =jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

def decode_access_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None

