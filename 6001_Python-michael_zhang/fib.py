#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:57:45 2017

@author: xinyezhang
"""

def fib(x):
    """
    assumes x an int >=0
    returns fib of x
    """
    if x == 0 or x == 1:
        return 1
    else: 
        return fib(x-1) + fib(x-2)