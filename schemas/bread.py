from pydantic import BaseModel
from typing import Optional
from pydantic import Field

class Bread(BaseModel):
    id: Optional[int] = None
    producto: str = Field(min_length=5)
    precio: float
    tipo: str

    class Config:
        schema_extra = {
            "example" : {
                "id": "1",
                "producto": "frances",
                "precio": 0.40,
                "tipo" :  "espiral",
            }
        }