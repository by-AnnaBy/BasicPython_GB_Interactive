#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def personal_data(name, surname, birthyear, city, email, mobnumber):
    print(name, surname, birthyear, city, email, mobnumber, end='', sep=' ')


personal_data(name='John',
              birthyear='1970',
              city='New York',
              email='wjohn@ya.hoo',
              mobnumber='8-888-88-8',
              surname='Wick')
