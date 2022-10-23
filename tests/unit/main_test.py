from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_request_example():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_login():
    response = client.get("/login")
    assert response.status_code == 200
    assert response.json() == {"msg": "login"}
