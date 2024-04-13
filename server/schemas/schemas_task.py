from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[int]
    name: str
    isDone: bool

    class Config:
        orm_mode = True
