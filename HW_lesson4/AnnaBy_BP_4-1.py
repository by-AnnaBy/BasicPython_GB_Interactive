#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from decimal import Decimal


def salary_calculation(time: Decimal, rate: Decimal, bonus: Decimal = 0) -> Decimal:
    """
    Расчёт заработной платы

    :param time:
    :param rate:
    :param bonus:
    :return:
    """
    return Decimal(time * rate + bonus).quantize(Decimal("1.00"))


def main():
    working_time = input('Введите выработку рабочего времени в часах: ').replace(" ", "")
    salary_rate = input('Введите выработку рабочего времени в часах: ').replace(" ", "")
    bonus_flag = input("Если есть премия, нажмите Y: ")

    working_time = (Decimal(working_time.replace(',', '.')) if working_time.find(',') else Decimal(working_time))
    salary_rate = (Decimal(salary_rate.replace(',', '.')) if salary_rate.find(',') else Decimal(salary_rate))

    if bonus_flag.lower() == 'y':
        bonus_amount = input('Введите размер премии сотруднику: ').replace(" ", "")
        bonus_amount = (Decimal(bonus_amount.replace(',', '.')) if bonus_amount.find(',') else Decimal(bonus_amount))
        total_amount = salary_calculation(time=working_time, rate=salary_rate, bonus=bonus_amount)
    else:
        total_amount = salary_calculation(time=working_time, rate=salary_rate)

    print(f'Размер заработной платы сотруднику за отработанное время составит {total_amount} рублей')


if __name__ == '__main__':
    main()
