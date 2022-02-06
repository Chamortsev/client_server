"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
тип на кириллице.
"""

import subprocess
from sys import platform
import platform as p
import chardet
print(platform)

param = '-n' if p.system().lower() == 'windows' else '-c'
sites = ['yandex.ru', 'youtube.com']
max_lines = 5

for site in sites:
    result = subprocess.Popen(['ping', param, '2', site], stdout=subprocess.PIPE)
    print(site)
    for line in result.stdout:
        result = chardet.detect(line)
        print('result =', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
