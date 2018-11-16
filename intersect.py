#!/usr/bin/env python3

def intersect(t1, t2):
    """Assumes t1 and t2 are tuples
        returns a tuple containing elements that are in both t1 and t2
    """
    result = ()
    for element in t1:
        if element in t2:
            result += (element, )
    return result


t1 = (3, 5, 2, 9, 'a', 'c')
t2 = (4, 5, 9, 'a', 'h', 3.4)

result = intersect(t1, t2)

print(result)


