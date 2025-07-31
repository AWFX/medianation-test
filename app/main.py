from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from db import Data
#from model import Post
from logger import setup_loggers


# Initialize FastAPI app, database connection and logging
app = FastAPI()
db = Data()
setup_loggers()


# Handles HTTP GET requests to the health endpoint
@app.get("/health")
def check_status():
    return {"message": "API is runnning"}


# Handles HTTP GET requests to the posts endpoint
@app.get("/posts")
def get_posts():
    return db.get_posts()


# Handles HTTP POST requests to the posts endpoint
@app.post("/posts")
def create_post(post: Post):
    return db.create_post(post.title, post.content)


# Redirects 404 errors to the documentation page
@app.exception_handler(StarletteHTTPException)
def redirect_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return RedirectResponse(url="/docs")
    return exc
