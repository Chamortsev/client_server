"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale
from chardet import detect

print('Задание 6')
info = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w+') as f:
    for i in info:
        f.write(i + '\n')
    f.seek(0)
print(f)

file_coding = locale.getpreferredencoding()
with open('test_file.txt', 'r', encoding=file_coding) as f:
    for i in f:
        print(i)
    f.seek(0)


with open('test_file.txt', 'rb') as f:
    CONTENT = f.read()
ENCODING = detect(CONTENT)['encoding']
print(ENCODING)