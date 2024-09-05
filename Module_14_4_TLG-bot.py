# Дополните ранее написанный код для Telegram-бота:
#     В самом начале запускайте ранее написанную функцию get_all_products.
#     Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации продуктов
#     функцию get_all_products. Полученные записи используйте в выводимой надписи:
#     "Название: <title> | Описание: <description> | Цена: <price>"

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Module_14_crud_functions import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Инициализация базы данных при запуске
initiate_db()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Информация'), KeyboardButton('Купить'))


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Выберите действие:", reply_markup=keyboard)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    products = get_all_products()  # Получаем все продукты из базы данных

    if not products:
        await message.answer("Нет доступных продуктов для покупки.")
        return

    inline_kb = InlineKeyboardMarkup()

    for product in products:
        product_id, title, description, price = product
        inline_kb.add(InlineKeyboardButton(title, callback_data=f'product_buying_{product_id}'))
        await message.answer_photo(
            open(f'files_bot_ru//{title}.jpg', 'rb'),  # Имя файла зависит от названия продукта
            caption=f'Название: {title} | Описание: {description} | Цена: {price}'
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data.startswith('product_buying_'))
async def send_confirm_message(call):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
