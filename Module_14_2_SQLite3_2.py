import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

users = [
    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000) for i in range(1, 11)
]
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

cursor.execute('''
    UPDATE Users
    SET balance = 500
    WHERE id % 2 = 1
''')

cursor.execute('''
    DELETE FROM Users
    WHERE (id - 1) % 3 = 0
''')

cursor.execute('''
    SELECT username, email, age, balance
    FROM Users
    WHERE age != 60
''')

rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

#     Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute('DELETE FROM Users WHERE id = 6')

#     Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM Users')
total_count = cursor.fetchone()[0]
#print(f'Общее количество записей: {total_count}')

#     Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
#print(f'Сумма всех балансов: {total_balance}')

#     Вывести в консоль средний баланс всех пользователя.
cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()[0]
print(f'Средний баланс всех пользователей: {average_balance}')

conn.commit()
conn.close()