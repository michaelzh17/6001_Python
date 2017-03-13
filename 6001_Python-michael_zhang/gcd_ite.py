#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:16:38 2017

@author: xinyezhang
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    for i in range(0,min(a,b)):
         if (max(a, b)%(min(a,b) - i) == 0 and min(a, b)%(min(a,b)- i) == 0):
              return min(a, b) - i
              
"""
#another thought official version
def gcdIter(a, b): 
    ''' 
    a, b: positive integers 
    returns: a positive integer, the greatest common divisor of a & b. 
    ''' 
    testValue = min(a, b) 
    # Keep looping until testValue divides both a & b evenly 
    while a % testValue != 0 or b % testValue != 0: 
        testValue -= 1 
    return testValue
"""
