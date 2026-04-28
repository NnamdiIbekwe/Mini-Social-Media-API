from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form
from typing import Annotated
from app.schemas import schema
from app.db.base import Base, SessionLocal, engine, get_db, salt 
from app import models
#import bcrypt
from sqlalchemy.orm import Session
from app.api.v1 import post as post_router
from app.api.v1 import user as user_router
from app.core.security import get_password_harsh

#Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini_Social_Media_API")    

@app.get("/")
async def root():
    return {"message": "Welcome to the Mini Social Media API!"}

app.include_router(post_router.router, prefix="/api/v1", tags=["posts"])
app.include_router(user_router.router, prefix="/api/v1", tags=["users"])



# # @app.post("/")
# # def register_user(user: schema.UserCreate, db:session = Depends(get_db)):

# @app.post("/users/")
# # async def Create_Post(
# #     username: Annotated[str, Form()],
# #     tilte: Annotated[str, Form()],
# #     content: Annotated[str, Form()],
# #     image: Annotated[UploadFile | None, File()] = None,
# #     db: Session = Depends(get_db),
# # ):

# #     db.add(Post)
# #     db.commit()
# #     return {"message": "Post created"}
#     #return{"username": username, "email": email}

# #@app.post("/posts/")
# #async def post():
# #    return

# @app.get("/posts/")
# async def all_posts(db: Session = Depends(get_db)):
#     return db.query(models.Post).all()

# @app.get("/users/{username}/posts")
# async def post_by_user():
#     return

# @app.post("/posts/{post_id}/like")
# async def like_a_post(Post_id: int, User_id: int,):
#     post = db.query(models.posts).filter(models.Post_id)
#     post.likes += 1
#     db.commit()
#     return {"status": "Liked"}