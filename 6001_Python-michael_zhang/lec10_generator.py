#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:12:43 2017

@author: xinyezhang
"""

#generator

def genTest():
    print("generator")
    yield 1
    print("another generator")
    yield 2
    
    
def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        n = fibn_1 + fibn_2
    yield n
    fibn_2 = fibn_1
    fibn_1 = n

def genPrimes():
    prime = [2]
    yield 2
    x = 3
    while True:
        _flag = True
        for element in prime:
            if x % element == 0:
                _flag = False
        if _flag == True :
            prime.append(x)
            yield x
        x += 1
        

        
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 
"""the 'right' way"""

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
            
          

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            