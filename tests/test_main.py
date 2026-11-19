from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200


def test_get_employee_success():
    response = client.get("/employees/Ravi")
    assert response.status_code == 200


def test_employee_not_found():
    response = client.get("/employees/Unknown")
    assert response.status_code == 404


def test_add_employee():
    response = client.post("/employees", json={"name": "Arun", "salary": 25000})
    assert response.status_code == 200


def test_invalid_salary():
    response = client.post("/employees", json={"name": "Test", "salary": -100})
    assert response.status_code == 422


def test_empty_name():
    response = client.post("/employees", json={"name": "", "salary": 20000})
    assert response.status_code == 422
