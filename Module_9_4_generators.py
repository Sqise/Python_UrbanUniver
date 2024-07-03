# Напишите функцию-генератор all_variants(text), которая принимает строку text
# и возвращает объект-генератор, при каждой итерации которого
# будет возвращаться подпоследовательности переданной строки.

def all_variants(text):
    j = 0
    while j < len(text):
        i = 0
        while i < len(text) - j:
            yield text[i:i + j + 1]
            i += 1
        j += 1


string = input("Введите строку: ")
generator = all_variants(string)

for element in generator:
    print(element)
