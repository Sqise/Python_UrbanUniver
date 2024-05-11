def test(*pos_param, **kw_param):
    print(pos_param, kw_param)


test(1, 10.1, 'Kosovo', False, [1, 2, 3, 4], (5, 6, 7, 8), phone1=8800, phone2=9900)


def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n - 1)


m = ''
while not m.isdigit() or type(m) == 'float':
    m = input('Введите натуральное число для факториала: ')

n = int(m)
print(f'Факториал для {n} будет {factor(n)}')
