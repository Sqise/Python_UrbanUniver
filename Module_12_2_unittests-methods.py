import unittest


# Скачайте исходный код, который нужно обложить тестами с GitHub.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут
# сохраняться результаты всех тестов.
# setUp - метод, где создаются 3 объекта:
#     Бегун по имени Усэйн, со скоростью 10.
#     Бегун по имени Андрей, со скоростью 9.
#     Бегун по имени Ник, со скоростью 3.
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
# У объекта класса Tournament запускается метод start, который возвращает словарь в переменную
# all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из
# all_results и предполагаемое имя последнего бегуна.

# Напишите 3 таких метода, где в забегах участвуют Усэйн и Ник, Андрей и Ник, Усэйн, Андрей и Ник.

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results["Усэйн и Ник"] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["Андрей и Ник"] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["Усэйн, Андрей и Ник"] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")


if __name__ == '__main__':
    unittest.main()
