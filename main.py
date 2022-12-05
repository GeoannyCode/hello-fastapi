#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI 
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_colot: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/") #path decorator
def home():
    return{"Hello": "World"}

# Request and response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person