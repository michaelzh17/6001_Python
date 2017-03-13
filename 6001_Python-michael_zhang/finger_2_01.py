#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 21:32:34 2017

@author: xinyezhang
"""

numbXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate  x to toPrint numXs times
while (numbXs > 0):
    toPrint = toPrint + 'X'
    numbXs = numbXs -1
    
print(toPrint)

