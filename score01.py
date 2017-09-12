# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 00:12:00 2017

@author: Henley
"""
from numpy import mean
f = open(r'C:\Users\Henley\Desktop\Python\report.txt')
scores = []
#导入数据，并求出各人的平均分，总分
for line in f:
    temp = line.split()
    score = []
    score.append(temp[0])
    for i in temp[1:]:
        score.append(int(i))
    score.append(sum(score[1:]))
    score.append(mean(score[1:-1]))
    scores.append(score)
#按照平均分进行排序    
scores = sorted(scores,key=lambda x:x[11],reverse=True)
#计算每一科目的平均分
avg = ['平均']
for i in range(1,12):
    sum = scores[0][i]
    for j in range(0,30):
        sum = sum+scores[j][i]    
    avg.append(int(sum/30))
scores.insert(0,avg)
#替换不及格分数
for i in range(0,31):
    for j in range(1,10):
        if scores[i][j]<60:
            scores[i][j]='不及格'
    scores[i].insert(0,i)
#添加科目名称
subject = ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
scores.insert(0,subject)
result = []
for i in range(0,32):
    for j in range(0,13):
        if type(scores[i][j])!=str:
           scores[i][j] = str(scores[i][j])
    result.append(' '.join(scores[i]))
#写入文件
f = open(r'C:\Users\Henley\Desktop\Python\result.txt','w')
for line in result:
    f.writelines(line)
    f.writelines('\n')
f.close()