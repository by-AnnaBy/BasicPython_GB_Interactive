#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translations = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
data = []

with open("Task_5-4.txt", "r", encoding="utf-8") as source:
    for line in source:
        data.append(line)

for index, unit in enumerate(data):
    words_list = [word.lower() for word in unit.split(' ')]
    for i, word in enumerate(words_list):
        if word in translations:
            words_list[i] = translations[word].capitalize()
    data[index] = " ".join(words_list)

with open("Task_5-4_translate.txt", "w", encoding="utf-8") as result:
    for unit in data:
        result.write(unit)
