import random

# Задача 1: Составление lambda-функции для выражения list(map("?", first, second))
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


# Задача 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


# Пример использования замыкания
write_to_file = get_advanced_writer('output.txt')
write_to_file('Hello', 123, [1, 2, 3], {'key': 'value'})


# Задача 3: Метод __call__


class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


# Пример использования класса MysticBall
words = ['Yes', 'No', 'Maybe', 'Ask again later']
ball = MysticBall(words)
print(ball())
