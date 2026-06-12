from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# TODO: Define your data models using Pydantic BaseModel classes
# Example structure (you'll need to implement this):
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float

# TODO: Create an in-memory data store (you can use a list or dictionary)
# Example: items = []

# Task 1: Implement basic GET endpoints
@app.get("/")
def read_root():
    """TODO: Return a welcome message"""
    pass

@app.get("/items")
def read_items():
    """TODO: Return a list of items"""
    pass

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """TODO: Return a specific item by ID"""
    pass

# Task 2: Add query parameters
@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    """TODO: Return items with pagination support"""
    pass

# Task 3: Implement POST and PUT endpoints
@app.post("/items")
def create_item():
    """TODO: Create a new item from request body"""
    pass

@app.put("/items/{item_id}")
def update_item(item_id: int):
    """TODO: Update an existing item"""
    pass

# To run the server, use:
# uvicorn starter_code:app --reload
