from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello world"}

@app.get("/welcome/{name}")
def read_item(request: Request, name: str):
    accept_headers = request.headers.get("Accept")

    if name is None:
        return {"message": "hello"}

    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)
    else:
        return PlainTextResponse(f"hello {name}")
# python -m venv venv
# venv\Scripts\activate
# pip install fastapi uvicorn
# uvicorn main:app --reload