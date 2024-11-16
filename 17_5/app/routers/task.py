from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from slugify import slugify
from typing import List, Annotated

from backend.db_depends import get_db
from models.task import Task as TaskModel
from models.user import User as UserModel
from pydantic import BaseModel

router = APIRouter(prefix="/task", tags=["task"])


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int = 0


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int = 0
    completed: bool = False


# Получение всех задач
@router.get("/", response_model=List[CreateTask])
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    result = await db.execute(select(TaskModel))
    tasks = result.scalars().all()
    return tasks


# Получение задачи по ID
@router.get("/{task_id}", response_model=CreateTask)
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    result = await db.execute(select(TaskModel).where(TaskModel.id == task_id))
    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

    return task


# Создание задачи
@router.post("/create", response_model=dict)
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверка на существование пользователя
    user_result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = user_result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    # Преобразование данных задачи
    task_data = task.dict()
    task_data['user_id'] = user_id
    task_data['slug'] = slugify(task.title)  # Генерация slug для задачи

    stmt = insert(TaskModel).values(**task_data)
    await db.execute(stmt)
    await db.commit()

    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


# Обновление задачи
@router.put("/update/{task_id}", response_model=dict)
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    result = await db.execute(select(TaskModel).where(TaskModel.id == task_id))
    existing_task = result.scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

    stmt = update(TaskModel).where(TaskModel.id == task_id).values(
        title=task.title,
        content=task.content,
        priority=task.priority,
        completed=task.completed
    )
    await db.execute(stmt)
    await db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


# Удаление задачи
@router.delete("/delete/{task_id}", response_model=dict)
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    result = await db.execute(select(TaskModel).where(TaskModel.id == task_id))
    existing_task = result.scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

    stmt = delete(TaskModel).where(TaskModel.id == task_id)
    await db.execute(stmt)
    await db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deletion is successful!'}