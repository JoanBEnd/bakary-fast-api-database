from pydantic import BaseModel
from typing import Optional


class User(BaseModel):     
    id: Optional[int] = None
    usuario: str
    password: str

    class Config():
        schema_extra = {
            "example": {  
                "id": "1",
                "usuario": "bakery@gmail.com",
                "password": "@auth_2023@",
            }
        }