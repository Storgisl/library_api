from pydantic import BaseModel
from datetime import date


class Book(BaseModel):
    id: int
    title: str
    description: str
    publish_date: date
    author: str
    genre: str
    quantity: int
