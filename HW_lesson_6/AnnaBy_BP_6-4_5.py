#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

5. (Продолжение задания 4) Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self):
        print(f'Машина {self.name} начала движение.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        print(f'Машина {self.name} начала движение.')

    def show_speed(self):
        print(f'Машина {self.name} движется со скоростью {self.speed} км/ч.')

    def info(self):
        print(f'Машина {self.name} цвета {self.color} со скоростью {self.speed} км/ч.. Является полицейской - {self.is_police}')


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} превышает допустимый лимит скорости (60 км/ч)! Пожалуйста, сбавьте скорость.')
        else:
            print(f'Машина {self.name} движется со скоростью {self.speed} км/ч.')


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} превышает допустимый лимит скорости (40 км/ч)! Пожалуйста, сбавьте скорость.')
        else:
            print(f'Машина {self.name} движется со скоростью {self.speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


volga = PoliceCar("Волга", "черный", 85)
hundai = TownCar("Хёндай Солярис", "желтый", 65)
uazik = WorkCar("Вазик", "серый", 39)
lamborgini = SportCar("Ламборджини", "красный", 145)

volga.info()
hundai.show_speed()
hundai.speed = 59
hundai.show_speed()