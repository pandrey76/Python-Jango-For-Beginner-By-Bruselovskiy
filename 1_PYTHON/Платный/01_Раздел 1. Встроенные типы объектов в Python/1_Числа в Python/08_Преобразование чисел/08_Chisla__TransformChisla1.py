﻿#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     04.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    # Правила старшинства
    print (5 * 5 + 6 * 6)   # 61
    print (6 + 5 * 5 )   # 31
    print (5 * (5 + 6))   # 55
    # Преобразование целых и вещественных чисел
    print (6 * 3.8) # 22.799999999999997
                    # Если нам нужна еще большая точность,
                    #то мы будем использовать модуль decimal.
    # Философия Python - простое не должно быть сложным.
    # Что в данном случае сделал Python, он 6 перевел в вещественное
    #число 6.0.
    print (6.0 * 3.8) #22.799999999999997

    # Преобразование чисел int и float

    # int должен усекать дробную часть
    print (6 * int (3.8))   # 18
                            # Дробную часть Python отбросил.

    # float преобразует целое число в вещественное
    print (float (6) * 3.8) # 22.799999999999997

    # Функция round
    # round (x,[n]) - Округляет до ближайшего кратного 10 в степени минус n
    #                 (только для чисел с плавающей точкой)
    print (round (float (6) * 3.8)) # 23
    print (round ( 6 * 3.8)) # 23

    print ( 5.5 * 6.3) # 34.65
    print ( round (5.5 * 6.3)) # 35

if __name__ == '__main__':
    main()
