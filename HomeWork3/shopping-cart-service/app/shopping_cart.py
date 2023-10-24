import db_manager
from fastapi import APIRouter, HTTPException
from models import CartIn, UserIn
from service import count_price, update_user_bank_count

cart = APIRouter()


@cart.post("/remove/", status_code=201)
async def remove_from_cart(cart: CartIn):
    result = await db_manager.update_cart_remove(cart.id_user, cart.id_stock)
    if not result:
        raise HTTPException(status_code=404, detail="Please repeat")


@cart.post("/add/", status_code=201)
async def add_to_cart(cart: CartIn):
    result = await db_manager.update_cart_add(cart.id_user, cart.id_stock)
    if not result:
        raise HTTPException(status_code=404, detail="Please repeat")


@cart.post("/pay/", status_code=201)
async def pay(user: UserIn):
    stock = await db_manager.get_stock_list(user.id_user)
    price = count_price(stock)
    try:
        update_user_bank_count(user.id_user, price)
    except Exception:
        raise HTTPException(status_code=404, detail="Please repeat")
    return "Successful payment"
