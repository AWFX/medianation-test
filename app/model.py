from pydantic import BaseModel

# Post model for the application
class Post(BaseModel):
    title: str
    content: str
