from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["user"])

class User(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

@router.get("/")
async def all_users():
    # Здесь будет код для получения всех пользователей
    return []

@router.get("/user_id")
async def user_by_id(user_id: int):
    # Здесь будет код для получения пользователя по ID
    return {}

@router.post("/create")
async def create_user(user: User):
    # Здесь будет код для создания пользователя
    return {}

@router.put("/update")
async def update_user(user_id: int, user: User):
    # Здесь будет код для обновления пользователя
    return {}

@router.delete("/delete")
async def delete_user(user_id: int):
    # Здесь будет код для удаления пользователя
    return {}