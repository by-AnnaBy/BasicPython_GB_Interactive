#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name,
surname,
position (должность),
income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: {"wage": '', "bonus": ''}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


arthur = Position("Arthur", "Doe", "Analyst", {"wage": 10500, "bonus": 1250})

print(arthur.get_full_name())
print(arthur.get_total_income())
