my_list = ['киви', 'банан', 'груша', 'ананас', 'мандарин', 'фейхоа']
print('Фрукты (список): ', my_list)
print('Первый и последний: ', my_list[0], my_list[-1])
print('С 3 по 5: ', my_list[2:5])
my_list[2] = 'яблочко'
print('Замена: ', my_list[2])
print('Фрукты_NEW (список): ', my_list)

my_dict = {'table': 'таблица', 'chair': 'стул', 'bed': 'кровать', 'armchair': 'кресто'}
print('Словарь: ', my_dict)
print('Значение для слова "table": ', my_dict['table'])
my_dict.update({'table': 'стол'})
print('Словарь исправленный: ', my_dict)
