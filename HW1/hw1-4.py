"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

print('\n', 'Задание 4')

words4 = ['разработка', 'администрирование', 'protocol', 'standard']

for i in words4:
    print('В байтовом виде', i.encode("utf8"))
    print('Обратное преобразование', i.encode("utf8").decode())
