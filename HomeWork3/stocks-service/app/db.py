import sqlite3

from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

DATABASE_URI = "sqlite:///foo.db"

engine = create_engine(DATABASE_URI)
metadata = MetaData()

stocks = Table(
    "stocks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("price", Integer),
    Column("count", Integer),
)

database = Database(DATABASE_URI)


def get_db(db_path=None):
    connection = sqlite3.connect(db_path)

    return connection


def init_db(db_path=None):
    connection = get_db(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO stocks (id, name, price, count) VALUES (?, ?, ?, ?);",
        (1, "potato", 20, 4),
    )
    cursor.execute(
        "INSERT INTO stocks (id, name, price, count) VALUES (?, ?, ?, ?);",
        (2, "tomato", 30, 5),
    )
    cursor.execute(
        "INSERT INTO stocks (id, name, price, count) VALUES (?, ?, ?, ?);",
        (3, "apple", 40, 6),
    )
    connection.commit()


init_db("foo.db")
