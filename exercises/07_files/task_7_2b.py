# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

config_file = input('Enter name of config file: ')

with open(config_file) as f, open('new_config_sw1.txt', 'w') as nf:
    for line in f:
        for var in ignore:
            if var in line:
                mark = 1
        if not line.startswith('!') and not mark == 1:
            nf.write(line)
        mark = 0