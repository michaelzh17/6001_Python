#!/usr/bin/env python3

class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'
    
    def printVisible(self):
        print(self.visible)
    
    def printInVisible(self):
        print(self.__invisible)

    def __printInVisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)


