# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt') as f:
    for line in f:
        list_line = line.split()
        list_line.pop(0)
        list_line.pop(2)
        list_line[1] = list_line[1].strip('[]')
        list_line[2] = list_line[2].rstrip(',')
        list_line[3] = list_line[3].rstrip(',')
        pr, ad, next, last, out = list_line
        print(f'{'Prefix':20}{pr}')
        print(f'{'AD/Metric':20}{ad}')
        print(f'{'Next-Hop':20}{next}')
        print(f'{'Last update':20}{last}')
        print(f'{'Outbound Interface':20}{out}')
        print('\n')