# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import csv
import re

sh_version_files = glob.glob("17_serialization/sh_vers*")
# print(sh_version_files)

headers = ["hostname", "ios", "image", "uptime"]

def parse_sh_version(out_command):
    '''
    на вход подается вывод команды sh version как строка,
    на выходе кортеж (IOS, image, uptime)
    '''
    result = ()
    temp = []
    regex_ios = r'.+IOS.+Version (?P<ios>\S+)\,.+'
    regex_image = r'System image file is (?P<image>\S+)'
    regex_uptime = r'router uptime is (?P<uptime>.+)'
    lines = out_command.split('\n')
    for line in lines:
        line = line.rstrip()
        match_ios = re.search(regex_ios, line)
        match_image = re.search(regex_image, line)
        match_uptime = re.search(regex_uptime, line)
        if match_ios:
            temp.append(match_ios.group('ios'))
        if match_image:
            image = match_image.group('image').strip('""')
            temp.append(image)
        if match_uptime:
            temp.append(match_uptime.group('uptime'))
        result = tuple(temp)
    return result

def write_inventory_to_csv(data_filenames, csv_filename):
    '''
    два параметра:
    * список имен файлов с выводом sh version
    * имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
    ничего не возвращает

    Функция делает следующее:
    * обработать информацию из каждого файла с выводом sh version:
    * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
    * с помощью функции parse_sh_version, из каждого вывода должна быть получена
    информация ios, image, uptime
    * из имени файла нужно получить имя хоста
    * после этого вся информация должна быть записана в CSV файл
    '''
    regex = r'17_serialization\\sh_version_(?P<host>\S+).txt'
    data = []
    temp = []
    data.append(headers)
    for file in data_filenames:
        host = re.search(regex, file)
        temp.append(host.group('host'))
        with open(file) as f:
            output_data = f.read()
            out_tuple = list(parse_sh_version(output_data))
            temp.extend(out_tuple)
            data.append(temp)
            temp = []
    with open(csv_filename, 'w', newline='') as csvf:
        writer = csv.writer(csvf, quoting=csv.QUOTE_NONNUMERIC)
        for line in data:
            writer.writerow(line)

if __name__ == '__main__':
    write_inventory_to_csv(sh_version_files, '17_serialization/info_versions.csv')