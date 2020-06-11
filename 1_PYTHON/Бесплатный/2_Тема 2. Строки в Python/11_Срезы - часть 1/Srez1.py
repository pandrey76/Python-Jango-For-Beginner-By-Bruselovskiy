#!/usr/bin/env python
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
    print(len(selo))    #корова
    s = selo[0] #Пример среза
    print(s)    #к

    s = selo [:3] + 'ч'
    print (s)   #корч

    selo = selo[0]
    print(selo) #к

if __name__ == '__main__':
    main()
