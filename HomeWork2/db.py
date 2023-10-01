import sqlite3
from collections import namedtuple

db_path = "database.sqlite"
Salon = namedtuple("Salon", "name, rating, region")


def create_db():
    """
    Function for creating all tables
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS salons (id INTEGER PRIMARY KEY, "
        "name TEXT, rating REAL, region TEXT)"
    )
    connection.commit()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS hairdressers(id INTEGER PRIMARY KEY,
        salon_id INTEGER, name TEXT, rating REAL)"""
    )
    connection.commit()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS reviews(id INTEGER PRIMARY KEY,
        salon_id INTEGER, hairdresser_id INTEGER, text TEXT) """
    )
    connection.commit()
    connection.close()


def insert_data():
    """
    Function for inserting all data
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO salons (id, name, rating, region) VALUES (?, ?, ?, ?);",
        (1, "Salon1", 5.0, "Region1"),
    )
    cursor.execute(
        "INSERT INTO salons (id, name, rating, region) VALUES (?, ?, ?, ?);",
        (2, "Salon2", 4.0, "Region2"),
    )

    cursor.execute(
        "INSERT INTO hairdressers (id, salon_id, name, rating) VALUES (?, ?, ?, ?);",
        (1, 1, "Sam Sam", 5.0),
    )
    cursor.execute(
        "INSERT INTO hairdressers (id, salon_id, name, rating) VALUES (?, ?, ?, ?);",
        (2, 1, "Kylie Os", 3.0),
    )
    cursor.execute(
        "INSERT INTO hairdressers (id, salon_id, name, rating) VALUES (?, ?, ?, ?);",
        (3, 2, "Grunt Gustin", 5.0),
    )
    cursor.execute(
        "INSERT INTO hairdressers (id, salon_id, name, rating) VALUES (?, ?, ?, ?);",
        (4, 2, "Tom Jerry", 4.8),
    )

    cursor.execute(
        "INSERT INTO reviews (id, salon_id, hairdresser_id, text) VALUES (?, ?, ?, ?);",
        (1, 1, 1, "Wonderful"),
    )
    cursor.execute(
        "INSERT INTO reviews (id, salon_id, hairdresser_id, text) VALUES (?, ?, ?, ?);",
        (2, 1, 2, "Not a master"),
    )
    cursor.execute(
        "INSERT INTO reviews (id, salon_id, hairdresser_id, text) VALUES (?, ?, ?, ?);",
        (3, 2, 3, "Good"),
    )

    connection.commit()
    connection.close()


def select_salons(rating: int, region: str):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    salons = []
    if region == "":
        cursor.execute(
            "SELECT name, rating, region FROM salons WHERE rating > ?", (rating,)
        )
    else:
        cursor.execute(
            "SELECT name, rating, region FROM salons WHERE rating > ? AND region = ?",
            (rating, region),
        )
    for i in cursor.fetchall():
        salon = {}
        salon["name"] = i[0]
        salon["rating"] = i[1]
        salon["region"] = i[2]
        salons.append(salon)

    return salons


def select_hairdressers(id_salon: int):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name, rating FROM hairdressers WHERE salon_id =?", (id_salon,)
    )

    hairdressers = []
    for i in cursor.fetchall():
        hairdresser = {}
        hairdresser["name"] = i[0]
        hairdresser["rating"] = i[1]
        hairdressers.append(hairdresser)

    return hairdressers


def select_reviews(id_salon: int, id_hairdresser: int):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT text FROM reviews WHERE salon_id =? AND hairdresser_id =?",
        (
            id_salon,
            id_hairdresser,
        ),
    )

    reviews = []
    for i in cursor.fetchall():
        reviews.append(i[0])
    return reviews


def max_id_reviews():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM reviews")

    ids = []
    for i in cursor.fetchall():
        ids.append(i[0])

    return max(ids)


def insert_review(id_salon: int, id_hairdresser: int, text: str):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    max_id = max_id_reviews()
    cursor.execute(
        "INSERT INTO reviews (id, salon_id, hairdresser_id, text) VALUES (?, ?, ?, ?);",
        (max_id + 1, id_salon, id_hairdresser, text),
    )
    connection.commit()
    cursor.close()
