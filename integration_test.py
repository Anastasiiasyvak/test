import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def test_app():
    client = TestClient(app)
    return client

def test_get_user_list_integration(test_app):
    response = test_app.get('/api/users/list')

    assert response.status_code == 200

    user_list = response.json()
    assert len(user_list) > 0
    assert 'username' in user_list[0]
    assert 'userId' in user_list[0]
    assert 'firstSeen' in user_list[0]
