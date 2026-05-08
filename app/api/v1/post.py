from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.db.base import get_db
from app import models

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/")
async def create_new_post(post: schema.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(
        content=post.content,
        image_url=post.image_url,
        likes=post.likes,
        username=post.username,
        timestamp=post.timestamp
    )
    db.add(new_post)
    db.commit() # Commit the changes to the database
    db.refresh(new_post) # Refresh to get any DB-generated fields like the post ID
 
    return new_post

@router.post("/{post_id}/like")
async def like_a_post(post_id: int, user_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Check if the user has already liked the post
    existing_like = db.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="User has already liked this post")
    
    # Create a new like entry
    new_like = Like(user_id=user_id, post_id=post_id)
    db.add(new_like)
    
    # Increment the like count on the post
    post.likes += 1
    
    db.commit() # Commit the changes to the database
    return {"status": "Liked"}

@router.get("/")
async def all_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

@router.get("/users/{username}/posts")
async def post_by_user(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username ==username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return db.query(models.Post).filter(models.Post.username == username).all()

@router.get("/{post_id}")
async def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post