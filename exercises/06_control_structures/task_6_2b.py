# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter IP address in format 10.0.1.1: ')

octs = ip.split('.')
bool_var = False

while not bool_var:
    for counter in octs:
        if counter.isdigit() == False:
            print('Error. Only digit.')
            break
        elif int(counter) < 0:
            print('Error. Out of range, negative numbers.')
            break
        elif int(counter) > 255:
            print('Error. Out of range, too much.')
            break
        elif len(octs) != 4:
            print('Error. Enter correct ip.')
            break
    else:
        new_list = []
        for oct in octs:
            new_list.append(int(oct))

        if new_list[0] >= 1 and new_list[0] <= 223:
            print('unicast')
        elif new_list[0] >= 224 and new_list[0] <= 239:
            print('multicast')
        elif new_list[0] == 255 and new_list[1] == 255 and new_list[2] == 255 and new_list[3] == 255:
            print('local broadcast')
        elif new_list[0] == 0 and new_list[1] == 0 and new_list[2] == 0 and new_list[3] == 0:
            print('unassigned')
        else:
            print('unused')
        bool_var = True
        continue
    ip = input('Enter ip again: ')
    octs = ip.split('.')