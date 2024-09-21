# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import csv
import re

def write_dhcp_snooping_to_csv(filenames, output):
    headers = ['switch','mac','ip','vlan','interface']
    data = []
    data.append(headers)
    regex = r'(?P<mac>(\S+\:)\S+) +(?P<ip>(\S+\.)\S+).+ +(?P<vlan>\d+) +(?P<intf>\S+)'
    regex_two = r'17_serialization/(?P<device>\S+)_dhcp_snooping.txt'
    for file in filenames:
        with open(file) as f:
            device = re.search(regex_two, file)
            for line in f:
                match = re.search(regex, line)
                if match:
                    temp = [device.group('device'), match.group('mac'), match.group('ip'), match.group('vlan'), match.group('intf')]
                    data.append(temp)
                    temp = []
    with open(output, 'w', newline='') as csvf:
        writer = csv.writer(csvf)
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    files = ['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    new_files = []
    for file in files:
        file = '17_serialization/' + file
        new_files.append(file)
    write_dhcp_snooping_to_csv(new_files, '17_serialization/dhcp_snooping.csv')
    with open('17_serialization/dhcp_snooping.csv') as f:
        print(f.read())