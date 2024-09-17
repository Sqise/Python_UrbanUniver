# Создайте новое приложение FastAPI и сделайте CRUD запросы.

from fastapi import FastAPI, HTTPException, Path
from typing import Dict, Annotated

app = FastAPI()

# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


#     Реализуйте 4 CRUD запроса.

#     get запрос по маршруту '/users', который возвращает словарь users.
@app.get("/users")
async def get_users():
    return users


#     post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом
#     значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20)],
        age: Annotated[int, Path(ge=18, le=120)]
):
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


#     put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом
#     user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is registered"
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: str,
        username: Annotated[str, Path(min_length=5, max_length=20)],
        age: Annotated[int, Path(ge=18, le=120)]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


#     delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"
