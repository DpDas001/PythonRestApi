from fastapi import FastAPI
from pydantic import BaseModel

from outboundservice import invoke
from prerequesthandler import prepare

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class Item(BaseModel):
    age: str
    place: str
    summary: str
    example: str
    cues: str
    language: str

@app.post("/submit")
def submit_item(item: Item):
   # return {"age": item.age, "place": item.place, "location": item.location}
   prompt = prepare(item)
   return invoke(prompt)