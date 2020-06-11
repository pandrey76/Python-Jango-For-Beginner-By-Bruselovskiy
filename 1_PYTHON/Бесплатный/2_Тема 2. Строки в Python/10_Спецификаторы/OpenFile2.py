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
    file = open(r'e:\t1.txt', 'r')#Используем спецификатор 'r'
    for line in file:
        x = line.split(",")#обратить внимание на отступы
        print(x[0],'\t')


if __name__ == '__main__':
    main()
