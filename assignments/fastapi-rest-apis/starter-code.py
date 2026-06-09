from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

items: Dict[int, Item] = {}
next_item_id = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI item service"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items")
def create_item(item: Item):
    global next_item_id
    items[next_item_id] = item
    created_item = {"id": next_item_id, **item.dict()}
    next_item_id += 1
    return created_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}

# Run the app with:
# uvicorn starter-code:app --reload
