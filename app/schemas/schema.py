from pydantic import BaseModel
from fastapi import UploadFile


class User(BaseModel):
    username: str
    email: str
    

class UserCreate(User):
    password: str

class PostCreate(BaseModel):
    content: str
    image_url: str | None
    is_public: bool = True
    user_id: int

class Post(BaseModel):
    id: int
    title: str
    content: str
    image_url: str | None
    likes: int = 0
    username: str
    timestamp: str

class UserResponse(User):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class PostResponse(Post):
    class Config:
        from_attributes = True

class LikeResponse(BaseModel):
    user_id: int
    post_id: int
    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

