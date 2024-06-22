# Создайте в директории проекта текстовый файл с расширением txt
# Добавьте в этот файл следующий текст
# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль, используя оператор with


file_stih = 'Module_7_2_stih.txt'
with open(file_stih, 'w', encoding='utf8') as file:
    stih = ('# -*- coding: utf-8 -*-\n'
            'My soul is dark - Oh! quickly string\n'
            'The harp I yet can brook to hear;\n'
            'And let thy gentle fingers fling\n'
            "Its melting murmurs o'er mine ear.\n"
            'If in this heart a hope be dear,\n'
            'That sound shall charm it forth again:\n'
            'If in these eyes there lurk a tear,\n'
            'Twill flow, and cease to burn my brain.\n'
            'But bid the strain be wild and deep,\n'
            'Nor let thy notes of joy be first:\n'
            'I tell thee, minstrel, I must weep,\n'
            'Or else this heavy heart will burst;\n'
            'For it hath been by sorrow nursed,\n'
            'And ached in sleepless silence, long;\n'
            "And now 'tis doomed to know the worst,\n"
            "And break at once - or yield to song.\n")
    file.write(stih)
with open(file_stih) as file:
    print(file.read())

# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
# Конструкция "with ... as ..." является более удобной и гарантирует закрытие файла в любом случае.
