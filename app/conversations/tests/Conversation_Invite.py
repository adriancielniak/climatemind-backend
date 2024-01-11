import pytest
from flask import url_for
from mock import mock

from app.common.tests.utils import assert_email_sent
from app.factories import faker, ScoresFactory

@pytest.mark.integration
def test_create_conversation_invite_with_valid_data(client_with_user_and_header, accept_json):
    client, _, session_header, _ = client_with_user_and_header
    valid_invited_user_name = faker.name()
    url = url_for("conversations.create_conversation_invite")
    response = client.post(
        url,
        headers=session_header + accept_json,
        json={"invitedUserName": valid_invited_user_name},
    )
    assert response.status_code == 201
    assert response.json["message"] == "conversation created"

@pytest.mark.integration
def test_create_conversation_invite_missing_user_name(client_with_user_and_header, accept_json):
    client, _, session_header, _ = client_with_user_and_header
    url = url_for("conversations.create_conversation_invite")
    response = client.post(
        url,
        headers=session_header + accept_json,
        json={},
    )
    assert response.status_code == 400
    assert "invitedUserName" in response.json["error"]

@pytest.mark.integration
def test_create_conversation_invite_with_invalid_user_name(client_with_user_and_header, accept_json):
    client, _, session_header, _ = client_with_user_and_header
    invalid_user_name = "Invalid#Name123"
    url = url_for("conversations.create_conversation_invite")
    response = client.post(
        url,
        headers=session_header + accept_json,
        json={"invitedUserName": invalid_user_name},
    )
    assert response.status_code == 400
    assert "invalid" in response.json["error"]

@pytest.mark.integration
def test_create_conversation_invite_without_token(client):
    url = url_for("conversations.create_conversation_invite")
    invited_user_name = faker.name()
    response = client.post(
        url,
        json={"invitedUserName": invited_user_name},
    )
    assert response.status_code == 401
    assert "Authorization" in response.json["error"]

@pytest.mark.integration
def test_create_conversation_invite_with_invalid_token(client, accept_json):
    expired_token = "expiredOrInvalidToken"  # Replace with an actual expired/invalid token
    session_header = [("Authorization", f"Bearer {expired_token}")]
    url = url_for("conversations.create_conversation_invite")
    invited_user_name = faker.name()
    response = client.post(
        url,
        headers=session_header + accept_json,
        json={"invitedUserName": invited_user_name},
    )
    assert response.status_code == 401
    assert "invalid" in response.json["error"]
