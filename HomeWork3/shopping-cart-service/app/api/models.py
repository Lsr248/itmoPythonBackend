from pydantic import BaseModel


class CartIn(BaseModel):
    id_user: int
    id_stock: int


class UserIn(BaseModel):
    id_user: int
