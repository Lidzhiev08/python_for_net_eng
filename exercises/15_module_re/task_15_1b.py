# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re
def get_ip_from_cfg(filename):
    res_dict = {}
    list_keys = []
    list_values = []
    regex_intf = (r'interface (?P<intf>\S+)')
    regex = (r'ip address (?P<ip_addr>(\d+\.)+\S+) (?P<mask>(\d+\.)+\S+)')
    with open(filename) as f:
        for line in f:
            match_intf = re.search(regex_intf, line)
            if match_intf:
                list_keys.append(match_intf.group('intf'))
                continue
            match = re.search(regex, line)
            if 'secondary' in line:
                list_values[-1] = [list_values[-1][0], (match.group('ip_addr'), match.group('mask'))]
                continue
            if match:
                temp_tuple = (match.group('ip_addr'), match.group('mask'))
                list_values.append([temp_tuple])
                temp_tuple = []
                continue
            if 'no ip address' in line or 'ip unnumbered' in line:
                del_elem = list_keys.pop()
            res_dict = dict(zip(list_keys, list_values))
    return res_dict

if __name__ == '__main__':
    test_list = get_ip_from_cfg('config_r2.txt')
    print(test_list)