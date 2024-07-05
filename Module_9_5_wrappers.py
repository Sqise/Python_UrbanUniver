# Напишите 2 функции:
#
#     Функция, которая складывает 3 числа (sum_three)
#     Функция декоратор (is_prime), которая распечатывает "Простое",
#     если результат 1ой функции будет простым числом и "Составное" в противном случае.


def is_prime(func):
    def wrapper(*args):
        summa_origi = func(*args)
        for i in range(2, summa_origi - 1):
            if summa_origi % i == 0:
                return 'Составное'
        return 'Простое'

    return wrapper


@is_prime
def sum_three(a, b, c):
    summa = a + b + c
    print(summa)
    return summa


result = sum_three(2, 3, 6)
print(result)
