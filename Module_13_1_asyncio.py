# Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
# Напишите асинхронную функцию start_strongman(name, power), где name - имя силача,
# power - его подъёмная мощность. Реализуйте следующую логику в функции:
#
#     В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
#     После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой,
#     обратно пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
#     В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'

import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шаров.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('StrongMan', 2))
    task2 = asyncio.create_task(start_strongman('PowerMan', 3))
    task3 = asyncio.create_task(start_strongman('ThunderStorm', 1.5))

    await task1
    await task2
    await task3


asyncio.run(start_tournament())
