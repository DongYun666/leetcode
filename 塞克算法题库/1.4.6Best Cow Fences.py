# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 11:51
# @Author : DongYun
# @File : 1.4.6Best Cow Fences.py
# @Software : PyCharm

N,F = list(map(int,input().split()))
num = []
num.append(int(input()))
res = 0
for i in range(1,N):
    num.append(int(input()))
    num[i]+=num[i-1]
    if i >=F:

        res = max(res,(num[i]-num[i-F]))
print(int(1000*res/F))


