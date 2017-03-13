# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# this is for finger exercise in chapter 2. Prints the largest odd number in 3
# numbers, if none of them are odd, print a message to indicate.

if(x%2==1)
    if (y%2==1)
        if(z%2==1)
            if (x>y and x>z)
                print('x is the biggest odd in the three number')
            elif(y>z)
                print('y is the biggest odd in the three number')
            else:
                print('z is the biggest odd in the three number')
        else:
            if (x>y):
                print('x is the biggest odd')
            else:
                print('y is the biggest odd')
    else:
        if(z%2==1)
            if(x>z)
                print('x is the biggest odd')
            else:
                print('z is the biggest odd')
else:
    if (y%2==1)
        if(z%2==1)
            if(y>z)
                print('y is the biggest odd in the three number')
            else:
                print('z is the biggest odd in the three number')
        else:
                print('y is the biggest odd')
    else:
        if(z%2==1)
                print('z is the biggest odd')
            else:
                print('no odd number in the list')
    
