#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

data = []

with open("Task_5-7.txt", "r", encoding="utf-8") as file:
    for line in file:
        data.append(line.replace("\n", ""))

companies = {}
average_profit = []
average_indexes = {}

for company in data:
    company_data = [info for info in company.split(" ")]
    if len(company_data) > 4:
        company_data = [" ".join(company_data[:-3]), company_data[-3], company_data[-2], company_data[-1]]
    company_name = company_data[0]
    company_revenue = int(company_data[-2])
    company_expenses = int(company_data[-1])
    company_profit = company_revenue - company_expenses
    companies[company_name] = company_profit
    if company_profit >= 0:
        average_profit.append(company_profit)

try:
    average_indexes["average_profit"] = round(sum(average_profit)/len(average_profit),2)
except ZeroDivisionError:
    average_indexes["average_profit"] = 0

final_list = [companies, average_indexes]

with open("companies_data.json", "w", encoding="utf-8") as json_file:
    json.dump(final_list, json_file, ensure_ascii=False)
