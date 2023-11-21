import pytest
import src.service as service
import unittest.mock as mock
import requests

@mock.patch('src.service.get_user_from_db')
def test_get_user_from_db(virtual_function):
    virtual_function.return_value = "Alice"
    assert service.get_user_from_db(1) == "Alice"
    

# Substitute the requests.get function with a mock object.
@mock.patch('requests.get')
def test_get_users():
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Alice"}]
    mock_get = mock.Mock(return_value=mock_response)
    data = service.get_users()
    assert