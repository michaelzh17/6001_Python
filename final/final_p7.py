#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:40:34 2017

@author: xinyezhang
"""

def general_poly_3(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def poly(x):
        f = ''
        for k in range(len(L)):
            f += str(L[k]) + ' * ' + x + ' ** ' + str(len(L)-1) + '+'
        f = f[:-1]
        return eval(f)
    return poly
    
def general_poly_1(L):
    f = 'lambda x:'
    l = len(L) - 1
    for k in range(len(L)):
        f += str(L[k]) + "*x**" + str(l) + "+"
        l -= 1
    f = f[:-1]
    return eval(f)

def general_poly_2(L):
    return lambda x: sum(c*(x**i) for i, c in enumerate(reversed(L)))

def general_poly(L):  

    def f(x):
        return sum(c*(x**i) for i, c in enumerate(reversed(L)))

    return f
    
def general_poly (L):
    def function(x):
        value = 0
        myList = L[::-1]
        for n in range(len(myList)):            
            value += myList[n] * (x**n)
        return value
    return function