# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess as sp
import ipaddress as ia

def ping_ip_addresses(list_ip_address):
    en_list = []
    disen_list = []
    for ip_addr in list_ip_address:
        ping_command = sp.run(['ping', '-n', '3', ip_addr], stdout=sp.DEVNULL,
                              stderr=sp.DEVNULL, encoding='cp1251')
        if ping_command.returncode == 0:
            en_list.append(ip_addr)
        else:
            disen_list.append(ip_addr)
    result = (en_list, disen_list)
    return result

if __name__ == '__main__':
    subnet_1 = ia.ip_network('192.168.217.240/28')
    subnet_1 = list(subnet_1.hosts())
    subnet_1 = [str(ip) for ip in subnet_1]

    res_1 = ping_ip_addresses(subnet_1)
    print(res_1)