from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel

app = FastAPI()

students_db = []

class Student(BaseModel):
    Reference: str
    firstName: str
    lastName: str
    Age: int

@app.get("/hello")
def read_root():
    return {"message": "Hello world"}

@app.get("/welcome/{name}")
def read_item(request: Request, name: str):
    accept_headers = request.headers.get("accept")
    if accept_headers != "text/plain":
        return JSONResponse(content={"message": "Unsupported Media Type"}, status_code=400)
    return PlainTextResponse(f"hello {name}")

@app.post("/students")
def add_students(students: list[Student]):
    for student in students:
        students_db.append(student)
    return {"message": "Étudiants ajoutés avec succès", "count": len(students)}

@app.get("/students")
def get_students():
    return {"students": students_db}



# python -m venv venv
# venv\Scripts\activate
# pip install fastapi uvicorn
# uvicorn main:app --reload