#     Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать
#     на текст 'Рассчитать', а не на 'Calories'.

#     Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом:
#     'Рассчитать' и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры
#     интерфейса устройства при помощи параметра resize_keyboard.
#     Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
#
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками.
# При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age,
# с которой начинается работа машины состояний для age, growth и weight.


from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()  # Возраст
    growth = State()  # Рост
    weight = State()  # Вес

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Рассчитать'), KeyboardButton('Информация'))

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(text=['Рассчитать'])
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
