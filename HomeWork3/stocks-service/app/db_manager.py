from db import database, stocks


async def get_stock(id: int):
    query = stocks.select(stocks.c.id == id)
    return await database.fetch_one(query=query)


async def update_stock(id: int, delta: int):
    row = await get_stock(id)
    result = row[3] - delta
    query = stocks.update().where(stocks.c.id == id).values(count=result)
    return await database.execute(query=query)
