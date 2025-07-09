from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_another_endpoint_if_you_had_one():
    # Пример дополнительного теста, если у вас будет больше эндпоинтов
    # response = client.get("/items/42")
    # assert response.status_code == 200
    # assert response.json() == {"item_id": 42, "q": None}
    pass