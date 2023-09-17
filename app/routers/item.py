from fastapi import APIRouter
from app.models.item import Item

router = APIRouter()

items = []


@router.post("/")
def create_item(item: Item):
    items.append(item)
    return item


@router.get("/")
def read_items():
    return items


@router.get("/{item_id}")
def read_item(item_id: int):
    return items[item_id]


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item


@router.delete("/{item_id}")
def delete_item(item_id: int):
    items.pop(item_id)
    return {"message": "Item deleted"}
