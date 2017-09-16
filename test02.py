# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:04:03 2017

@author: Henley
"""
import random
round = 0;
sumTimes = 0;
while True:
    #生成要猜的数字
    answer = random.randint(1,100)
    right = False
    guessTimes = 1
    #开始猜数字游戏
    while guessTimes <= 5:
        num = eval(input("请输入你猜的数字："))
        if num > answer:
            print("猜大了，请重新猜吧！")
        elif num < answer:
            print("猜小了，请重新猜吧！")
        else:
            print("恭喜你，猜对了")
            #是否猜对
            right = True
            break
        print("还剩%d次机会"%(5-guessTimes))
        #猜了多少次
        guessTimes += 1
    #统计总共猜了多少次
    if right:
        sumTimes += guessTimes
    round += 1;
    #是否继续游戏
    gameFlag = str(input("是否继续游戏？Y/N"))
    if gameFlag == "N":
        print("你总共猜了%d轮，平均%d次猜中。"%(round,int(sumTimes/round)))
        break
    

# length:打印图形的长度
# width:打印图形的宽度
# mark:图形的标记  
def rect(length,width,mark):
    i = 0
    while i<length:
        j=0
        while j<width:
            print(mark,end=" ")
            j += 1
        print()
        i += 1

rect(3,3,'*')
rect(2,4,'!')
rect(5,5,'*')


a=[1,3,2,5]
b=[1,3,2,5]
b.remove(2)
print(a,b)

l = [1,3,4,2,4,6]
l2 = sorted(l)
l3 = l.sort()

a = 'there is 120 second in every 2 minute'
l = [int(x) for x in a if ord(x) in range(ord('0'), ord('9')+1)]
# 取出字符串 a 中的所有数字，组合成新的列表
sum([1, 2, 0, 2])

ord('2')







































