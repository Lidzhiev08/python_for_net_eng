# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

temp = {'access': access_template, 'trunk': trunk_template}
temp_ques = {'access': 'Enter number of VLAN:', 'trunk': 'Enter enable VLANs:'}
regime = input('Enter regime of interface work (access/trunk): ')
type_num = input('Enter type and number of interface: ')
vlans = input(temp_ques.get(regime))

print('interface {}'.format(type_num))
str1 = '\n'.join(temp.get(regime))
print(str1.format(vlans))