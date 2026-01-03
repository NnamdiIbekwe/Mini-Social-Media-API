from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from typing import Annotated


app = FastAPI()

@app.post("/users/")
async def user(
    username: Annotated[str, Form()],
    email: Annotated[str, Form()]
):

    return{"username": username, "email": email}

@app.post("/posts/")
async def post():
    return

@app.get("/posts/")
async def all_posts():
    return

@app.get("/users/{username}/posts")
async def post_by_user():
    return

@app.post("/posts/{posy_id}/like")
async def like_a_post():
    return