"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""
print('\n', 'Задание 2')

words2 = ["class", "function", "method"]
for i in words2:
    z = bytes(i, encoding='utf-8')
    print(type(z), z, len(z))
