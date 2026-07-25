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