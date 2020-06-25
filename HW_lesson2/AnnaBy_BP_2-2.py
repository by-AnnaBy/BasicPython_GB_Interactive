#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

def main():
    list = [x for x in input('Введи ряд значений через пробел: ').split(' ')]
    prev_value = None

    print('До:    ', list)

    for i in range(0, (len(list) if len(list) % 2 == 0 else len(list) - 1)):
        if i % 2 != 0:
            list[i] = prev_value
        else:
            prev_value = list[i]
            list[i] = list[i + 1]

    print('После: ', list)

if __name__ == '__main__':
        main()
