from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("fast_api_example.main:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

