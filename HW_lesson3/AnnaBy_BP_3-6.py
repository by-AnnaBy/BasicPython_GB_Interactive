#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    """
    Делает первую букву в слове заглавной
    :param word: слово из маленьких латинских букв
    :return: исходное слово с прописной первой буквой
    """
    symbols = list(word)
    symbols[0] = symbols[0].upper()
    return ''.join(symbols)


print(int_func('word'))


def string_convert(string):
    """
    Выводит на экран исходную строку, но каждое слово должно начинаться с заглавной буквы.
    :param string: строка из слов, разделенных пробелом
    :return: None
    """
    words = []
    for element in string.split(' '):
        words.append(int_func(element))
    print(*words, sep=" ")


string_convert('list of words')
