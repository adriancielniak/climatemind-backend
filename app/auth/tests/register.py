import pytest
from flask import url_for
from mock import mock

from app.common.tests.utils import assert_email_sent
from app.factories import faker, ScoresFactory



@pytest.mark.integration
def test_failed_registry_invalid_email(client):
    data = get_fake_registration_json()
    data['email'] = 'invalid-email'
    response = client.post(url_for("auth.register"), json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Invalid email format."}

@pytest.mark.integration
def test_failed_registry_invalid_email(client):
    data = get_fake_registration_json()
    data['email'] = 'invalid-email'
    response = client.post(url_for("auth.register"), json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Invalid email format."}
