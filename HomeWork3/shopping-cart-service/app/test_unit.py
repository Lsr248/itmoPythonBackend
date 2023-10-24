import pytest
from service import update_user_bank_count


@pytest.mark.parametrize(
    "id, delta, expected_status",
    [
        (1, 100, 201),
        (2, 120, 201),
    ],
)
def test_update_user_bank_count(id, delta, expected_status):
    response = update_user_bank_count(id, delta)
    assert response.status_code == expected_status
