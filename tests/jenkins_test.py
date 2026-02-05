import pytest
from api.api import api

def test_calculations():
    client = api.test_client()
    response = client.post("/calculator", json={"input": [1, 2, 3, 4, 5]})
    response_json = response.get_json()
    assert response.status_code == 200, f"Got {response.status_code} from {response_json} instead of expected result"
    assert response.get_json()["Mean"] == 0, f"Got {response_json['Mean']} instead of expected result of 0"
    assert response.get_json()["Median"] == 3, f"Got {response_json['Median']} instead of expected result of 3"
    assert response.get_json()["Min"] == 1, f"Got {response_json['Min']} instead of expected result of 1"
    assert response.get_json()["Max"] == 5, f"Got {response_json['Max']} instead of expected result of 5"
    assert response.get_json()["Standard Deviation"] == 1.5811388300841898, f"Got {response_json['Standard Deviation']} instead of expected result of 1.5811388300841898"

def test_invalid_key():
    client = api.test_client()
    response = client.post("/calculator", json={"": [1, 2, 3, 4, 5]})
    response_json = response.get_json()
    assert response.status_code == 400, f"Got {response.status_code} instead of expected status code of 400"

def test_not_enough_numbers():
    client = api.test_client()
    response = client.post("/calculator", json={"input": [1]})
    response_json = response.get_json()
    assert response.status_code == 400, f"Got {response.status_code} instead of expected status code of 400"

def test_none_numeric_inputs():
    client = api.test_client()
    response = client.post("/calculator", json={"input": [1, "a", 2]})
    response_json = response.get_json()
    assert response.status_code == 400, f"Got {response.status_code} instead of expected status code of 400"

def test_bool_inputs():
    client = api.test_client()
    response = client.post("/calculator", json={"input": [1, True, 2]})
    response_json = response.get_json()
    assert response.status_code == 400, f"Got {response.status_code} instead of expected status code of 400"