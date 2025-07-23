from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur mon API!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# python -m venv venv
# venv\Scripts\activate
# pip install fastapi uvicorn
# uvicorn main:app --reload