# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:22:58 2017

@author: Henley
"""

import pandas
import numpy

data = pandas.read_table('C:/Users/Henley/Desktop/report.txt',
                         header=None,encoding='gb2312',
                         delim_whitespace=True)

dataTemp = data.iloc[0:30,1:10]

avg = dataTemp.mean(axis=1)
total = dataTemp.sum(axis=1)

dataTemp['总分']=total
dataTemp['平均分'] = avg


dataTemp = dataTemp.sort_values(
        by='平均分',
        ascending = False
        )

dataTemp.loc[len(dataTemp)]=dataTemp.mean()

dataTemp = dataTemp[dataTemp>60]

dataTemp = dataTemp.fillna("不及格")
dataTemp['名次'] = numpy.arange(1,32,1)
dataTemp['姓名'] = data.iloc[0:30,0:1]
dataTemp.iloc[30:31,11:12]=0
dataTemp.iloc[30:31,12:13]='平均'

dataTemp.columns=['语文','数学','英语','物理',
                  '化学','生物','政治','历史',
                  '地理','总分','平均分','名次','姓名' ]

result = dataTemp[['名次','姓名','语文','数学',
                  '英语','物理','化学','生物',
                  '政治','历史','地理','总分','平均分']]
result = result.sort_values(
        by='名次',
        ascending=True
        )

result.to_csv('C:/Users/Henley/Desktop/result.csv',index=False)



