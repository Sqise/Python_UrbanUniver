# Создайте новый класс Building

# Создайте инициализатор для класса Building, который будет задавать
# целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType

# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors
# и buildingType для сравнения

class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and \
            self.buildingType == other.buildingType


house1 = Building(19, 'Три квартала')
house2 = Building(24, 'Томилино')

print(house1 == house2)
