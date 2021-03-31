#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    """
    Функция сложения двух наибольших аргументов из трёх
    :return: число, результат сложения
    """
    first_max = 0
    sec_max = 0

    for el in [arg_1, arg_2, arg_3]:
        if el >= first_max:
            sec_max = first_max
            first_max = el
        elif el >= sec_max:
            sec_max = el

    return first_max + sec_max


print(my_func(8, 1, 3))
