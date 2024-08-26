import sqlite3

# Создайте файл базы данных not_telegram.db и подключитесь к ней,
# используя встроенную библиотеку sqlite3. # Создайте объект курсора.
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создайте таблицу Users.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# ...
# User10, example10@gmail.com, 100, 1000
users = [
    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000) for i in range(1, 11)
]
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

# Обновите balance на 500 у каждой 2-й записи начиная с 1-й на 500
cursor.execute('''
    UPDATE Users
    SET balance = 500
    WHERE id % 2 = 1
''')

# Удалите каждую 3-ю запись в таблице начиная с 1-й
cursor.execute('''
    DELETE FROM Users
    WHERE (id - 1) % 3 = 0
''')

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60
# и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute('''
    SELECT username, email, age, balance
    FROM Users
    WHERE age != 60
''')

rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

conn.commit()
conn.close()
