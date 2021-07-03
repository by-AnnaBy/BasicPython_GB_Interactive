#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:

Иванов 23543.12
Петров 13749.32
"""

list_of_people = []
losers = []
salaries = []


def average_value(lst):
    return sum(lst) / len(lst)


with open("Task_5-3.txt", "r", encoding="utf-8") as file:
    for line in file:
        surname = ""
        line = line.replace("\n", "")
        personal_info = [unit for unit in line.split(" ")]
        salary = float(personal_info[::-1][0])
        if len(personal_info) > 2:
            surname = " ".join(personal_info[:-1])
        else:
            surname = personal_info[0]
        list_of_people.append([surname, salary])

for person in list_of_people:
    salaries.append(person[1])
    if person[1] < 20000:
        losers.append(person[0])

average_salary = round(average_value(salaries), 2)

print(f'Средний величина дохода сотрудников составляет {average_salary}$')

if len(losers) > 0:
    print('Список сотрудников, которые получают зарплату меньше 20 тыс.$:')
    for person in losers:
        print(person)
else:
    print('Сотрудников с доходом ниже 20 тыс.$ нет!')
