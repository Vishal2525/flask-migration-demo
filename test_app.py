from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Hello from Flask"
    assert data["status"] == "running"

def test_get_user():
    client = app.test_client()
    response = client.get("/users/42")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 42
    assert data["name"] == "User 42"
