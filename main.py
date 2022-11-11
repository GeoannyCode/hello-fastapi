from fastapi import FastAPI

app = FastAPI()

@app.get("/") #path decorator
def home():
    return{"Hello": "World"}