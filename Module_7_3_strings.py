# Напишите код, который форматирует строки для сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:

# Использование %:
team1, team2 = 'Мастера кода', 'Волшебники данных'
team1_num, team2_num = 5, 6
print("В команде %s участников: %d !" % (team1, team1_num))
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование .format():
score_1, score_2 = 40, 42
team2_time = 18015.2
print("Команда {} решила задач: {} !".format(team2, score_2))
print("{0} решили задачи за {1} с !".format(team2, team2_time))

# Использование f-строк:
tasks_total = 57
time_avg = 355

if score_1 > score_2:
    challenge_result = 'победа команды Мастера кода!'
elif score_1 < score_2:
    challenge_result = 'победа команды Волшебники Данных!'
else:
    challenge_result = 'ничья'

print(f'Команды решили {score_1} и {score_2} задач')
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
