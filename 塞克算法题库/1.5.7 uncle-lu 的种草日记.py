# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 23:41
# @Author : DongYun
# @File : 1.5.7 uncle-lu 的种草日记.py
# @Software : PyCharm
n,m,q = list(map(int,input().split()))
num = [0]*(n+2)
for i in range(m):
    temp=list(map(int, input().split()))
    num[temp[0]]+=1
    num[temp[1]+1]-=1
for i in range(1,n):
    num[i]+=num[i-1]
question = list(map(int, input().split()))
for i in question:
    print(num[i])
