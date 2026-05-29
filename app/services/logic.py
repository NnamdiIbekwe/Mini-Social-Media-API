from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.core.security import decode_access_token



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")

async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    data = decode_access_token(token)
    if data is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == data["sub"]).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user