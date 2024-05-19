# Весь подсчёт должен выполняться одним вызовом функции.
#   Рекомендуется применить рекурсивный вызов функци, для каждой внутренней структуры.
#   Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
#    Для определения типа данного используйте функцию isinstance.


def calculate_structure_sum(summa, data_structure):
    #    print(len(data_structure))
    for i in data_structure:
        #      print(type(i))
        if isinstance(i, dict):
            i = i.items()
            summa = calculate_structure_sum(summa, i)
        elif isinstance(i, list | tuple | set):
            summa = calculate_structure_sum(summa, i)
        elif isinstance(i, int | float):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
    #        print('сумма подсчёт', summa)
    #    print('сумма итого', summa)
    return summa


summa = 0
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(summa, data_structure)
print(f'Результат функции: {result}')
