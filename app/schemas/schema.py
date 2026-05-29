from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

class UserCreate(User):
    hashed_password: str

class PostCreate(BaseModel):
    content: str
    image_url: str | UploadFile | None
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
    timestamp: str

    class Config:
        from_attributes = True

class PostResponse(Post):
    pass

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

Class TokenData(BaseModel):
    username: str | None = None

