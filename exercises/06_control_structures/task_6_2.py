# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter IP address in format 10.0.1.1: ')

octs = ip.split('.')
new_list = []
for oct in octs:
    new_list.append(int(oct))

if  new_list[0] >= 1 and  new_list[0] <= 223:
    print('unicast')
elif  new_list[0] >= 224 and  new_list[0] <= 239:
    print('multicast')
elif  new_list[0] == 255 and  new_list[1] == 255 and  new_list[2] == 255 and  new_list[3] == 255:
    print('local broadcast')
elif  new_list[0] == 0 and  new_list[1] == 0 and  new_list[2] == 0 and  new_list[3] == 0:
    print('unassigned')
else:
    print('unused')