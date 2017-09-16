# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:49:01 2017

@author: Henley
"""

import os
import os.path
import codecs

filePaths = []
for root, dirs, files in os.walk(
    "F:\\PDM\\2.1\\SogouC.mini\\Sample"
):
    for name in files:
        filePaths.append(os.path.join(root, name))
        
key = input("请输入关键字：\n")
result = []
for filename in filePaths:
    f = codecs.open(filename, 'r', 'utf-8')
    content = f.read()
    f.close()
    if key in filename :
        result.append(filename)
    elif key in content:
        result.append(filename)

r = open('F:\\PDM\\result.txt','a')
a = ['a','b','c']
for resultname in result:
    r.write(resultname)
    r.write('\n')
    r.flush()    