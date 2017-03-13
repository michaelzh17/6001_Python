#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:13:34 2017

@author: xinyezhang
"""

#exercise 1
n = 1
while n < 6:
    print(2 * n)
    n += 1
print("Goodbye!")

#using for loop
for n in range(5):
    print(2 * (n+1))
print("Goodbye!")

#exercise 2
print("Hello!")

n = 5
while n > 0:
    print(n * 2)
    n -= 1

#using for loop
print("Hello!")
for n in range(5):
    print(10 - n*2)
    
#exercise 3
n = 1
total = 0

while n <= end: 
    total += n
    n += 1
print(total)

#using for loop
total = 0
for n in range(end+1):
    total += n
print(total)
