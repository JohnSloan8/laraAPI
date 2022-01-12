from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from laraPython.lara_segment import segment_file
from os import listdir, path

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory = {}

@app.get("/list-text-files")
def get_item():
    items = listdir("data/text/")
    return {"items": items}

@app.post("/upload-text/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error, item exists"}
    inventory[item_id] = item
    return inventory[item_id]

@app.get("/segment-text/{text_file_name}")
def create_item(text_file_name: str):
    segment_file('data/text/' + text_file_name + '.txt', 'data/segmentedText/' + text_file_name + '_segmented.txt')
    output_file_path = path.dirname(path.abspath(__file__)) + '/data/segmentedText/' + text_file_name + '_segmented.txt'
    return output_file_path

# @app.get("/get-by-name")
# def get_item(test: int, name: Optional[str]=None ):
    # for item_id in inventory:
        # if inventory[item_id].name == name:
            # return inventory[item_id]
    # return {"Data": "Not Found"}

