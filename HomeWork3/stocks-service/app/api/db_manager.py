from api.models import CastIn, CastOut, CastUpdate
from api.db import stocks, database



async def get_stock (id:int):
    query = stocks.select(stocks.c.id == id)
    return await database.fetch_one(query=query)

async def update_stock(id :int, delta:float):
    query1 = stocks.select(stocks.c.id == id)
    result = query1 - delta
    query = stocks.update().where(stocks.c.id == id).values(bank_count = result)
    return await database.execute(query=query)
