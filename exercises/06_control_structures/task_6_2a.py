# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделены точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter IP address in format 10.0.1.1: ')

octs = ip.split('.')
for counter in octs:
    if counter.isdigit() == False:
        print('Error')
        break
    elif len(octs) != 4:
        print('Error')
        break
    elif int(counter) <= 0:
        print('Error')
        break
    elif int(counter) >= 255:
        print('Error')
        break
    else:
        new_list = []
        for oct in octs:
            new_list.append(int(oct))

        if new_list[0] >= 1 and new_list[0] <= 223:
            print('unicast')
            break
        elif new_list[0] >= 224 and new_list[0] <= 239:
            print('multicast')
            break
        elif new_list[0] == 255 and new_list[1] == 255 and new_list[2] == 255 and new_list[3] == 255:
            print('local broadcast')
            break
        elif new_list[0] == 0 and new_list[1] == 0 and new_list[2] == 0 and new_list[3] == 0:
            print('unassigned')
            break
        else:
            print('unused')
            break