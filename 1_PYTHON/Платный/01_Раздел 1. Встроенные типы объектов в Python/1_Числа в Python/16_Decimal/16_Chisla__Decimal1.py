#!/usr/bin/env python
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
    print (1/3) #0.3333333333333333
    import decimal  #Модуль для более точных вычислений,
                    #чем встроенный в Python механизм вычислений
    print (decimal.Decimal(1) / decimal.Decimal (3))
    #0.3333333333333333333333333333

if __name__ == '__main__':
    main()
