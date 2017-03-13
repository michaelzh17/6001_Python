#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:59:46 2017

@author: xinyezhang
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    l = len(aStr)
    if l == 0:
        return False
    elif char == aStr[l//2]:
        return True
    elif char > aStr[l//2]:
        return isIn(char, aStr[l//2 + 1: l])
    elif char < aStr[l//2]:
        return isIn(char, aStr[0: l//2])
    