#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:34:36 2017

@author: xinyezhang
"""

#final pset 3
trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    prn = ''
    if int(us_num) >= 0 and int(us_num) <= 10:
        prn += trans[us_num]
    elif int(us_num) >= 11 and int(us_num) <= 19:
        prn += trans['10'] + ' ' + trans[us_num[1]]
    elif int(us_num) > 19 and us_num[1] != '0':
        prn += trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]
    else:
        prn += trans[us_num[0]] + ' ' + trans['10']

    return prn
        
print(convert_to_mandarin('0'))
print(convert_to_mandarin('8'))
print(convert_to_mandarin('10'))
print(convert_to_mandarin('16'))
print(convert_to_mandarin('20'))
print(convert_to_mandarin('34'))
print(convert_to_mandarin('60'))
print(convert_to_mandarin('99'))
