# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan = input('Enter vlan: ')

with open('CAM_table.txt') as f:
    for line in f:
        line = line.split()
        for var in line:
            if var.isdigit() and vlan == var:
                print(f'{line[0]:8}{line[1]:<20}{line[3]:<}')