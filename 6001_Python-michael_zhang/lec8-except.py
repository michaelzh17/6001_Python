#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:51:55 2017

@author: xinyezhang
"""

#def readingData():
data = []
file_name = input("Provide a file name: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print("can't open:", file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()

gradesData = []

if data:
    for student in data:
        try:
            name = student[0: -1]
            grade = int(student[-1])
            gradesData.append([name, [grade]])
#            gradesData.append([student[0:2], [student[2]]])
        except ValueError:
            gradesData.append([student[:], []])
#            gradesData.append([student[0:2],[]])

    