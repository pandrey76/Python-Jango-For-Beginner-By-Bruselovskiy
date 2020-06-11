﻿#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     26.06.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    selo = 'корова'
    s = selo[:] #двоеточие это граница
    print(s)    #корова

    s = selo[1:] #все кроме первого символа
    print(s)    #орова

    s = selo[2:] #все кроме первого и второго символа
    print(s)    #рова

    s = selo[2:] * 3
    print(s)    #ровароварова

    s = selo[1:3]   #Один не включая 3 элемент
    print(s)    #ор

    s = selo[-1]    #Python может работать и в обратном порядке,
                    #т.е. последний символ в последовательности
                    #имеет индекс -1
    print(s)    #а

    s = selo[:-1]
    print(s)    #коров

    s = selo[:-2]
    print(s)    #коро

    s = selo[-2:]
    print(s)    #ва

    s = selo[-2:-2]
    print(s)    #ничего не будет выведено пустая последовательность ""

    s = selo[0:-1]
    print(s)    #коров


#Мы ограничиваем последовательность справа и слева и
#получаем то, что по середине.


if __name__ == '__main__':
    main()
