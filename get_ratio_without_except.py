#!/usr/bin/env python3

def getRatios(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
       Returns: a list containing the meaningful values of vect1[i]/vect2[i]"""
    
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('getRatios called with bad arguments')
    for index in range(len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]
        if (type(vect1Elem)) not in (int, float))\
            or (type(vect2Elem)) not in (int, float)):
            raise ValueError('getRatios called with bad arguments')
        if vect2Elem == 0.0:
            ratios.append(float('nan')) # nan = not a number
        else:
            ratios.append(vect1Elem/vect2Elem)
    return ratios


