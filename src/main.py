from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4
from models.item import Item
app = FastAPI(
    title="Simple API",
    description="A simple API with basic routes",
    version="0.1.0"
)

# In-memory storage for our items
items = dict[UUID, Item]()

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Simple API"}

@app.get("/items", response_model=dict)
async def get_items():
    """
    Get all items.
    """
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """
    Get a specific item by ID.
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    """
    Create a new item.
    """
    item_id = uuid4()
    items[item_id] = item
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: UUID, item: Item):
    """
    Update an existing item.
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: UUID):
    """
    Delete an item.
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items.pop(item_id)