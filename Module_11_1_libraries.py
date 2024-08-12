#     Выберите одну или несколько сторонних библиотек Python и изучите документацию
#     к ней(ним), ознакомьтесь с их основными возможностями и функциями.
#
# Если вы выбрали:
#
#     numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
#     matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
#     pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter

# 1. NumPy: создать массив и применить математические операции
array = np.array([1, 2, 3, 4, 5])
squared_array = array ** 2  # Квадраты элементов массива
mean_value = np.mean(array)  # Среднее значение
std_deviation = np.std(array)  # Средне-квадратическое отклонение

print("Исходный массив:", array)
print("Квадраты элементов массива:", squared_array)
print("Средне-арифметическое значение:", mean_value)
print("Средне-квадратическое отклонение:", std_deviation)

# 2. Matplotlib: визуализировать данные и сохранить график

plt.figure(figsize=(10, 5))  # Установить параметры графика

# Линейный график
plt.plot(array, label='Исходный массив', marker='o', color='blue')
plt.plot(squared_array, label='Квадраты чисел массива', marker='x', color='orange')

# Оформить график
plt.title('Визуализация массива и его квадратов')
plt.xlabel('Индекс массива')
plt.ylabel('Значение')
plt.xticks(np.arange(len(array)))
plt.legend()
plt.grid()

plt.savefig('Figure_1.jpg')  # Сохранить график в файл в формате JPG
plt.show()  # Показать график

# 3. Pillow: обработать сохранённое изображение

image = Image.open('Figure_1.jpg')  # Открыть изображение
resized_image = image.resize((800, 400))  # Уменьшить размер
blurred_image = resized_image.filter(ImageFilter.GaussianBlur(5))  # Размыть с радиусом 5
blurred_image.save('Figure_1_blurred.png', 'PNG')  # Сохранить в формате PNG
blurred_image.show()  # Показать измененное изображение
