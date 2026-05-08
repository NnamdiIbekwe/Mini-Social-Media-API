from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class PostCreate(BaseModel):
    title: str
    content: str
    image_url: str | None

class Post(BaseModel):
    id: int
    title: str
    content: str
    image_url: str | None
    likes: int
    username: str
    timestamp: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    image_url: str | None
    likes: int
    username: str
    timestamp: str

    class Config:
        from_attributes = True

