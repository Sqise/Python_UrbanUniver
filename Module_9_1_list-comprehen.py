#     Дан список целых чисел, примените функции map и filter так,
#     чтобы в конечном списке оставить нечётные квадраты чисел
#     [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]    ->     [1, 25, 49, 121, 1225, 7921]

def square(x):
    return x ** 2


def odd(x):
    return x % 2


input_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
filter_ = list(filter(odd, input_))
output_ = list(map(square, filter_))
print(output_)
