import logging
import unittest


# В модуле tests_12_4.py импортируйте пакет logging
# и настройте basicConfig на следующие параметры:
#
#     Уровень - INFO
#     Режим - запись с заменой('w')
#     Название файла - runner_tests.log
#     Кодировка - UTF-8
#     Формат вывода - на своё усмотрение, обязательная информация:
#     уровень логирования, сообщение логирования.
#
#
# Дополните методы тестирования в классе RunnerTest следующим образом:

# test_walk:
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте отрицательное значение в speed.
#     В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа
#     и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
#
# test_run:
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте что-то кроме строки в name.
#     В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа
#     и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# class RunnerTest(unittest.TestCase):
#     def test_walk(self):
#         runner = Runner("Ходок")
#         for _ in range(10):
#             runner.walk()
#         self.assertEqual(runner.distance, 50)
#
#     def test_run(self):
#         runner = Runner("Бегун")
#         for _ in range(10):
#             runner.run()
#         self.assertEqual(runner.distance, 100)
#
#     def test_challenge(self):
#         runner1 = Runner("Спортсмен1")
#         runner2 = Runner("Спортсмен2")
#         for _ in range(10):
#             runner1.run()
#             runner2.walk()
#         self.assertNotEqual(runner1.distance, runner2.distance)

# Настройка logging
logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format='%(levelname)s - %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Ходок", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(' "test_walk" выполнен успешно ')
        except TypeError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    def test_run(self):
        try:
            runner = Runner(123, 5)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(' "test_run" выполнен успешно ')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')

    def test_challenge(self):
        runner1 = Runner("Спортсмен1")
        runner2 = Runner("Спортсмен2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
