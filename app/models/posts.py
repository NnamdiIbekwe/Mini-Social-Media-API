from sqlalchemy import Boolean, Column, Integer, String
from app.db.base import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    image_url = Column(String, )