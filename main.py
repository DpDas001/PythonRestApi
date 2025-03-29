from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class Item(BaseModel):
    age: int
    place: str
    location: str

@app.post("/submit")
def submit_item(item: Item):
    return {"age": item.age, "place": item.place, "location": item.location}