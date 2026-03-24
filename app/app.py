from fastapi import FastAPI, HTTPException
from app.schema import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_sync_session
from app.db import post
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "New Post", "content": "Coll test post"},
    2: {"title": "Python Tips", "content": "List comprehensions are elegant and fast."},
    3: {"title": "Morning Routine", "content": "Coffee and coding is the best way to start the day."},
    4: {"title": "Database Setup", "content": "Remember to use echo=True for debugging SQLModel."},
    5: {"title": "FastAPI Guide", "content": "Lifespan events help manage database connections."},
    6: {"title": "Debugging Life", "content": "It's not a bug, it's an undocumented feature."},
    7: {"title": "Prime Numbers", "content": "The square root optimization makes loops much faster."},
    8: {"title": "Deep vs Shallow", "content": "Always use deepcopy for nested list structures."},
    9: {"title": "Git Workflow", "content": "Commit early, commit often, and write good messages."},
    10: {"title": "AI Future", "content": "Generative models are changing how we write code."}
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) +
               1] = new_post
    return new_post
