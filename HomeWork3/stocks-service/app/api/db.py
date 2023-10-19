import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = "sqlite:///foo.db" #os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

stocks = Table(
    'stocks',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('count', Integer),
)

database = Database(DATABASE_URI)
