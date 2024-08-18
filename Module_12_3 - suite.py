import unittest


# Часть 1. TestSuit.
#
#     Создайте модуль suite_12_3.py для описания объекта TestSuite.
#     Укажите на него переменной с произвольным названием.

#     Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.

#     Создайте объект класса TextTestRunner, с аргументом verbosity=2.

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


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Ходок")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Бегун")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Спортсмен-1")
        runner2 = Runner("Спортсмен-2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн")
        self.andrey = Runner("Андрей")
        self.nick = Runner("Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results["Усэйн и Ник"] = results

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["Андрей и Ник"] = results

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["Усэйн, Андрей и Ник"] = results


# Создаем объекты тестов
test_walk = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
test_run = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
test_challenge = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
test_usain_and_nick = unittest.TestLoader().loadTestsFromTestCase(TournamentTest)
test_andrey_and_nick = unittest.TestLoader().loadTestsFromTestCase(TournamentTest)
test_usain_andrey_and_nick = unittest.TestLoader().loadTestsFromTestCase(TournamentTest)

# TestSuite, добавляем тесты
test_suite = unittest.TestSuite([test_walk, test_run, test_challenge])
test_suite2 = unittest.TestSuite([test_usain_and_nick, test_andrey_and_nick, test_usain_andrey_and_nick])

runner = unittest.TextTestRunner(verbosity=2)

runner.run(test_suite)
runner.run(test_suite2)
