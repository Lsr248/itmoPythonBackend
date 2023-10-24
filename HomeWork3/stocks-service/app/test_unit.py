from db_manager import get_stock, update_stock
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "id, expected_result",
    [
        (
            1,
            (1, "potato", 20, 4),
        ),
        (
            2,
            (2, "tomato", 30, 5),
        ),
    ],
)
async def test_get_stock(id, expected_result):
    response = await get_stock(id)
    assert response == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "id, delta, expected_result",
    [
        (
            1,
            1,
            1,
        ),
        (
            2,
            2,
            1,
        ),
    ],
)
async def test_update_stock(id, delta, expected_result):
    response = await update_stock(id, delta)
    assert response == expected_result
