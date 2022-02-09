"""1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого: Создать
функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В
этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий
список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия
столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для
этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла); Создать функцию
write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов
функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл; Проверить работу программы
через вызов функции write_to_csv(). """

import csv
from chardet import detect
import re

my_files = {'info_1.txt', 'info_2.txt', 'info_3.txt'}


def get_encode(filename: str) -> str:
    # Функция для определения кодировки
    with open(filename, 'rb') as f:
        content = f.read()
    encoding = detect(content)['encoding']
    return encoding


def get_data(files):
    headers = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = [headers]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for i in files:
        with open(i, 'r', encoding=get_encode(i)) as f:
            data = f.read()
            result = []
            for j in data.split('\n'):
                for header in headers:
                    row_item = re.findall(r'{}:\s+(.+)$'.format(header), j)
                    if row_item:
                        result.append(row_item[0])
                        if header == headers[0]:
                            os_prod_list.append(row_item[0])
                        elif header == headers[1]:
                            os_name_list.append(row_item[0])
                        elif header == headers[2]:
                            os_code_list.append(row_item[0])
                        elif header == headers[3]:
                            os_type_list.append(row_item[0])
        main_data.append(result)
    return main_data


def write_csv(file):
    result = get_data(my_files)
    with open(file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(result)


write_csv('1.csv')
