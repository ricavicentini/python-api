from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    desciption: str
    price: float
    on_offer: bool = False
   