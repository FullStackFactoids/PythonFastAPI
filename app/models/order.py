from pydantic import BaseModel
from typing import List
from .item import Item


class Order(BaseModel):
    id: int
    items: List[Item]
    total_price: float

    

