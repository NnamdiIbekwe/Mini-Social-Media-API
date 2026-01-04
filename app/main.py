from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form
from typing import Annotated
from app.schemas import schema
from app.db.base import Base, SessionLocal, engine, get_db, salt 
from app import models
#import bcrypt
from sqlalchemy.orm import Session

#Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini_Social_Media_API")

@app.post("/")
def register_user(
    #user: schema.UserCreate, 
    #db: Annotated[Session, Depends(get_db)],
    username: Annotated[str, Form()],
    password: Annotated[str, Form()], 
    #password: bcrypt.hashpw(Annotated[str, Form()].encode('utf-8'), salt).decode('utf-8'),
    email: Annotated[str, Form()],
    db: Session = Depends(get_db)
):
    #existing_user = db.query(models.User).filter(models.User.username == username).first()
    return response

@app.post("/users/")
async def Create_Post(
    username: Annotated[str, Form()],
    tilte: Annotated[str, Form()],
    content: Annotated[str, Form()],
    image: Annotated[UploadFile | None, File()] = None,
    db: Session = Depends(get_db),
):

    db.add(Post)
    db.commit()
    return {"message": "Post created"}
    #return{"username": username, "email": email}

#@app.post("/posts/")
#async def post():
#    return

@app.get("/posts/")
async def all_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

@app.get("/users/{username}/posts")
async def post_by_user():
    return

@app.post("/posts/{post_id}/like")
async def like_a_post(Post_id: int, User_id: int,):
    post = db.query(models.posts).filter(models.Post_id)
    post.likes += 1
    db.commit()
    return {"status": "Liked"}