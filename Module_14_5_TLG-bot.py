# Дополните ранее написанный код для Telegram-бота:

#     Кнопки главного меню дополните кнопкой "Регистрация".

#     Напишите новый класс состояний RegistrationState с следующими объектами класса State:
#     username, email, age, balance(по умолчанию 1000).

#     Создайте цепочку изменений состояний RegistrationState.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from Module_14_5_crud_functions_add import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Информация'), KeyboardButton('Купить'), KeyboardButton('Регистрация'))

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000  # Начальный баланс по умолчанию


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Обработчик нажатия на кнопку "Регистрация"
@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

# Обработчик ввода имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text

    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.next()  # Переход к следующему состоянию

# Обработчик ввода email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.next()  # Переход к следующему состоянию

# Обработчик ввода возраста
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text

    # Проверка, что возраст - это число
    if not age.isdigit():
        await message.answer("Возраст должен быть числом, пожалуйста, введите корректный возраст:")
        return

    age = int(age)
    await state.update_data(age=age)

    # Получаем все данные из состояния
    user_data = await state.get_data()
    username = user_data['username']
    email = user_data['email']

    # Добавляем пользователя в базу данных
    add_user(username, email, age)

    await message.answer("Регистрация завершена! Добро пожаловать, {}!".format(username))

    # Завершаем процесс регистрации
    await state.finish()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    products = get_all_products()

    if not products:
        await message.answer("Нет доступных продуктов для покупки.")
        return

    inline_kb = InlineKeyboardMarkup()

    for product in products:
        product_id, title, description, price = product
        inline_kb.add(InlineKeyboardButton(title, callback_data=f'product_buying_{product_id}'))
        await message.answer_photo(
            open(f'files_bot_ru//{title}.jpg', 'rb'),
            caption=f'Название: {title} | Описание: {description} | Цена: {price}'
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data.startswith('product_buying_'))
async def send_confirm_message(call):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
