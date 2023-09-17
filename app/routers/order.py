from fastapi import APIRouter
from app.models.order import Order

router = APIRouter()

orders = []


@router.post("/")
def create_order(order: Order):
    orders.append(order)
    return order


@router.get("/")
def read_orders():
    return orders




@router.get("/{order_id}")
def read_order(order_id: int):
    return orders[order_id]


@router.delete("/{order_id}")
def delete_order(order_id: int):
    orders.pop(order_id)
    return {"message": "Order deleted"}
