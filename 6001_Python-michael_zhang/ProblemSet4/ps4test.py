#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:16:55 2017

@author: xinyezhang
"""

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words.txt', 'r')
    # wordList: list of strings
    wordList = []
    line = inFile.readline()
 #   print(line)
  #  for x in line:
    wordList = line.split()
    print("  ", len(wordList), "words loaded.")
  #  return wordList