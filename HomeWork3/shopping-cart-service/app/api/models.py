from pydantic import BaseModel
from typing import List, Optional

class StockIn(BaseModel):
    name: str
    count: int = None


class StockOut(StockIn):
    id: int
