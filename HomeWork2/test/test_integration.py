import json

import requests


def test_show_salons():
    response = requests.get("http://127.0.0.1:80/hairdressingSalonsSPB/salons")
    assert response.status_code == 200
    with open("./HomeWork2/test/test_show_salons.json", "r") as f:
        expected = json.load(f)
    assert response.json() == expected


def test_show_hairdressers():
    response = requests.get("http://127.0.0.1:80/hairdressingSalonsSPB/salons/1")
    assert response.status_code == 200
    expected = [{"name": "Sam Sam", "rating": 5.0}, {"name": "Kylie Os", "rating": 3.0}]
    assert response.json() == expected


def test_push_review():
    query = {"text": "Good"}
    response = requests.post(
        "http://127.0.0.1:80/hairdressingSalonsSPB/salons/1/3", json=query
    )
    assert response.text == "Success sending review"
    responce_check = requests.get(
        "http://127.0.0.1:80/hairdressingSalonsSPB/salons/1/3"
    )
    assert responce_check.status_code == 200
    assert responce_check.json() == ["Good"]
