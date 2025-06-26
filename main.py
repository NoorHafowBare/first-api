#fast Api
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello Welcome to Noor's Api!"}

@app.get("/posts")
def get_users():
    return {"data": "this is your post"}

@app.post("/createposts")
def create_posts(post: post):
    print(post)
    print(post.dict())
    return {"data": post}

