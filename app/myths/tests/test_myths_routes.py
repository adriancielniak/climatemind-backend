from flask import url_for
import pytest

from app.common.tests.utils import is_none_or_type


@pytest.mark.integration
def test_myths(client):
    response = client.get(url_for("myths.get_general_myths"))
    json = response.get_json()

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.access_control_allow_origin == "*"

    assert type(json) == dict
    assert "myths" in json
    assert type(json["myths"]) == list
    assert len(json["myths"]) != 0


@pytest.mark.integration
def test_myth_properties(client):
    response = client.get(url_for("myths.get_general_myths"))
    json = response.get_json()
    myths = json["myths"]

    assert len(myths) > 0
    for myth in myths:
        assert "faultyLogicDescription" in myth
        assert "iri" in myth
        assert "mythClaim" in myth
        assert "mythRebuttal" in myth
        assert "mythSources" in myth
        assert "mythTitle" in myth
        assert "mythVideos" in myth
        assert is_none_or_type(myth["faultyLogicDescription"], str)
        assert is_none_or_type(myth["iri"], str)
        assert is_none_or_type(myth["mythClaim"], str)
        assert is_none_or_type(myth["mythRebuttal"], str)
        assert is_none_or_type(myth["mythSources"], list)
        assert is_none_or_type(myth["mythTitle"], str)
        assert is_none_or_type(myth["mythVideos"], list)


#Konrad tests
@pytest.mark.integration
def test_specific_myth_retrieval(client):
    # Use a known IRI for testing
    test_iri = "some_known_test_iri"
    response = client.get(url_for("myths.get_myth_info", iri=test_iri))
    json = response.get_json()

    assert response.status_code == 200
    assert "myth" in json
    assert json["myth"]["iri"] == test_iri

@pytest.mark.integration
def test_invalid_iri_handling(client):
    invalid_iri = "invalid_iri"
    response = client.get(url_for("myths.get_myth_info", iri=invalid_iri))
    
    assert response.status_code == 400  # or whatever your error code is
    assert "error" in response.get_json()


@pytest.mark.integration
def test_empty_database_handling(client):
    # Ensure the database or myth data is empty for this test
    response = client.get(url_for("myths.get_general_myths"))
    
    assert response.status_code == 200
    assert response.get_json()["myths"] == []

@pytest.mark.integration
def test_myth_data_consistency(client):
    response = client.get(url_for("myths.get_general_myths"))
    myths = response.get_json()["myths"]

    for myth in myths:
        for key in ["iri", "mythTitle", "mythClaim", "mythRebuttal", "mythSources", "mythVideos", "faultyLogicDescription"]:
            assert key in myth

@pytest.mark.integration
def test_cors_headers(client):
    response = client.get(url_for("myths.get_general_myths"))
    assert response.headers["Access-Control-Allow-Origin"] == "*"


import time

@pytest.mark.integration
def test_response_time(client):
    start_time = time.time()
    response = client.get(url_for("myths.get_general_myths"))
    end_time = time.time()

    assert response.status_code == 200
    assert (end_time - start_time) < 1  # for example, less than 1 second
