from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_category():
    response = client.post("/categories/", json={"name": "Test Category"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Category"

def test_read_category():
    response = client.get("/categories/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_list_categories():
    response = client.get("/categories/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_category():
    response = client.put("/categories/1", json={"name": "Updated Category"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Category"

def test_delete_category():
    response = client.delete("/categories/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Category deleted successfully"}
