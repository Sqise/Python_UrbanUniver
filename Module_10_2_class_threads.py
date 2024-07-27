import threading
import time


# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
#     Атрибут name - имя рыцаря. (str)
#     Атрибут power - сила рыцаря. (int)
#     Метод run, в котором рыцарь будет сражаться с врагами.
class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    #     При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
    #     Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
    #     В процессе сражения количество врагов уменьшается на power текущего рыцаря.

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemy = 100
        days = 1
        while enemy - self.power > 0:
            print(f'{self.name} сражается {days}й день, осталось {enemy - self.power} воинов.')
            enemy -= self.power
            days += 1
            time.sleep(1)
        #     Выведите на экран строку об окончании битв.
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


#     Создайте и запустите 2 потока на основе класса Knight.
rytsar1 = Knight('Peter', 15)
rytsar2 = Knight('Vasily', 11)

rytsar1.start()
rytsar2.start()
