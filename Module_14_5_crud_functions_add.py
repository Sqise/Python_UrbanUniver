# Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:

# 1) initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса.
#
# 2) add_user, которая принимает: имя пользователя, почту и возраст.
# Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
# Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.
#
# 3) is_included принимает имя пользователя и возвращает True, если такой пользователь
# есть в таблице Users, в противном случае False. Для получения записей используйте SQL запрос.

import sqlite3


def initiate_db():
    conn = sqlite3.connect('products_add.db')
    cursor = conn.cursor()

    # Создание таблицы Products, если она еще не создана
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создание таблицы Users, если она еще не создана
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
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


def add_user(username, email, age):
    conn = sqlite3.connect('products_add.db')
    cursor = conn.cursor()

    # Добавление нового пользователя с начальным балансом 1000
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('products_add.db')
    cursor = conn.cursor()

    # Проверка наличия пользователя с данным именем
    cursor.execute('''
        SELECT 1 FROM Users WHERE username = ?
    ''', (username,))

    result = cursor.fetchone()

    conn.close()

    # Если результат не пустой, то пользователь существует
    return result is not None


def get_all_products():
    conn = sqlite3.connect('products_add.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products