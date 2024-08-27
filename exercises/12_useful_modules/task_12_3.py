# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
import tabulate as tb
import ipaddress as ia
from task_12_1 import ping_ip_addresses

def print_ip_table(en_list, disen_list):
    result = {}
    result['Reachable'] = en_list
    result['Unreachable'] = disen_list
    return print(tb.tabulate(result, headers='keys'))

if __name__ == '__main__':
    en_list = ['10.1.1.1', '10.1.1.2']
    disen_list = ['10.1.1.7', '10.1.1.8', '10.1.1.9']
    print_ip_table(en_list, disen_list)
