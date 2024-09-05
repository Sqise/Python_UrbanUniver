# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
#
#     id - целое число, первичный ключ
#     title(название продукта) - текст (не пустой)
#     description(описание) - тест
#     price(цена) - целое число (не пустой)
#
# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
#
# пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

import sqlite3


def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    products = [
        ('Зелье на деньги', 'Зелье для увеличения богатства', 100),
        ('Зелье на любовь', 'Зелье для привлечения любви', 200),
        ('Зелье на счастье', 'Зелье для получения счастья', 300),
        ('Зелье на удачу', 'Зелье для удачи в делах', 400),
        ('Зелье на успех', 'Зелье для успеха в карьере', 500),
        ('Зелье на здоровье', 'Зелье чтобы больше не болеть', 600)
    ]

    cursor.executemany('''
        INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products
