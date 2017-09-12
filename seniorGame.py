# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:05:40 2017

@author: Henley
"""
#猜数字游戏
def game():
    import random
    guessTimes = 0;
    num = 0
    answer = random.randint(1,100)
    print("猜猜数字是几？")
    while num != answer:
        guessTimes = guessTimes + 1
        print("第%d次"%(guessTimes))
        num = eval(input("请输入100以内的数字\n"))
        while num >100 or num<0:
            num = eval(input("请输入100以内的数字\n")) 
            
        if num > answer:
            print("太大了！")
        elif num < answer:
            print("太小了！")
        else:
            print("猜对了，答案是%d"%(answer))
            break
    return guessTimes
#计算输出结果
def procInfo(info):
    data = []
    temp = info.split()
    for times in temp[1:]:
        data.append(int(times))
    print("你猜中答案一共用了%d机会"%(data[-1]))
    print("你一共玩了%d次游戏"%(len(data)))
    print("你平均%.2f次猜中答案"%(sum(data)/len(data)))
    print("你最好的成绩是%d次"%(min(data)))
#保存数据
def save(infoList,file):
    file  = open(r'C:\Users\Henley\Desktop\Python\list.txt','w')
    for line in infoList:
        file.writelines(line)
        file.writelines('\n')
    file.flush()
    file.close()
    
    
file  = open(r'C:\Users\Henley\Desktop\Python\list.txt','r')
infoList = []
nameList = []
for line in file:
    infoList.append(line) 
    nameList.append(line.split()[0])
file.close()
name = eval(input("请输入玩家姓名：\n"))

if name in nameList:
    print('欢迎回来%s,祝您游戏愉快！'%(name))
    flag = 'go'
    while flag == 'go':
        newTimes = game()
        index = nameList.index(name)
        info = infoList[index]+" "+str(newTimes)
        procInfo(info)
        flag = eval(input("输入'go'再玩一次，否则退出游戏\n"))
        if flag == 'go':
            print("新游戏")
        else:
            infoList[index] = info
            save(infoList,file)
else:
    print('欢迎%s进入游戏,祝您游戏愉快！'%(name))
    flag = 'go'
    info = name
    while flag == 'go':
        newTimes = game()
        info = info + " " + str(newTimes)
        procInfo(info)
        flag = eval(input("输入'go'再玩一次，否则退出游戏\n"))
        if flag == 'go':
            print("新游戏")
        else:
            infoList.append(info)
            save(infoList,file)

