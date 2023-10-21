from db_manager import add_user, get_user, update_user
from models import UserOut
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "id, expected_result",
    [
        (
            1,
            (1, "David", 500),
        ),
        (
            2,
            (2, "Peter", 700),
        ),
    ],
)
async def test_get_user(id, expected_result):
    response = await get_user(id)
    assert response == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "id, delta, expected_result",
    [
        (
            1,
            20,
            1,
        ),
        (
            2,
            20,
            1,
        ),
    ],
)
async def test_update_user(id, delta, expected_result):
    response = await update_user(id, delta)
    assert response == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "id, user",
    [
        (
            3,
            {"bank_count": 600, "id": 3, "name": "Slava"},
        ),
        (
            4,
            {"bank_count": 200, "id": 4, "name": "Sam"},
        ),
    ],
)
async def test_add_usere(id, user):
    user_out = UserOut(
        id=user["id"],
        name=user["name"],
        bank_count=user["bank_count"],
    )
    await add_user(user_out)
    response = await get_user(id)
    assert response == user
