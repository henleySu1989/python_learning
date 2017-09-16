# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:50:51 2017

@author: Henley
"""
2
a = "hello world"
b = 1.4123
c = True
d = False
e = True

print("a:%s;b:%.2f;c:%s;d:%s;e:%s"%(a,b,c,d,e))


3
f = 'hello word \n\\\"hello word"'
print(f)

count=1
print(count)

# 输出 1 到 10
for count in range(1,1):
    print (count)
    
# 输出九九乘法口诀表
# 1 x 1 = 1
# 1 x 2 = 2, 2 x 2 = 4
# ...

for i in range(1, 10):
    for j in range(1,i+1):
        print ('%d x %d = %d' % (j,i,i*j),end="")
        if(j<i):
            print(",",end="")
        else:
            print()

#生成百位数
for i in range(1,5):
    for j in range(1,5):
        #如果十位数与百位数相同，跳出此次循环
        if i==j:
            continue
        for k in range(1,5):
            #如果个位数与百位数或者十位数相同，则跳出此次循环
            if k==i or k==j:
                continue
            else:
                print(i*100+j*10+k)


3.2>2

import math 
#输入身高            
height = eval(input("请输入身高(m)："))  
#输入体重              
weight = eval(input("请输入体重(kg)："))
#计算BMI值
BMI = weight/math.pow(height,2)
#根据BMI值判断体重正常否
if BMI>=24:
    print(BMI,"体重偏重")
elif BMI<18:
    print(BMI,"体重偏轻")
else:
    print(BMI,"体重正常")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
