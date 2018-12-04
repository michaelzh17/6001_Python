#!/usr/bin/env python3

numSuccess = int(input('number of success: '))
numFailures = int(input('number of failures: '))


try:
    successFailureRatio = numSuccess/numFailures
    print('The success/failure ratio is', successFailureRatio)
except ZeroDivisionError:
    print('No failures, so the success/failure ratio is undefined.')
print('Now here the end')


