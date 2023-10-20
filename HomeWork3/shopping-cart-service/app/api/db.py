import sqlite3

from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine


DATABASE_URI = "sqlite:///foo.db"

engine = create_engine(DATABASE_URI)
metadata = MetaData()

shopping_cart = Table(
    "cart",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("id_user", Integer),
    Column("ids_stock", String(100)),
)

database = Database(DATABASE_URI)


def get_db(db_path=None):
    connection = sqlite3.connect(db_path)

    return connection


def init_db(db_path=None):
    connection = get_db(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO cart (id, id_user, ids_stock) VALUES (?, ?, ?);",
        (1, 1, "1 2"),
    )
    connection.commit()
    cursor.execute(
        "INSERT INTO cart (id, id_user, ids_stock) VALUES (?, ?, ?);",
        (2, 2, "1 3"),
    )
    connection.commit()


init_db("foo.db")
