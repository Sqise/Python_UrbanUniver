# Дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
#
#     С текстом 'Рассчитать норму калорий' и callback_data='calories'
#     С текстом 'Формулы расчёта' и callback_data='formulas'


from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
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
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
    ))


@dp.callback_query_handler(lambda c: c.data == 'formulas')
async def get_formulas(call):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Формула (для мужчин): 10 * вес + 6.25 * рост - 5 * возраст + 5")


@dp.callback_query_handler(lambda c: c.data == 'calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
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
    # calories_w = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Норма калорий для мужчин - {calories_m:.1f} ккал")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
