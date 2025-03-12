import json
import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_endpoint(client):
    # Test the /chat endpoint with a query that should map to train_schedule intent
    test_data = {"message": "What is the train schedule for train 12345?"}
    response = client.post('/chat', data=json.dumps(test_data), content_type='application/json')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "response" in json_data
    assert json_data["intent"] == "train_schedule"

def test_train_schedule_endpoint(client):
    # Test the /train-schedule endpoint and verify the structure of the response
    response = client.get('/train-schedule?train_id=12345')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["train_id"] == "12345"
    assert "schedule" in json_data
