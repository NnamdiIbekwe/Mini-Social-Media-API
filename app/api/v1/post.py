from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.schema import PostCreate, PostResponse, LikeResponse
from app.api.depends import get_db, get_current_user
from app.models.posts import Post, Like
from app.models.users import User

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostResponse)
async def create_new_post(post: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_post = Post(
        content=post.content,
        image_url=post.image_url,
        is_public=post.is_public,
        user_id=current_user.id,
    )
    db.add(new_post)
    db.commit() # Commit the changes to the database
    db.refresh(new_post) # Refresh to get any DB-generated fields like the post ID
 
    return {"message": "Post created successfully", "post": new_post}

@router.post("/{post_id}/like", response_model=LikeResponse)
async def like_a_post(post_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Check if the user has already liked the post
    existing_like = db.query(Like).filter(Like.post_id == post_id, Like.user_id == current_user.id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="User has already liked this post")
    
    # Create a new like entry
    new_like = Like(user_id=current_user.id, post_id=post_id)
    db.add(new_like)
    
    # Increment the like count on the post
    post.likes += 1
    
    db.commit() # Commit the changes to the database
    return {"message": f"Post{post_id} liked successfully by user {current_user.username}"}

@router.get("/", response_model=list[PostResponse])
async def all_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    posts = db.query(Post).all()
    return posts

@router.get("/users/{user_id}/posts", response_model=list[PostResponse])
async def post_by_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return db.query(Post).filter(Post.user_id == user.id).all()


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post