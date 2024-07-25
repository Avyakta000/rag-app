from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
    id: int
    file_name: str
    upload_date: datetime

    class Config:
        orm_mode = True