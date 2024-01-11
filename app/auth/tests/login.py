import pytest
from flask import url_for
from mock import mock

from app.common.tests.utils import assert_email_sent
from app.factories import faker, ScoresFactory

@pytest.mark.integration
def test_failed_login_nonexistent_user(client):
    response = client.post(
        url_for("auth.login"),
        json={
            "email": "nonexistent@example.com",
            "password": "password123"
        },
    )
    assert response.status_code == 401
    assert response.json == {"error": "User does not exist."}

@pytest.mark.integration
def test_failed_login_wrong_password(client):
    registration = get_fake_registration_json()
    client.post(url_for("auth.register"), json=registration)
    response = client.post(
        url_for("auth.login"),
        json={
            "email": registration["email"],
            "password": "wrongpassword"
        },
    )
    assert response.status_code == 401
    assert response.json == {"error": "Wrong password."}

@pytest.mark.integration
def test_failed_login_without_email(client):
    registration_data = get_fake_registration_json()
    client.post(url_for("auth.register"), json=registration_data)
    response = client.post(
        url_for("auth.login"),
        json={"password": registration_data["password"]}
    )
    assert response.status_code == 400
    assert response.json == {"error": "Email and password must be included in the request body."}

@pytest.mark.integration
def test_failed_login_without_password(client):
    registration_data = get_fake_registration_json()
    client.post(url_for("auth.register"), json=registration_data)
    response = client.post(
        url_for("auth.login"),
        json={"email": registration_data["email"]}
    )
    assert response.status_code == 400
    assert response.json == {"error": "Email and password must be included in the request body."}

@pytest.mark.integration
def test_failed_login_with_nonexistent_email(client):
    response = client.post(
        url_for("auth.login"),
        json={
            "email": "nonexistent@example.com",
            "password": "password123"
        },
    )
    assert response.status_code == 401
    assert response.json == {"error": "Wrong email or password. Try again."}

@pytest.mark.integration
@mock.patch("app.auth.routes.check_if_local")
def test_failed_login_with_invalid_recaptcha_token(m_check_if_local, client):
    m_check_if_local.return_value = False  # to enforce recaptchaToken validation
    registration = get_fake_registration_json()
    client.post(url_for("auth.register"), json=registration)
    response = client.post(
        url_for("auth.login"),
        json={
            "email": registration["email"],
            "password": registration["password"],
            "recaptchaToken": "invalidToken"
        },
    )
    assert response.status_code == 401
    assert "error" in response.json


