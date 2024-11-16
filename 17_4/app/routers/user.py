from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Annotated
from slugify import slugify

from backend.db_depends import get_db
from models.user import User as UserModel

router = APIRouter(prefix="/user", tags=["user"])


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


# Получение всех пользователей
@router.get("/", response_model=List[CreateUser])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    async with db as session:
        result = await session.execute(select(UserModel))
        users = result.scalars().all()
        return users


# Получение пользователя по ID
@router.get("/{user_id}", response_model=CreateUser)
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    async with db as session:
        result = await session.execute(select(UserModel).where(UserModel.id == user_id))
        user = result.scalar_one_or_none()

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

        return user


# Создание пользователя
@router.post("/create", response_model=dict)
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    async with db as session:
        # Проверка на существование пользователя по username
        existing_user = await session.execute(select(UserModel).where(UserModel.username == user.username))
        if existing_user.scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="User with this username already exists")

        # Преобразование данных пользователя
        user_data = user.model_dump()
        user_data['slug'] = slugify(user.username)  # Создаем slug из username

        stmt = insert(UserModel).values(**user_data)
        await session.execute(stmt)
        await session.commit()

        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


# Обновление пользователя
@router.put("/update/{user_id}", response_model=dict)
async def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    async with db as session:
        result = await session.execute(select(UserModel).where(UserModel.id == user_id))
        existing_user = result.scalar_one_or_none()

        if existing_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

        # Обновляем данные пользователя
        stmt = update(UserModel).where(UserModel.id == user_id).values(
            firstname=user.firstname,
            lastname=user.lastname,
            age=user.age
        )
        await session.execute(stmt)
        await session.commit()

        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


# Удаление пользователя
@router.delete("/delete/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    async with db as session:
        result = await session.execute(select(UserModel).where(UserModel.id == user_id))
        existing_user = result.scalar_one_or_none()

        if existing_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

        # Удаляем пользователя
        stmt = delete(UserModel).where(UserModel.id == user_id)
        await session.execute(stmt)
        await session.commit()

        return {'status_code': status.HTTP_200_OK, 'transaction': 'User deletion is successful!'}