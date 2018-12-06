#!/usr/bin/env python3

def findAnEven(L):
    """Assumes L is a list of integers
        Returns the first even number in L
        Raises ValueError if L does not contain an even number. """
    try:
        for i in L:
            if i%2 == 0:
                return i 
    except:
        raise ValueError("There is no even number in this list.")

l = [3, 5, 9, 1]

val = findAnEven(l)
print(val)
