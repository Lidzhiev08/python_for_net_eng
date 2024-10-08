# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(filename):
    access_dict = {}
    trunk_dict = {}
    with open(filename) as f:
        for line in f:
            if 'interface' in line:
                intf = line.split()[-1]
            if 'trunk allowed' in line:
                trunk_dict[intf] = line.split()[-1]
            elif 'access' in line:
                access_dict[intf] = line.split()[-1]
                if line.split()[-1] == 'access':
                    access_dict[intf] = '1'
    result = (access_dict, trunk_dict)
    return result

file_config = input('Enter file name: ')
res = get_int_vlan_map(file_config)
print(res)