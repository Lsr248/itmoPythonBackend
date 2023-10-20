import main
import pytest
from fastapi.testclient import TestClient

client = TestClient(main.app)


@pytest.mark.parametrize(
    "id, excepted_status, expected_result",
    [
        (
            1,
            200,
            {"bank_count": 500, "id": 1, "name": "David"},
        ),
        (
            2,
            200,
            {"bank_count": 700, "id": 2, "name": "Peter"},
        ),
        (
            -1,
            404,
            {"detail": "User not found"},
        ),
    ],
)
def test_get_user(id, excepted_status, expected_result):
    response = client.get(f"/api/v1/users/{id}")
    assert response.status_code == excepted_status
    assert response.json() == expected_result


@pytest.mark.parametrize(
    "insert_data, excepted_status",
    [
        (
            {"id": 1, "delta": 100},
            201,
        ),
        (
            {"id": 2, "delta": 50},
            200,
        ),
    ],
)
def test_post_update(insert_data, excepted_status):
    response = client.post("/api/v1/users/update/", json=insert_data)
    assert response.status_code == excepted_status
