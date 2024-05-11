def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(10, 'qwerty')
print_params([1.3, 'string'], (12, 1, {'audi', 'mercedex'}), False)
# print_params('Italy', 'Spain', 'Mexico', 'Zanzibar')
# Вызов не сработает, поскольку число параметров больше чем нужно
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, 10.101, 321]
values_dict = {'a': 0, 'b': 'нестрока', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [(10, 54), ['abc', 'dfg']]
print_params(*values_list_2, 42)  # Вызов сработает, но список распакуется
