from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/task", tags=["task"])

class Task(BaseModel):
    title: str
    content: str
    priority: int

@router.get("/")
async def all_tasks():
    # Здесь будет код для получения всех задач
    return []

@router.get("/task_id")
async def task_by_id(task_id: int):
    # Здесь будет код для получения задачи по ID
    return {}

@router.post("/create")
async def create_task(task: Task):
    # Здесь будет код для создания задачи
    return {}

@router.put("/update")
async def update_task(task_id: int, task: Task):
    # Здесь будет код для обновления задачи
    return {}

@router.delete("/delete")
async def delete_task(task_id: int):
    # Здесь будет код для удаления задачи
    return {}