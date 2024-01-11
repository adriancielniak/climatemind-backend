import pytest
from flask import url_for
from mock import mock

from app.common.tests.utils import assert_email_sent
from app.factories import faker, ScoresFactory

@pytest.mark.integration
def test_successful_logout(client):
    # User logs in first to get the token
    login_response = client.post(url_for("auth.login"), json=get_login_json())
    access_token = login_response.json['access_token']

    # User logs out
    response = client.post(url_for("auth.logout"), headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json == {"message": "User logged out successfully."}

@pytest.mark.integration
def test_logout_without_token(client):
    response = client.post(url_for("auth.logout"))
    assert response.status_code == 401
    assert response.json == {"error": "Authorization token required."}

@pytest.mark.integration
def test_logout_with_invalid_token(client):
    response = client.post(url_for("auth.logout"), headers={"Authorization": "Bearer invalidToken"})
    assert response.status_code == 401
    assert response.json == {"error": "Invalid token."}

@pytest.mark.integration
def test_logout_with_expired_token(client):
    expired_token = "expiredToken"  # Replace with an actual expired token
    response = client.post(url_for("auth.logout"), headers={"Authorization": f"Bearer {expired_token}"})
    assert response.status_code == 401
    assert response.json == {"error": "Token expired."}

@pytest.mark.integration
def test_multiple_logout_attempts(client):
    login_response = client.post(url_for("auth.login"), json=get_login_json())
    access_token = login_response.json['access_token']

    # First logout attempt
    first_response = client.post(url_for("auth.logout"), headers={"Authorization": f"Bearer {access_token}"})
    assert first_response.status_code == 200

    # Second logout attempt with the same token
    second_response = client.post(url_for("auth.logout"), headers={"Authorization": f"Bearer {access_token}"})
    assert second_response.status_code == 401
    assert second_response.json == {"error": "Invalid token."}

@pytest.mark.integration
def test_logout_with_altered_token(client):
    altered_token = "alteredToken"  # Replace with a manipulated token
    response = client.post(url_for("auth.logout"), headers={"Authorization": f"Bearer {altered_token}"})
    assert response.status_code == 401
    assert response.json == {"error": "Invalid token."}

@pytest.mark.integration
def test_logout_with_missing_authorization_header(client):
    response = client.post(url_for("auth.logout"), headers={})
    assert response.status_code == 401
    assert response.json == {"error": "Authorization header is missing."}

@pytest.mark.integration
def test_logout_with_non_bearer_token(client):
    non_bearer_token = "Basic nonBearerToken"  # Replace with a non-Bearer token
    response = client.post(url_for("auth.logout"), headers={"Authorization": non_bearer_token})
    assert response.status_code == 401
    assert response.json == {"error": "Invalid token type. Bearer token required."}
