from pydantic import BaseModel
from datetime import date


class author(BaseModel):
    id: int
    name: str
    biography: str
    birthday: date
