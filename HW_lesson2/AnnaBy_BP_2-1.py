#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

def main():
    list = [1, 'meh', True, 'warrior', None, (8, 13, 21, 34, 55, 89), b'Jesus', 42, False, b'religion']
    types_dictionary = {}

    for i in list:
        types_dictionary.setdefault(type(i), []).append(i)

    print(types_dictionary)



if __name__ == '__main__':
    main()
