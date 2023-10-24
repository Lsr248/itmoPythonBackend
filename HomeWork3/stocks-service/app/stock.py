import db_manager
from fastapi import APIRouter, HTTPException
from models import StockOut, StockUpdate

stocks = APIRouter()


@stocks.post("/update/", status_code=201)
async def update_stock_count(stock: StockUpdate):
    print(stock)
    result = await db_manager.update_stock(stock.id, stock.count)
    if not result:
        raise HTTPException(status_code=404, detail="stock not found")


@stocks.get("/{id}/", response_model=StockOut)
async def get_stock(id: int):
    stock = await db_manager.get_stock(id)
    if not stock:
        raise HTTPException(status_code=404, detail="stock not found")
    return stock
