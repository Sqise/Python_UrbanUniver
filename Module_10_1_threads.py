import time
import datetime
import threading


# Создать функцию write_words(word_count, file_name),
# где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
# в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)
    print('Завершилась запись в файл', file_name)


# Вызовите 4 раза функцию write_words, передав в неё следующие значения:
start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = datetime.datetime.now()
print(f'Затраченное время: {end - start}')

# Создайте 4 потока для вызова этой функции со следующими аргументами для функции:
th1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
th2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
th3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
th4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.
start = datetime.datetime.now()
th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()
end = datetime.datetime.now()
print(f'Затраченное время: {end - start}')
