from typing import Union
from fastapi import FastAPI, Request
import uvicorn
from dataclasses import dataclass

app = FastAPI()

@dataclass
class Item:
    _id: int
    name: str
    other: list


items = []

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("fast_api_example.main:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/get/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id not in [item._id for item in items]:
        return {"error": f"Item with id {item_id} does not exist"}
    item = list(filter(lambda i: i._id == item_id, items))[0]
    return {"item_id": item._id, "name": item.name, "other": item.other}

@app.post("/items/add")
async def read_item(request: Request):
    request_json: Dict = await request.json()
    item_id: int = request_json["item_id"]
    if item_id in [item._id for item in items]:
        return {"error": f"An item already exists with item_id {item_id}. Specify an other one, item_id must be unique."}
    name: str = request_json["name"]
    other: list = request_json.get("other", None)
    items.append(Item(item_id, name, other))
    return [{"_id": item._id, "name": item.name, "other": item.other} for item in items]

