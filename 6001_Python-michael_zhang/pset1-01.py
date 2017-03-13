#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 10:26:37 2017

@author: xinyezhang
"""

s = 'massaachuseets'
count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print("Number of vowels:", count)