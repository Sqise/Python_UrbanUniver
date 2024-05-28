class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('"Такого этажа не существует"')
        else:
            for i in range(new_floor):
                print(i + 1)


house1 = House('ЖК Идиллия', 25)
house2 = House('Лев Толстой', 34)

house1.go_to(10)
house2.go_to(50)

# Если new_floor больше чем self.number_of_floors или меньше 1,
# то вывести строку "Такого этажа не существует".
