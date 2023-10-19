from fastapi import APIRouter, HTTPException

from api.models import StockOut, StockIn
from api import db_manager

users = APIRouter()
@users.post('/update/{id}/', status_code=201)
async def update_stock_count(delta: int):
    result = await db_manager.update_stock(id, delta)
    if not result:
        raise HTTPException(status_code=404, detail="stock not found")
@users.get('/{id}/', response_model=StockOut)
async def get_user(id: int):
    stock= await db_manager.get_stock(id)
    if not stock:
        raise HTTPException(status_code=404, detail="stock not found")
    return stock
