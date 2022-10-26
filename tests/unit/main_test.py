from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_request_example():
    response = client.get("/")
    assert response.json() == {"msg": "Hello World"}


def test_login():
    response = client.post("/auth/token",
                           data={"username": "johndoe@mail.com", "password": "hunter2", "grant_type": "password"})
    assert "access_token" in response.json()
    response_root = client.post("/", headers={"Authorization": f'Bearer {response.json()["access_token"]}'})
    assert "token" in response_root.json()


def test_query():
    response = client.get("/login_get")
    assert response.json() == {
        'johndoe@mail.com': {
            'name': 'John Doe',
            'password': 'hunter2'
        }
    }
