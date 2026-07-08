from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Define the Pydantic model for the request body
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Added PUT route that accepts a path parameter and a JSON body
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}