from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form
from fastapi.security import OAuth2PasswordBearer

from app.api.v1 import post as post_router
from app.api.v1 import user as user_router
from app.api.v1 import auth as auth_router



app = FastAPI(title="Mini_Social_Media_API")    

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Welcome to the Mini Social Media API!"}

app.include_router(auth_router.router, prefix="/api/v1", tags=["auth"])
app.include_router(user_router.router, prefix="/api/v1", tags=["users"])
app.include_router(post_router.router, prefix="/api/v1", tags=["posts"])



