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
    #по умолчанию в Python и так встроенны опреации с высокой точностью, но
    #если вам необходимо что-то дополнительное, то в модуле math уже есть
    #дополнительные математические опреации например операции с логарифмами,
    #тригонометрические функции и т.д.

    import math
    x = 10
    y = 7

    a = x / y
    print ( a ) # 1.4285714285714286

    a = x // y
    print ( a ) # 1

    #math.trunc(x) - значение x обрезаются до целого числа.
    #Делегат x.__trunc__()
    a = math.trunc (x / y)
    print ( a ) # 1

if __name__ == '__main__':
    main()
