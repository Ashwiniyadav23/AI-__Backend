from fastapi import FastAPI

app = FastAPI()

# Get method
@app.get("/")
def home():
    return {"message": "Hello, welcome to learning FastAPI!"}

@app.get("/students")
def students():
    return ["Ashwini","Ash","Rash"]

# POST method
@app.post("/post")
def add_students():
    return {"message": "added student"}

#Update the dat
@app.put("/students")
def update_student():
    return {"message": "Student Updated"}

# Delete the data
@app.delete("/students")
def delete_student():
    return {"message": "Student Deleted"}

students = {
    1: "Ashwini",
    2: "Rahul",
    3: "Priya"
}


#path parameter
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "id": student_id,
        "name": students.get(student_id, "Student Not Found")
    }

# Query Parameters

from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def get_student(name: str, age: int):
    return {
        "name": name,
        "age": age
    }