import pytest
import requests
import requests_mock

def test_read_users_with_invalid_credentials(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {'username': 'admin', 'password': 'admin'}

    with requests_mock.Mocker() as mock:
        mock.get(url, text='', status_code=401)
        response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text == ''

def test_read_users_with_valid_credentials(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {'username': 'admin', 'password': 'qwerty'}

    with requests_mock.Mocker() as mock:
        mock.get(url, text='', status_code=200)
        response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text == ''
