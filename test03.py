# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:22:37 2017

@author: Henley
"""
character = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
#定义一个集合
code=set()

import random
while len(code)<=199:
    #对元数据进行乱序
    random.shuffle(character)
    #放入集合中保证不重复
    code.add(''.join(character[:8]))
import string    
lst = list(string.digits+string.letters)
import string                           # 导入random,string模块
lst = string.ascii_letters 

cardType = ['Heart','Plum','Diamond','Spade']
cardNum = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
card = []
for cType in cardType:
    for cNum in cardNum:
        card.append(cType+cNum);
        
card.append('Jocker')
card.append('jocker')
player1 = []
player2 = []
player3 = []

import random
random.shuffle(card)
for i in range(1,52):
    if i%3 == 0:
        player3.append(card[i])
    elif i%2 == 0:
        player2.append(card[i])
    else:
        player1.append(card[i])
        
last = card[-3:]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        