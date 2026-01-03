from sqlalchemy import Boolean, Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(70), unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    harshed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
