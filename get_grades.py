#!/usr/bin/env python3

def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') #open file for reading
    except IOError:
        raise ValueError('getGrades can not open file ' + fname)
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades


try:
    grades = getGrades('filename.txt') # replace with good file name
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is ', median)
except ValueError as errorMsg:
    print('Whoops.', errorMsg)


