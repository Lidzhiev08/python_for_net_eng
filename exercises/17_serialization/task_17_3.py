# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

def parse_sh_cdp_neighbors(out_com):
    result = {}
    d_keys = []
    d_values = []
    temp = {}
    lines = out_com.split('\n') #list of lines of commands
    for line in lines:
        line = line.rstrip()
        if len(line.split('>')) == 2:
            host = line.split('>')[0] #name host
        if line == '':
            continue
        if len(line.split()) > 5 and line.split()[3].isdigit():
            line = line.split()
            value = line[-2] + ' ' + line[-1] # порт подключенного устройства
            key = line[1] + ' ' + line[2] #порт хоста
            temp[line[0]] = value
            d_values.append(temp)
            d_keys.append(key)
            temp = {} #delete dict
    res_value = dict(zip(d_keys, d_values))
    result[host] = res_value
    return result

if __name__ == '__main__':
    with open('17_serialization/sh_cdp_n_sw1.txt') as f:
        out_command = f.read()
        res = parse_sh_cdp_neighbors(out_command)
        print(res)