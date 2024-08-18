import unittest


# Часть 2. Пропуск тестов.
#
#     Классы RunnerTest дополнить атрибутом is_frozen = False
#     и TournamentTest атрибутом is_frozen = True.

#     Напишите соответствующий декоратор к каждому методу (кроме "class method"),
#     который при значении is_frozen = False будет выполнять тесты,
#     а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.

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


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        if not self.is_frozen:
            runner = Runner("Ходок")
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        else:
            print("Тесты в этом кейсе заморожены")

    def test_run(self):
        if not self.is_frozen:
            runner = Runner("Бегун")
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        else:
            print("Тесты в этом кейсе заморожены")

    def test_challenge(self):
        if not self.is_frozen:
            runner1 = Runner("Спортсмен1")
            runner2 = Runner("Спортсмен2")
            for _ in range(10):
                runner1.run()
                runner2.walk()
            self.assertNotEqual(runner1.distance, runner2.distance)
        else:
            print("Тесты в этом кейсе заморожены")


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
    is_frozen = True

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
        if not self.is_frozen:
            tournament = Tournament(90, self.usain, self.nick)
            results = tournament.start()
            self.all_results["Усэйн и Ник"] = results
            last_place = max(results.keys())
            self.assertTrue(results[last_place] == "Ник")
        else:
            print("Тесты в этом кейсе заморожены")

    def test_andrey_and_nick(self):
        if not self.is_frozen:
            tournament = Tournament(90, self.andrey, self.nick)
            results = tournament.start()
            self.all_results["Андрей и Ник"] = results
            last_place = max(results.keys())
            self.assertTrue(results[last_place] == "Ник")
        else:
            print("Тесты в этом кейсе заморожены")

    def test_usain_andrey_and_nick(self):
        if not self.is_frozen:
            tournament = Tournament(90, self.usain, self.andrey, self.nick)
            results = tournament.start()
            self.all_results["Усэйн, Андрей и Ник"] = results
            last_place = max(results.keys())
            self.assertTrue(results[last_place] == "Ник")
        else:
            print("Тесты в этом кейсе заморожены")


if __name__ == '__main__':
    unittest.main()
