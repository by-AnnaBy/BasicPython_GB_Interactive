#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

** Подсказка:
** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_1(x, y):
    """
    Функция возведения числа x в степень y через оператор ** (вариант 1)
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: результат возведения в степень
    """
    try:
        return x ** y
    except ZeroDivisionError:
        return 0


def my_func_2(x, y):
    """
    Функция возведения числа x в степень y через оператор цикл (вариант 2)
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: результат возведения в степень
    """
    try:
        result = 1
        for iteration in range(0, (y * -1)):
            result = result / x
        return result
    except ZeroDivisionError:
        return 0


print(my_func_1(0, -5))
print(my_func_2(0, -5))
