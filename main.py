from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Welcome to Noor's Api!"}

@app.get("/posts")
def get_users():
    return {"data": "this is your post"}
