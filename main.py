#fast Api
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "i like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Hello Welcome to Noor's Api!"}

@app.get("/posts")
def get_users():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: post):
    # print(post)
    # print(post.dict())
    post_dict = post.dict()
    post_dict['id'] =  randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post =(id)
    return {"post_detail": post}
