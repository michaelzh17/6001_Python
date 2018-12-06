#!/usr/bin/env python3

def getRatios(vect1, vect2):
    """Assumes: vect1 and vect2 are equal length lists of numbers 
        Returns: a list containing the meaningful values of vect1[i]/vect2[i]"""

    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

try:
    print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0, 3.0]))
    print(getRatios([], []))

    print(getRatios([3.0, 2.0], [8.0]))
except ValueError as msg:
    print(msg)
#print(getRatios([1.0, 'a'], [4.0, 'b']))





