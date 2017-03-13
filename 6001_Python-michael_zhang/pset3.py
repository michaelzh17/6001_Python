# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:12:31 2017

@author: Surface3pro
"""
count = 0

lst_end = []
lst_count = []
s = "zyxabcabcdc"

for i in range(len(s) - 1):
    if i != (len(s) - 2) and s[i+1] >= s[i]:
        count += 1
    elif s[i+1] < s[i]:
        lst_end.append(i -1)
        lst_count.append(count)
        count = 0
    else:
        count += 1
        lst_end.append(i)
        lst_count.append(count)
        count = 0
        
    
max_count = max(lst_count)
index = lst_count.index(max_count)
end = lst_end[index]

print("Longest substring in alphabetical order is: " + s[end - max_count + 1: end +  2])



