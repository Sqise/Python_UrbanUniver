# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них
# должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.


class Figure:
    def __init__(self, __color=(0, 0, 0), __sides=0, sides_count=0, filled=True):
        self.__color = __color
        self.__sides_count = sides_count
        self.filled = filled
        if __sides == 0:
            __sides = 1
        sides_list = []
        for i in range(sides_count):
            sides_list.append(__sides)
        self.__sides = sides_list

    def get_color(self):
        """Метод get_color, возвращает список RGB цветов."""
        __color = list(self.__color)
        return __color

    def __is_valid_color(self):
        """Метод __is_valid_color - служебный, принимает параметры r, g, b,
        проверяет корректность переданных значений перед установкой нового цвета.
        Корректный цвет: r, g и b - целые числа от 0 до 255 (включительно)."""
        pass

    def set_color(self, r, g, b):
        """Метод set_color принимает параметры r, g, b - числа и изменяет атрибут
        __color на соответствующие значения, предварительно проверив их на корректность.
        Если введены некорректные данные, то цвет остаётся прежним."""
        if 0 < r < 255 or 0 < g < 255 or 0 < b < 255:
            self.__color = (r, g, b)
            return self.__color

    def set_sides(self, *args):
        """Метод set_sides принимает неограниченное кол-во сторон, проверяет
        корректность переданных данных, если данные корректны, то меняет
        __sides на новый список, если нет, то оставляет прежние."""
        if len(args) == self.__sides_count:
            self.__sides = args
        return list(self.__sides)

    def __is_valid_sides(self, *arrs):
        """Метод is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        возвращает True если все стороны целые положительные числа и кол-во
        новых сторон совпадает с текущим, False - во всех остальных случаях."""
        for i in arrs:
            if i <= 0:
                return False
        return True

    def __len__(self):
        """Метод __len__ должен возвращать периметр фигуры"""
        return sum(self.__sides)


class Circle(Figure):
    def __init__(self, __color=(0, 0, 0), __sides=0, sides_count=0, filled=True):
        self.__sides_count = 1
        super().__init__(__color, __sides, self.__sides_count, filled)
        self.radius = self._Figure__sides[0] / (2 * 3.14159265359)

    def get_square(self):
        """Метод get_square возвращает площадь круга (можно рассчитать
        как через длину, так и через радиус)"""
        square_circ = self.__sides[0] ** 2 / (4 * 3.14159265359)
        return square_circ


class Triangle(Figure):
    def __init__(self, __color=(0, 0, 0), __sides=0, sides_count=0, filled=True):
        self.__sides_count = 3
        super().__init__(__color, __sides, self.__sides_count, filled)
        self.__height = self._Figure__sides[0] * 3 ** 0.5 / 2

    def get_square(self):
        """Метод get_square возвращает площадь треугольника."""
        square_tria = self.__sides[0] ** 2 * 3 ** 0.5 / 4
        return square_tria


class Cube(Figure):
    def __init__(self, __color=(0, 0, 0), __sides=0, sides_count=0, filled=True):
        self.__sides_count = 12
        super().__init__(__color, __sides, self.__sides_count, filled)

    def get_volume(self):
        """Метод get_volume, возвращает объём куба."""
        volume_cube = self._Figure__sides[0] ** 3
        return volume_cube


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.set_sides())
print(circle1.set_sides())
#
# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
