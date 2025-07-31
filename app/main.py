from fastapi import FastAPI
from db import Data
from pydantic import BaseModel
from logger import setup_loggers

app = FastAPI()
db = Data()
setup_loggers()

class Post(BaseModel):
    title: str
    content: str

# Handles GET requests to the root endpoint
@app.get("/")
def read_root():
    return {"message": "API is running"}

# Handles HTTP GET requests to the posts endpoint
@app.get("/posts")
def get_posts():
    return db.get_posts()

# Handles HTTP POST requests to the posts endpoint
@app.post("/posts")
def create_post(post: Post):
    return db.create_post(post.title, post.content)
