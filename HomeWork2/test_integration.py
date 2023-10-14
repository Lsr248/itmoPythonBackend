import json

import pytest


def test_hello(client):
    response = client.get("/hairdressingSalonsSPB")
    assert response.data == b"Welcome to hairdressingSalonsSPB!"


def test_show_salons(client):
    response = client.get("/hairdressingSalonsSPB/salons")
    assert response.status_code == 200
    with open("HomeWork2/test_show_salons.json", "r") as f:
        expected = json.load(f)
    assert response.json == expected


@pytest.mark.parametrize(
    "id, excepted_status, expected_result",
    [
        (
            1,
            200,
            b'[{"name":"Sam Sam","rating":5.0},{"name":"Kylie Os","rating":3.0}]\n',
        ),
        (
            2,
            200,
            b'[{"name":"Grunt Gustin","rating":5.0},{"name":"Tom Jerry","rating":4.8}]\n',
        ),
    ],
)
def test_show_hairdressers(client, id, excepted_status, expected_result):
    response = client.get(f"hairdressingSalonsSPB/salons/{id}")
    assert response.status_code == excepted_status
    assert response.data == expected_result


@pytest.mark.parametrize(
    "id_salon, id_haird, excepted_result",
    [
        (1, 2, b'["Not a master"]\n'),
        (2, 2, b'["This hairdresser has no reviews."]\n'),
    ],
)
def test_get_review(client, id_salon, id_haird, excepted_result):
    response = client.get(f"hairdressingSalonsSPB/salons/{id_salon}/{id_haird}")
    assert response.data == excepted_result


@pytest.mark.parametrize(
    "id_salon, id_haird, query, excepted_status",
    [
        (1, 2, {"text": "Good"}, 200),
        (2, 2, {"text": "I liked it"}, 200),
    ],
)
def test_push_review(client, id_salon, id_haird, query, excepted_status):
    response = client.post(
        f"hairdressingSalonsSPB/salons/{id_salon}/{id_haird}", json=query
    )
    assert response.text == "Success sending review"
    responce_check = client.get(f"hairdressingSalonsSPB/salons/{id_salon}/{id_haird}")
    assert responce_check.status_code == excepted_status
