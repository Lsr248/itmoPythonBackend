import main
import pytest
from fastapi.testclient import TestClient

client = TestClient(main.app)


@pytest.mark.parametrize(
    "remove_data, excepted_status",
    [
        (
            {"id_user": 1, "id_stock": 1},
            201,
        ),
        (
            {"id_user": 2, "id_stock": 3},
            201,
        ),
    ],
)
def test_remove_from_cart(remove_data, excepted_status):
    response = client.post("/api/v1/cart/remove/", json=remove_data)
    assert response.status_code == excepted_status


@pytest.mark.parametrize(
    "insert_data, excepted_status",
    [
        (
            {"id_user": 1, "id_stock": 3},
            201,
        ),
        (
            {"id_user": 2, "id_stock": 2},
            201,
        ),
    ],
)
def test_add_to_cart(insert_data, excepted_status):
    response = client.post("/api/v1/cart/add/", json=insert_data)
    assert response.status_code == excepted_status


@pytest.mark.parametrize(
    "insert_data, excepted_status",
    [
        (
            {"id_user": 1},
            201,
        ),
        (
            {"id_user": 1},
            201,
        ),
    ],
)
def test_pay(insert_data, excepted_status):
    response = client.post("/api/v1/cart/pay/", json=insert_data)
    assert response.status_code == excepted_status
