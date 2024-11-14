from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_brand():
    response = client.post("/brands/", json={"name": "Test Brand"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Brand"

def test_read_brand():
    response = client.get("/brands/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_list_brands():
    response = client.get("/brands/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_brand():
    response = client.put("/brands/1", json={"name": "Updated Brand"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Brand"

def test_delete_brand():
    response = client.delete("/brands/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Brand deleted successfully"}
