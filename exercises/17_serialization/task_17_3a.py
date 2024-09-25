# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import pprint as pp
import yaml

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    '''
        обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую
        топологию в один словарь.
        параметры:
        * list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
        * save_to_filename - имя файла в формате YAML, в который сохранится топология.
        * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
        * топология сохраняется только, если save_to_filename как аргумент указано имя файла
    '''
    result = {}
    d_keys = []
    d_values = []
    temp = {}
    for file in list_of_files:
        with open(file) as f:
            for line in f:
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
            d_keys = []
            d_values = []
    with open(save_to_filename, 'w') as f:
        yaml.dump(result, f)
    return result

if __name__ == '__main__':
    files = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt',
              'sh_cdp_n_r4.txt', 'sh_cdp_n_r5.txt', 'sh_cdp_n_r6.txt']
    new_list = []
    for file in files:
        file = '17_serialization/' + file
        new_list.append(file)

res = generate_topology_from_cdp(new_list, save_to_filename='17_serialization/topology_from_17_3a.yaml')
pp.pprint(res)