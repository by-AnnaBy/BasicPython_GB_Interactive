#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

range_len = random.randint(1, 1000)


with open("Task_5-5.txt", "w") as file:
    for i in range(range_len - 1):
        file.write(str(random.randint(1, 1000)))
        file.write(" ")
    file.write(str(random.randint(1, 1000)))


with open("Task_5-5.txt", "r") as file:
    line = file.readline()


line = [int(x) for x in line.split(" ")]
print('Сумма чисел в файле равна:', sum(line))
