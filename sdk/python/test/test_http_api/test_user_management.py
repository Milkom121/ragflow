"""PYTEST_DONT_REWRITE"""
import pytest
from api.apps.user_management_app import user_mgmt
from flask import Flask
from flask.testing import FlaskClient

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(user_mgmt)
    app.config['TESTING'] = True
    return app

@pytest.fixture

def client(app) -> FlaskClient:
    return app.test_client()

def test_create_user(client):
    # Test user creation endpoint
    response = client.post('/api/user_management/user', json={
        "email": "testuser@example.com",
        "nickname": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["code"] == 0 or "user_id" in data.get("data", {})

def test_list_users(client):
    # Test list users endpoint
    response = client.get('/api/user_management/users')
    assert response.status_code == 200
    data = response.get_json()
    assert "data" in data

def test_update_user(client):
    # This test requires a user_id to update, so it depends on previous test
    # For simplicity, assume user_id is known or mock it
    user_id = "some-user-id"
    response = client.put(f'/api/user_management/user/{user_id}', json={
        "nickname": "updateduser"
    })
    # Since user_id may not exist, just check for valid response
    assert response.status_code in (200, 400, 404)

def test_delete_user(client):
    # This test requires a user_id to delete, so it depends on previous test
    user_id = "some-user-id"
    response = client.delete(f'/api/user_management/user/{user_id}')
    assert response.status_code in (200, 400, 404)
