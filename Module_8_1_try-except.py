#     Реализуйте следующую функцию:
#     add_everything_up, будет складывать числа(int, float) и строки(str)

def add_everything_up(a, b):
    print(f'Результат: {a + b}')


a = input('Введите слагаемое 1:')
b = input('Введите слагаемое 2:')

try:
    if float(a) - int(float(a)) == 0:
        a = int(a)
    else:
        a = float(a)
    if float(b) - int(float(b)) == 0:
        b = int(b)
    else:
        b = float(b)
    add_everything_up(a, b)
except ValueError:
    a = str(a)
    b = str(b)
    add_everything_up(a, b)
