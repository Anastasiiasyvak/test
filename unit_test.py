import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def test_app():
    client = TestClient(app)
    return client


def test_fetch_user_data_successful(test_app):
    response = test_app.get('/api/users/list')
    assert response.status_code == 200
    user_list = response.json()
    assert len(user_list) > 0


def test_fetch_user_data_failure(test_app):
    url = 'https://sef.podkolzin.consulting/api/users/lastSeen?offset=nonexistent'
    response = test_app.get(url)
    assert response.status_code != 200
    data = response.json()
    assert 'error' in data
