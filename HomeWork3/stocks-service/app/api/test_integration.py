from fastapi.testclient import TestClient
import pytest
import main

client = TestClient(main.app)


@pytest.mark.parametrize(
    "id, excepted_status, expected_result",
    [
        (
            1,
            200,
            {"count": 4, "id": 1, "name": "potato", "price": 20},
        ),
        (
            2,
            200,
            {"count": 5, "id": 2, "name": "tomato", "price": 30},
        ),
        (
            -1,
            404,
            {"detail": "stock not found"},
        ),
    ],
)
def test_get_stock(id, excepted_status, expected_result):
    response = client.get(f"/api/v1/stocks/{id}")
    assert response.status_code == excepted_status
    assert response.json() == expected_result


@pytest.mark.parametrize(
    "insert_data, excepted_status",
    [
        (
            {"id": 1, "count": 2},
            201,
        ),
        (
            {"id": 2, "count": 1},
            201,
        ),
    ],
)
def test_post_update(insert_data, excepted_status):
    response = client.post(f"/api/v1/stocks/update/", json=insert_data)
    assert response.status_code == excepted_status
