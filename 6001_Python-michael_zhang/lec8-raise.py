#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:40:16 2017

@author: xinyezhang
"""

def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i]"""
    
    ratio = []
    for index in range(len(L1)):
        try:
            ratio.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratio.append(float('NaN'))
        except:
            raise ValueError('get_ratios called by bad argu')
    return ratio
    
        
        
    