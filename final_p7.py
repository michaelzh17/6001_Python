#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:40:34 2017

@author: xinyezhang
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def poly(x):
        f = ''
        for k in range(len(L)):
            f += str(L[k]) + ' * ' + x + ' ** ' + str(len(L)-1)
        return f
    w = eval(poly(x))
    return w