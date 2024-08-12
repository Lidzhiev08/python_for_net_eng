# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result = {}
    device = command_output.split('>')[0]
    device = device.strip('\n')
    list_of_pieces = command_output.split('\n')                  #разбиваем вывод команды на строки
    list_of_pieces = [var.strip() for var in list_of_pieces]     #убираем пробелы и отступы в строках
    list_keys = []                                               #список ключей для словаря
    list_values = []
    flag = 1
    for line in list_of_pieces:
        if flag < 4:
            flag += 1
            continue
        else:
            '''##########################################''' #ключи словаря
            if line == '':
                break
            temp = []     # <- вспомогательные списки
            temp_2 = []   # <-|
            key_dict = []
            value_dict = []
            key_dict.append(device)
            temp.append(line.split()[1])
            temp.append(line.split()[2])
            local_intf = ''.join(temp)
            key_dict.append(local_intf)
            list_keys.append(key_dict)

            '''#########################################''' #значения словаря
            value_dict.append(line.split()[0])     #добавление устройств, подключенных к sw1
            temp_2.append(line.split()[-2])
            temp_2.append(line.split()[-1])
            port_id = ''.join(temp_2)
            value_dict.append(port_id)
            list_values.append(value_dict)
            flag += 1

    list_keys = [tuple(key) for key in list_keys]
    list_values = [tuple(value) for value in list_values]
    result = dict(zip(list_keys, list_values))
    return result

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f, open("new_sh_cdp_n_sw1.txt", 'w+') as nsf:
        for line in f:
            if line == '\n':
                continue
            else:
                nsf.write(line)
        print(parse_cdp_neighbors(nsf.read()))

    with open("sh_cdp_n_r3.txt") as f, open("new_sh_cdp_n_r3.txt", 'w+') as nrf:
        for line in f:
            if line == '\n':
                continue
            else:
                nrf.write(line)
        print(parse_cdp_neighbors(nrf.read()))