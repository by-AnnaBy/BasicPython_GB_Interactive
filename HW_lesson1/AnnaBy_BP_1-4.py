#!/usr/bin/env python3

TASK = """
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input('Введите целое положительное число: '))
maximum = 0

while number > 0:
    end = number % 10
    if end > maximum:
        maximum = end
    number = number // 10

print(maximum)
