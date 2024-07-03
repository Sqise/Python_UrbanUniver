# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом
# числовом диапазоне. При создании и инициализации объекта этого класса создаются атрибуты:

# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)

# Значение атрибута start всегда меньше значения атрибута end
# В решении задачи не использовать list, tuple и др. встроенные типы данных.

class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        if start % 2 == 1:
            self.start = start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        result = self.start
        self.start += 2
        return result


start_range = -1
end_range = 1
while int(start_range) < 0 or int(start_range) >= int(end_range):
    start_range = input('Введите начало диапазона: ')
    end_range = input('Введите конец диапазона: ')

range1 = EvenNumbers(int(start_range), int(end_range))
print('Чётные числа:')
for i in range1:
    print(i)
