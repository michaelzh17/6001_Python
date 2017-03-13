#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 10:48:02 2017

@author: xinyezhang
"""

#('a', 'e', 'i', 'o', 'u')
s = ' '
count = 0
for letter in s:
    if letter in 'a eiou':
        count += 1
print("Number of vowels:", count)