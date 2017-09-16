# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:42:45 2017

@author: Henley
"""

with open("data.txt",'r') as f:
    word = f.read()
    wordList = word.split()
    f.close()