import requests


def test_get_user_list_e2e():
    url = 'http://localhost:8000/api/users/list'

    response = requests.get(url)

    assert response.status_code == 200

    user_list = response.json()
    assert len(user_list) > 0
    assert 'username' in user_list[0]
    assert 'userId' in user_list[0]
    assert 'firstSeen' in user_list[0]
