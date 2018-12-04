#!/usr/bin/env python3

def sumDigits(s):
    """Assumes s is a string
        Returns the sum of the decimal digits in s
        For example, if s is 'a2b3c' it returns 5"""
    sum_digit = 0

    for e in s:
        try:
            sum_digit += int(e)
        except ValueError:
            continue
    return sum_digit

s = 'x5a9n2'
a = sumDigits(s)

print(a)

