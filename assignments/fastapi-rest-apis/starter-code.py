from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    in_stock: bool


class Item(ItemIn):
    id: int


items: dict[int, Item] = {}
next_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI REST API assignment!"}


@app.get("/items")
def list_items() -> dict[str, list[Item]]:
    return {"items": list(items.values())}


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemIn) -> Item:
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items[next_id] = item
    next_id += 1
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, payload: ItemIn) -> Item:
    existing = items.get(item_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **payload.model_dump())
    items[item_id] = updated
    return updated


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
