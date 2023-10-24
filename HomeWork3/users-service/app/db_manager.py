from db import database, users
from models import UserOut


async def add_user(payload: UserOut):
    query = users.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_user(id: int):
    query = users.select(users.c.id == id)
    return await database.fetch_one(query=query)


async def update_user(id: int, delta: float):
    query1 = await get_user(id)
    result = query1[2] - delta
    query = users.update().where(users.c.id == id).values(bank_count=result)
    return await database.execute(query=query)
