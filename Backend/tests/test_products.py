from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post(
        "/products/",
        json={
            "name": "Test Product",
            "description": "A test product",
            "brand_id": 1,
            "category_id": 1,
            "price": 10.0,
            "rating": 4.5
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
