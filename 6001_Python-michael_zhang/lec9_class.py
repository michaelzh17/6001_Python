#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:06:55 2017

@author: xinyezhang
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
        
#clock = Clock('10:30')

class Clock_c1(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)

#clock = Clock_c1('5:30')

class Clock_c2(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

ny_clock = Clock_c2('4:30')
bj_clock = ny_clock
bj_clock.time = '8:30'
