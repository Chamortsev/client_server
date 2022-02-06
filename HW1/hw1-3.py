"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

print('\n', 'Задание 3')

words3 = ['attribute', 'класс', 'функция', 'type']
for i in words3:
    try:
        print(i, i.encode(encoding='ascii'))
    except UnicodeEncodeError:
        print(f'ОШИБКА: слово "{i}" невозможно записать в байтовом типе')
