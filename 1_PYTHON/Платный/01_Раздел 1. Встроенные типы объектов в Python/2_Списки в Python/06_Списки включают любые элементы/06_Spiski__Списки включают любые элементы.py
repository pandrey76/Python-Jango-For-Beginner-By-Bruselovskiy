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
    #Списки могут содержать в себе абсолютно любые элементы
    sad = ['Грабли','Лопаты','Лейки']
    dom1 = ['Кирпич','Цемент','Доски','25', 56 ]
    print (dom1)#['Кирпич', 'Цемент', 'Доски', '25', 56]

    dom2 = ['Кирпич','Цемент','Доски','25', 56, sad ]
    print (dom2)#['Кирпич', 'Цемент', 'Доски', '25',
               #56, ['Грабли', 'Лопаты', 'Лейки']]

    summa = sad + dom1
    print (summa)#['Грабли', 'Лопаты', 'Лейки', 'Кирпич',
                 #'Цемент', 'Доски', '25', 56]

    #sad2 = ['Грабли','Лопаты','Лейки'] + '36'           #TypeError: can only
                                          #concatenate list (not "str") to list
    #Здесь мы снова сталкиваемся с динамической типизацией и полиморфизмом
    #Складывать можно только идентичные элементы, поэтому интерпретатор
    #нам предлагает преобразовать или в список или в строку.

    #str()-преобразование списка в строку
    #list()-преобразование строки в список

    #Основной принцип полиморфизма действие зависит от участвующих объектов

    #Более внимательно отнестись к встроенным функциям Python
    #http://docs.python.org/3/library/functions.html


    sad2 = str(sad) + '36'
    print (sad2)#['Грабли', 'Лопаты', 'Лейки']36
    sad3 = sad + list('36')
    print (sad3)#['Грабли', 'Лопаты', 'Лейки', '3', '6']

    sad += '36'
    print (sad) #['Грабли', 'Лопаты', 'Лейки', '3', '6']

    #sad += 36 #TypeError: 'int' object is not iterable

if __name__ == '__main__':
    main()
