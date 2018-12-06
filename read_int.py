#!/usr/bin/env python3

# exceptions as a flow of control mechanism


def readInt():
    while True:
        val = input('Enter an integer: ')
        try:
            return int(val) # convert str to int before returning
        except ValueError:
            print(val, 'is not an integer')


def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            return valType(val) # convert str to valType before returning
        except ValueError:
            print(val, errorMsg)



#print(readInt())

val = readVal(int, 'Enter  an integer: ', 'is not an integer.')



print(val)
