from fastapi import FastAPI
from app.recycle import recycle_convert
app = FastAPI()



@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.get("/recycle")
def recycle_world():
    recycle_convert()
    return {"message": "recycle convert success"}