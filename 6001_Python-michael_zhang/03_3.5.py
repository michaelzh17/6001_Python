#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 23:25:21 2017

@author: xinyezhang
"""

#Newton - Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0.01

epsilon  = 0.01
k = 25.0
guess = k/2.0
numGuess = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuess += 1
print('Square root of', k, 'is about', guess)
print('numGuess = ', numGuess)