from pydantic import BaseModel
from .order import Order


class Transaction(BaseModel):
    id: int
    order: Order
    payment_method: str
    payment_status: str


