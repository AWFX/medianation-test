from fastapi import FastAPI
from db import Data
from model import Post
from logger import setup_loggers


# Initialize FastAPI app, database connection and logging
app = FastAPI()
db = Data()
setup_loggers()


# Handles HTTP GET requests to the posts endpoint
@app.get("/posts")
def get_posts():
    return db.get_posts()


# Handles HTTP POST requests to the posts endpoint
@app.post("/posts")
def create_post(post: Post):
    return db.create_post(post.title, post.content)
