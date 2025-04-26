from fastapi import FastAPI
import uvicorn

app = FastAPI()



items = []



@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/item")
def home():
    return {"message": "Hey World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items




if __name__ == "__main__":
     uvicorn.run('routes:app',host="localhost", port=8080, reload=True)

