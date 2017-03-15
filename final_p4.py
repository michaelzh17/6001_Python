#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:26:05 2017

@author: xinyezhang
"""
#for final pset4

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    #find the longest run of increasing and decreasing separately
    #then compare them, return the sum 
    count_in = 0
    count_de = 0
    #list to record ending point of an increasing run
    lst_in = []
    #list to record count of an increasing run 
    lst_count_in = []
    #list to record ending point of a decreasing run 
    lst_de =[]
    #list to record count fo a decreasing run 
    lst_count_de = []
    
    #go through L to find the longest run in increasing order 
    for i in range(1, len(L)):
        if L[i] >= L[i-1] and i !=len(L) - 1:
            count_in += 1
        elif L[i] < L[i-1]:
            #record i -1 in lst_in
            lst_in.append(i-1)
            #record count_in in lst_count_in
            lst_count_in.append(count_in)
            count_in = 0
        else:
            #this covers the scenario that i is the last element of L and still in increasing  order
            lst_in.append(i)
            count_in += 1
            lst_count_in.append(count_in)
    
    #go through L to find the longest run in decreasing order
    for i in range(1, len(L)):
        if L[i] <= L[i-1] and i != len(L) -1:
            count_de += 1
        elif L[i] > L[i-1]:
            #record i-1 in lst_de
            lst_de.append(i-1)
            #record count_de in lst_count_de
            lst_count_de.append(count_de)
            count_de = 0
        else:
            #this covers the scenario that i is the last element of L and still in decreasing order
            lst_de.append(i)
            count_de += 1
            lst_count_de.append(count_de)
    #find the longest run in lst_count_in and lst_count_de and compare
    if len(lst_count_in) == 0 or len(lst_count_de) == 0:
        return sum(L)
    else:
        max_in = max(lst_count_in)
        max_de = max(lst_count_de)
        index_in = lst_count_in.index(max_in)
        key_in = lst_in[index_in]
        index_de = lst_count_de.index(max_de)
        key_de = lst_de[index_de]
        if max_in > max_de:
            
            return sum(L[key_in - max_in: key_in + 1])
        elif max_in < max_de:
            
            return sum(L[key_de - max_de: key_de + 1])
        else:
            if key_in < key_de:
                return sum(L[key_in - max_in: key_in + 1])
            elif key_in > key_de:
                return sum(L[key_de - max_de: key_de + 1])
            else:
                return sum(L)

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                