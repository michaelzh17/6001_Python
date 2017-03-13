#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:41:02 2017

@author: xinyezhang
"""
'''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
def oddTuples(aTup):
    odd_tuple = ()
    for t in range(len(aTup)):
        if t%2 == 0:
            odd_tuple = odd_tuple + (aTup[t],)
    return odd_tuple 