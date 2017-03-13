#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:26:43 2017

@author: xinyezhang
"""

def closest_power(base, num):
    ex = 0
    while base**ex - num <= 0:
        ex += 1
    if abs(base**ex - num) >= abs(base**(ex-1) - num):
        return ex-1
    else :
        return ex
        
def dotProduct(listA, listB):
    dotp = 0 
    for i in range(len(listA)):
        dotp += listA[i]*listB[i]
    return dotp
    
    
def deep_reverse(L):
    L.reverse()
    for i in range(len(L)):
        L[i].reverse()

def dict_interdiff(d1, d2):
    d1_cpy = d1.copy()
    d2_cpy = d2.copy()
    d3 = {}
    for d1_key in d1.keys():
        for d2_key in d2.keys():
            if d1_key == d2_key:
                d3[d1_key] = f(d1[d1_key], d2[d2_key])
                del(d1_cpy[d1_key])
                del(d2_cpy[d2_key])
    d1_cpy.update(d2_cpy)
    if d1_cpy == None:
        d1_cpy = {}
    return (d3, d1_cpy)
    

def f(i):
    return i + 2
def g(i):
    return i > 5  
    
def applyF_filterG_(L, f, g):
    l = L.copy()
    for i in L:
        if (g(f(i))) == False:
            l.remove(i)
    print(l)
    print(L)
    L = l
    print(L)
    if len(L) == 0:
        return -1
    else:
        return max(L)
    
def applyF_filterG(L, f, g):
    l = L.copy()
    for i in l:
        #if (g(f(i))) == False:
        if not (g(f(i))):
            L.remove(i)
    if len(L) == 0:
        return -1
    else:
        return max(L)
    
        
def flatten(aList):

    lst = []
    for element in aList:
        if type(element) == list:
            lst += flatten(element)
        else:
            lst.append(element)
    return lst
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                