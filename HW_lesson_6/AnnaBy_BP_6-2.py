#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.

Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, meter_mass,thickness):
        return self._length * self._width * int(meter_mass) * int(thickness)


country_road = Road(5000, 20)
print(f'Масса асфальта для покрытия дороги равна {country_road.asphalt_mass(25, 5)} кг')
