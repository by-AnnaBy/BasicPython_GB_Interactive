#!/usr/bin/env python3

TASK = """
Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

seconds = int(input('Введите время в секундах: '))

hours = seconds // 3600
minutes = (seconds - (hours * 3600)) // 60
seconds = seconds - minutes * 60 - hours * 3600


print('{:0>2}:{:0>2}:{:0>2}'.format(hours, minutes, seconds))
