﻿#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     05.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #Строки - это не изменяемые последовательности, и когда мы работали через
    #строковые методы интерпретатор создавал новую строку.
    #Списки - это изменяемые последовательности.

    dom = ['Кирпич', 'Цемент', 'Песок']
    print (dom) #['Кирпич', 'Цемент', 'Песок']
    zakaz = dom
    zakaz[0] = 'Блоки'
    print (zakaz)   #['Блоки', 'Цемент', 'Песок']

    dom_len = len (dom)
    print (dom_len) #3

    meblia = ['стол', 'стул']
    vsego = dom + meblia
    print (vsego)   #['Блоки', 'Цемент', 'Песок', 'стол', 'стул']

    print (dom * 2)   #['Блоки', 'Цемент', 'Песок', 'Блоки', 'Цемент', 'Песок']

if __name__ == '__main__':
    main()
