from pydantic import BaseModel



class UserCreate(BaseModel):
    username: str
    password: str
    #password: bcrypt.hashpw(Annotated[str, Form()].encode('utf-8'), salt).decode('utf-8')
    email: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    image_url: str | None
    likes: int
    username: str