from pydantic import BaseModel


class StockIn(BaseModel):
    name: str
    price: int
    count: int


class StockOut(StockIn):
    id: int


class StockUpdate(BaseModel):
    id: int
    count: int
