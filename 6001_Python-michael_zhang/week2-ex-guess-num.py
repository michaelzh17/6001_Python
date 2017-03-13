#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:09:15 2017

@author: xinyezhang
"""

# week 2 finger exercise -- guess number 

print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = 0 
hint = 'l'
while ( hint != 'c'):
    if (hint == 'h'):
        high = guess 
    elif (hint == 'l'):
        low = guess 
    else:
        print("Sorry, I did not understand your input.")
    guess = int((low + high)/2)
    print("Is your secret number", guess,"?")
#    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.")
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
print("Game over. Your secret number was:", guess)
    