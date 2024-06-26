# Создайте минимум два своих собственных исключения, наследуя их от класса Exception
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте

class AgeError(Exception):
    pass


class SalaryError(Exception):
    pass


def exc(age, salary):
    offer = age * 2000
    if age < 1 or age > 125:
        raise AgeError
    if age < 14:
        print('Маленький ещё работать!')
    if 14 <= age < 60:
        if salary < 1000 or salary > 1000000:
            raise SalaryError
        if salary <= offer:
            print('Вы приняты!')
        if salary > offer:
            print('Спасибо, мы вам перезвоним!')
    if age >= 60:
        print('Вам на пенсию уже пора!')


try:
    age = int(input('Сколько вам лет? '))
    salary = int(input('Сколько денег в месяц хотите? '))
    exc(age, salary)
except AgeError:
    print("Не бывает такого возраста!")
except SalaryError:
    print("Не бывает такой зарплаты у нас")
except Exception:
    print("Надо было цифры вводить! А вы что наделали?")
except KeyboardInterrupt:
    print("\nЗачем программу прервали?")
