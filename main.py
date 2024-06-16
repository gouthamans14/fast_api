from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'data':{"name":"Gouthaman"}}

@app.get("/about")
def about():
    return {"data":"Gosduthaman"}
