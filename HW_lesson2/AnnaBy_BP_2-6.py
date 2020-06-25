#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
6. *Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def input_status():
    Input_Flag = None
    status = input('Вы хотите ввести новый товар? Y/N: ')

    if status.lower() == 'y':
        Input_Flag = True
    else:
        Input_Flag = False

    return Input_Flag


def product_input():
    product_description = {'название': None, 'цена': None, 'количество': None, 'eд': None}

    product_description['название'] = input('Введите название товара: ')
    product_description['цена'] = input('Введите цену товара: ')
    product_description['количество'] = input('Введите количество единиц товара: ')
    product_description['eд'] = input('Введите единицы (например: шт.): ')

    return product_description

def products_analysis(product_list):
    analysis = {}

    for i, dict in product_list:
        for key, value in dict.items():
            analysis.setdefault(key, [])
            if value not in analysis[key]:
                analysis[key].append(value)

    return analysis


def main():
    products = []

    while input_status():
        product_description = product_input()
        index = len(products) + 1

        products.append((index, product_description))

    print(*products, sep='\n')

    analysis = products_analysis(products)

    print(*analysis.items(), sep=',\n')


if __name__ == '__main__':
    main()
