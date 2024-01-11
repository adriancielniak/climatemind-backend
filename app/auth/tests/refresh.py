import pytest
from flask import url_for
from mock import mock

from app.common.tests.utils import assert_email_sent
from app.factories import faker, ScoresFactory

@pytest.mark.integration
def test_successful_token_refresh(client):

    registration_data = get_fake_registration_json()
    client.post(url_for("auth.register"), json=registration_data)
    login_response = client.post(url_for("auth.login"), json=registration_data)
    refresh_token = login_response.json['refresh_token']


    response = client.post(url_for("auth.refresh"), json={"refresh_token": refresh_token})
    assert response.status_code == 200
    assert "access_token" in response.json
    
@pytest.mark.integration
def test_failed_token_refresh_with_invalid_token(client):
    response = client.post(url_for("auth.refresh"), json={"refresh_token": "invalidToken"})
    assert response.status_code == 401
    assert response.json == {"error": "Invalid refresh token."}

@pytest.mark.integration
def test_failed_token_refresh_with_expired_token(client):
    # Uzyskanie wygasłego tokena odświeżania (symulacja)
    expired_refresh_token = "expiredToken"  # Zastąp przykładową wartością wygasłego tokena

    response = client.post(url_for("auth.refresh"), json={"refresh_token": expired_refresh_token})
    assert response.status_code == 401
    assert response.json == {"error": "Refresh token expired."}

@pytest.mark.integration
def test_failed_token_refresh_for_nonexistent_user(client):
    non_existent_user_token = "nonExistentUserToken"  # Zastąp przykładową wartością tokena

    response = client.post(url_for("auth.refresh"), json={"refresh_token": non_existent_user_token})
    assert response.status_code == 401
    assert response.json == {"error": "User not found."}
