# Работа с состояниями в телеграм-боте.
#
# Задача "Цепочка вопросов":
# Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
# Группа состояний:
#
#     Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
#     Создайте класс UserState наследованный от StateGroup.
#     Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).


from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ''

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()  # Возраст
    growth = State()  # Рост
    weight = State()  # Вес


@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    calories_m = 10 * weight + 6.25 * growth - 5 * age + 5
    calories_w = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Норма калорий: \n \
    для мужчин - {calories_m:.1f} ккал, \n \
    для женщин - {calories_w:.1f} ккал,")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
