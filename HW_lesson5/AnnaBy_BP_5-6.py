#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

ENCODING = "utf-8"
data = []

with open("Task_5-6.txt", "r", encoding=ENCODING) as file:
    for line in file:
        data.append(line.replace("\n", ""))

study_plan = {}

for unit in data:
    index = unit.find(":")
    lesson = unit[:index]
    lessons_list = [x for x in unit[index+2:].split(" ")]
    amount_of_lessons = 0
    for info in lessons_list:
        if "(" in info:
            amount_of_lessons += int(info[:info.find("(")])
    study_plan[lesson] = amount_of_lessons

print(study_plan)
