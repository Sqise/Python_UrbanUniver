# Создайте и дополните клавиатуры:
#
#     В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
#     Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
#     У всех кнопок назначьте callback_data="product_buying"
#
# Создайте хэндлеры и функции к ним:
#
#     Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию
#     get_buying_list(message).
#     Функция get_buying_list должна выводить надписи
#     'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
#     После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное
#     Inline меню с надписью "Выберите продукт для покупки:".
#     Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию
#     send_confirm_message(call).
#     Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"

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
keyboard.add(KeyboardButton('Рассчитать'), KeyboardButton('Информация'), KeyboardButton('Купить'))

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


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    await message.answer("Выберите продукт для покупки:", reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton('Зелье на деньги', callback_data='product_buying'),
        InlineKeyboardButton('Зелье на любовь', callback_data='product_buying'),
        InlineKeyboardButton('Зелье на счастье', callback_data='product_buying'),
        InlineKeyboardButton('Зелье на удачу', callback_data='product_buying'),
        InlineKeyboardButton('Зелье на успех', callback_data='product_buying'),
        InlineKeyboardButton('Зелье на здоровье', callback_data='product_buying')
    ))
    await message.answer_photo(open('files_bot//dengi.jpg', 'rb'), caption='Название: Зелье на деньги | Описание: Зелье для увеличения богатства | Цена: 100')
    await message.answer_photo(open('files_bot//Lyubov.jpg', 'rb'), caption='Название: Зелье на любовь | Описание: Зелье для привлечения любви | Цена: 200')
    await message.answer_photo(open('files_bot//shchastie.jpg', 'rb'), caption='Название: Зелье на счастье | Описание: Зелье для получения счастья | Цена: 300')
    await message.answer_photo(open('files_bot//udacha.jpg', 'rb'), caption='Название: Зелье на удачу | Описание: Зелье для удачи в делах | Цена: 400')
    await message.answer_photo(open('files_bot//uspeh.jpg', 'rb'), caption='Название: Зелье на успех | Описание: Зелье для успеха в карьере | Цена: 500')
    await message.answer_photo(open('files_bot//zdorovie.jpg', 'rb'), caption='Название: Зелье на здоровье | Описание: Зелье чтобы больше не болеть | Цена: 600')


@dp.callback_query_handler(lambda c: c.data == 'product_buying')
async def send_confirm_message(call):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)