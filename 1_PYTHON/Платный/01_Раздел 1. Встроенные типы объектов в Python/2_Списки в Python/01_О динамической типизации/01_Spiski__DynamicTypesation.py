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
    #Пример на другом языке
    #1. Объявить, что мы создаём переменную.
    #2. Указать какую.
    #3. Выделить память.

    #Python ничего не нужно, что в предыдущем примере, просто пишите чистый код,
    #Python сам определяет, автоматически типы данных.

    A = 3
    print (A)   #3
    #Что теоретически делает Python:
    #    1. Первым делом он определяет объект (3 - числовое значение);
    #    2. Интерпретатор создаёт переменную, которую мы написали (A);
    #    3. Создаёт между 3 и A ссылочку, т.е. A теперь ссылается
    #       на число 3 и выделена  память 2 бита.

    #Уборка мусора

    B = 3
    B = 'Вася'
    print (B)   #Вася

    C = 3
    D = 1 + C
    print (D)   #4

if __name__ == '__main__':
    main()
