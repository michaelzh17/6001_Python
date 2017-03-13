#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:22:39 2017

@author: xinyezhang
"""

count = 0

s = 'azcbobobobegghaklbob'

for sp in range(0,len(s)):
    if s[sp:sp+3]=='bob':
        count += 1
print("Number of times bob occurs is:", count)
        

