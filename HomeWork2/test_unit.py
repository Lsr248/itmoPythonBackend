import json
import sqlite3
import tempfile

import pytest

from db import init_db, insert_data, insert_review, select_salons

db_fd, db_path = tempfile.mkstemp()
init_db(db_path)
insert_data(db_path)


@pytest.mark.parametrize(
    "id, result_salon",
    [
        (1, [(1, "Salon1", 5.0, "Region1")]),
        (2, [(2, "Salon2", 4.0, "Region2")]),
        (3, []),
    ],
)
def test_init_db(id, result_salon):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM salons WHERE id = ?", (id,))
    result = cursor.fetchall()
    assert result == result_salon
    connection.close()


def test_select_salons():
    result = select_salons(0, "", db_path)
    with open("HomeWork2/test_show_salons.json", "r") as f:
        expected = json.load(f)
    assert result == expected


@pytest.mark.parametrize(
    "rating, region, expected_result",
    [
        (4.0, "", [{"name": "Salon1", "rating": 5.0, "region": "Region1"}]),
        (4.0, "Region1", [{"name": "Salon1", "rating": 5.0, "region": "Region1"}]),
        (3.0, "Region2", [{"name": "Salon2", "rating": 4.0, "region": "Region2"}]),
        (2.0, "Region1", [{"name": "Salon1", "rating": 5.0, "region": "Region1"}]),
    ],
)
def test_select_salons_with_parameters(rating, region, expected_result):
    result = select_salons(rating, region, db_path)
    assert result == expected_result


@pytest.mark.parametrize(
    "id_salon, id_hairdresser, text, expected_result",
    [
        (1, 1, "I liked it", [("Wonderful",), ("I liked it",)]),
        (2, 2, "Good", [("Good",)]),
        (1, 3, "Great!", [("Great!",)]),
        (2, 3, "Bad", [("Good",), ("Bad",)]),
    ],
)
def test_push_review(id_salon, id_hairdresser, text, expected_result):
    insert_review(id_salon, id_hairdresser, text, db_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT text FROM reviews WHERE salon_id = ? AND hairdresser_id = ?",
        (
            id_salon,
            id_hairdresser,
        ),
    )
    result = cursor.fetchall()
    assert result == expected_result
    connection.close()
