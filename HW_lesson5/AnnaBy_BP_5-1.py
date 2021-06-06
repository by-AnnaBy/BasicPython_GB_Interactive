#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

# вариант 1

new_file = open("task1.txt", "w")
line = None

while True:
    line = input("Введите строку или просто нажмите Enter для окончания:")
    if line == "":
        break
    else:
        new_file.write(f'{line}\n')

new_file.close()

# вариант 2

try:
    with open("task1-2.txt", "x") as file:
        line = input("Введите строку или просто нажмите Enter для окончания:")
        while line != "":
            file.write(f'{line}\n')
            line = input("Введите строку или просто нажмите Enter для окончания:")
except IOError:
    print("Произошла ошибка ввода-вывода!")
