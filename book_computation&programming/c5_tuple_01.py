#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:01:31 2017

@author: xinyezhang
"""

def intersect(t1, t2):
    """Assumes t1 and t2 are tuples
       Returns a tuple containing elements that are in both t1 and t2"""
    result = ()
    for elmt in t1:
        if elmt in t2:
            result += (elmt,)
    return result

    
t1 = (3, 5, 8)
t2 = (9, 0, 5, 5)


