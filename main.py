from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Welcome to Noor's Api!"}

@app.get("/posts")
def get_users():
    return {"data": "this is your post"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

