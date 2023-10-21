from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    bank_count: int


class UserOut(UserIn):
    id: int


class UserUpdate(BaseModel):
    id: int
    delta: int
