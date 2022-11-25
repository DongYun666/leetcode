# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 22:29
# @Author : DongYun
# @File : ipc2_7 蚂蚁.py
# @Software : PyCharm
n = int(int(input()))
x = []
y = []
lower = []
upper = []
for i in range(n):
    temp = list(map(int, input().split()))
    x.append(abs(temp[0]))
    y.append(abs(temp[1]))
    lower.append(min(x[i],y[i]))
    upper.append(max(x[i],y[i]))

print(max(lower)**2+min(upper)**2)
