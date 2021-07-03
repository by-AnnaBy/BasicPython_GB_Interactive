#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open("Task_5-2.txt", mode="r", encoding="utf_8") as file:
    line_count = 0
    word_count = []
    for line in file.readlines():
        words = [word for word in line.split(" ") if word != "\n"]
        word_count.append(len(words))
        line_count += 1

print(f'В файле {line_count} строк')
for index, value in enumerate(word_count):
    print(f'В строке номер {index+1} записано {value} слов')
