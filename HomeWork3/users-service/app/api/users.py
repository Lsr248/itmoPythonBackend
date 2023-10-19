from typing import Union

import db_manager
from fastapi import APIRouter, HTTPException
from models import UserOut, UserUpdate

users = APIRouter()


@users.post("/update/", status_code=201)
async def update_user_count(user: Union[UserUpdate, None]):
    print("update")
    print(user.id)
    print(user.delta)
    if user is None:
        print("wtffff")
    result = await db_manager.update_user(user.id, user.delta)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")


@users.get("/{id}/", response_model=UserOut)
async def get_user(id: int):
    print(id)
    user = await db_manager.get_user(id)
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
