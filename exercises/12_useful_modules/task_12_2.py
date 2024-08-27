# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

import ipaddress as ip

def convert_ranges_to_ip_list(list_ip_addr):
    first_format = []
    sec_format = []
    for addr in list_ip_addr:
        if len(addr.split('-')) != 2:
            continue
        else:
            temp = addr.split('-')
            if len(temp[1]) <= 3: # for this format 10.1.1.1-10
                oct_1, oct_2, oct_3, oct_4 = temp[0].split('.')
                new_ip = str(oct_1) + '.' + str(oct_2) + '.' + str(oct_3) + '.' + temp[1]
                first_format.append(new_ip)
                list_of_numbers = range(int(temp[0].split('.')[-1]), int(temp[1]))
                for num in list(list_of_numbers):
                    new_ip = str(oct_1) + '.' + str(oct_2) + '.' + str(oct_3) + '.' + str(num)
                    first_format.append(new_ip)
            else: # for this format 10.1.1.1-10.1.1.10
                oct_1_1, oct_2_1, oct_3_1, oct_4_1 = temp[0].split('.')
                list_of_numbers = range(int(temp[0].split('.')[-1]), int(temp[1].split('.')[-1]))
                for num in list(list_of_numbers):
                    new_ip = str(oct_1_1) + '.' + str(oct_2_1) + '.' + str(oct_3_1) + '.' + str(num)
                    sec_format.append(new_ip)
                sec_format.append(temp[1])
    list_ip_addr = list_ip_addr + first_format + sec_format
    list_ip_addr = sorted(list_ip_addr)
    for ip in list_ip_addr:
        if len(ip.split('-')) == 2:
            list_ip_addr.remove(ip)
    return list_ip_addr

if __name__ == '__main__':
    hosts = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    res = convert_ranges_to_ip_list(hosts)
    print(res)