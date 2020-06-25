#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
ообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""


def main():
    seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
    month = int(input('Пожалуйста введите порядкой номер месяца от 1 до 12: '))

    for time_of_year, months in seasons.items():
        if month in months:
            print('Это будет', time_of_year.lower())


if __name__ == '__main__':
        main()
