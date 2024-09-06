# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
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
            if match:
                temp_tuple = (match.group('ip_addr'), match.group('mask'))
                list_values.append(temp_tuple)
                temp_tuple = []
                continue
            if 'no ip address' in line or 'ip unnumbered' in line:
                del_elem = list_keys.pop()
            res_dict = dict(zip(list_keys, list_values))
    return res_dict

if __name__ == '__main__':
    test_list = get_ip_from_cfg('config_r1.txt')
    print(test_list)