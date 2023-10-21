import sqlite3

from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

DATABASE_URI = "sqlite:///foo.db"

engine = create_engine(DATABASE_URI)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("bank_count", Integer),
)

database = Database(DATABASE_URI)


def get_db(db_path=None):
    connection = sqlite3.connect(db_path)

    return connection


def init_db(db_path=None):
    connection = get_db(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (id, name, bank_count) VALUES (?, ?, ?);",
        (1, "David", 500),
    )
    cursor.execute(
        "INSERT INTO users (id, name, bank_count) VALUES (?, ?, ?);",
        (2, "Peter", 700),
    )
    connection.commit()


init_db("foo.db")
