#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:56:43 2017

@author: xinyezhang
"""

def how_many(aDict):
    lst = aDict.values()
    sum_num = 0
    for i in lst:
        sum_num += len(i)
    return sum_num
    


def biggest(aDict):
    lst = list(aDict.values())
    lst_key = list(aDict.keys())
    lst_len = []
    for i in range(len(lst)):
        lst_len.append(len(lst[i]))
    max_len = max(lst_len)
    ind = lst_len.index(max_len)
    return lst_key[ind]