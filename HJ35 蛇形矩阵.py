# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 21:59
# @Author : DongYun
# @File : HJ35 蛇形矩阵.py
# @Software : PyCharm

N = int(input())
temp = 1
a = 2
for i in [x for x in range(0,N)]:
    print(temp+i,end=" ")
    x = temp
    for j in range(i+a,N+1):
        x+=j
        print(x,end=" ")
    a+=1
    temp +=i
    print("")
