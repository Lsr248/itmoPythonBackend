from db import database, shopping_cart


async def get_cart(id_user: int):
    query = shopping_cart.select(shopping_cart.c.id_user == id_user)
    return await database.fetch_one(query=query)


async def update_cart_add(id_user: int, id_stock: int):
    row = await get_cart(id_user)
    new_array = row[2]
    new_array += " " + str(id_stock)
    query = (
        shopping_cart.update()
        .where(shopping_cart.c.id_user == id_user)
        .values(ids_stock=new_array)
    )
    return await database.execute(query=query)


async def update_cart_remove(id_user: int, id_stock: int):
    new_array = await get_stock_list(id_user)
    new_array.remove(str(id_stock))
    new_str = " ".join(new_array)
    query = (
        shopping_cart.update()
        .where(shopping_cart.c.id_user == id_user)
        .values(ids_stock=new_str)
    )
    return await database.execute(query=query)


async def get_stock_list(id_user: int):
    row = await get_cart(id_user)
    return row[2].split(" ")
