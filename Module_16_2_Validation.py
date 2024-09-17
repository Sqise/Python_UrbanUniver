# Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated.

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


# '/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id,
# для которого необходимо написать следующую валидацию:
#
#     Должно быть целым числом
#     Ограничено по значению: больше или равно 1 и меньше либо равно 100.
#     Описание - 'Enter User ID'
#     Пример - свой


@app.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='22')]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# '/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и age,
# для которых необходимо написать следующую валидацию:
#
#     username - строка, age - целое число.
#     username ограничение по длине: больше или равно 5 и меньше либо равно 20.
#     age ограничение по значению: больше или равно 18 и меньше либо равно 120.
#     Описания для username и age - 'Enter username' и 'Enter age' соответственно.
#     Пример - свой

@app.get("/user/{username}/{age}")
async def user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='PythonUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='45')]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
