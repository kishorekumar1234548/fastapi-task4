from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Employee API")

employees = [
    {"name": "Ravi", "salary": 25000},
    {"name": "Kumar", "salary": 30000},
]


class Employee(BaseModel):
    name: str = Field(min_length=1)
    salary: float = Field(gt=0)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{name}")
def get_employee(name: str):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employees")
def add_employee(employee: Employee):
    employees.append(employee.model_dump())
    return {"message": "Employee added", "employee": employee}
