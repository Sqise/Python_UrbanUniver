from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from typing import List, Annotated

from backend.db_depends import get_db
from models.user import User as UserModel
from models.task import Task as TaskModel
from pydantic import BaseModel

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


class UserWithTasks(CreateUser):
    tasks: List[dict]

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


# Получение всех задач конкретного пользователя по его ID
@router.get("/{user_id}/tasks", response_model=List[dict])
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверка существования пользователя
    user_result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = user_result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    # Получение всех задач пользователя
    tasks_result = await db.execute(select(TaskModel).where(TaskModel.user_id == user_id))
    tasks = tasks_result.scalars().all()

    return tasks


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


# Изменение функции удаления пользователя
@router.delete("/delete/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверка существования пользователя
    user_result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = user_result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    # Удаление задач пользователя
    await db.execute(delete(TaskModel).where(TaskModel.user_id == user_id))

    # Удаление самого пользователя
    await db.execute(delete(UserModel).where(UserModel.id == user_id))
    await db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User and related tasks deletion is successful!'}