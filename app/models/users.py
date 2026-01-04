from sqlalchemy import Boolean, Column, Integer, String
from app.db.base import Base
from sqlalchemy.orm import relationship
from app.schemas import schema


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(70), unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    harshed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    posts = relationship("Post", back_populates="user")
