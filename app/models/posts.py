from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship
from app.schemas import schema
from app import models

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    is_public = Column(Boolean, default=True)
    likes = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")

class Like(Base):
    __tablename__ = "likes"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)