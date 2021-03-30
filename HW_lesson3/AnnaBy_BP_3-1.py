#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(dividend, divisor):
    """
    Функция деления
    :param dividend: делимое
    :param divisor: делитель
    :return: результат деления
    """
    if divisor == 0:
        print('Деление на ноль невозможно')
    else:
        return dividend / divisor


def main():
    number_one = float(input('Введите делимое:'))
    number_two = float(input('Введите делитель:'))
    print(division(number_one, number_two))


if __name__ == '__main__':
    main()
