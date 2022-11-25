# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 15:24
# @Author : DongYun
# @File : 1.4.7 借教室.py
# @Software : PyCharm
import sys

n,m = list(map(int,input().split()))
num = list(map(int,input().split()))
num.append(0)
d,l,r = [0] * 1000000,[0] * 1000000,[0] * 1000000
def check(x):
    change = [0] * 1000000
    for i in range(1,x+1):
        change[i] = num[i] - num[i-1]
    for i in range(1,n+1):
        change[l[i]] += d[i]
        change[r[i]+1] -= d[i]
    for i in range(1,n+1):
        if change[i]<0:
            return False
    return True

for i in range(m):
    temp = list(map(int, input().split()))
    d[i] = temp[0]
    l[i] = temp[1]
    r[i] = temp[2]
if check(m):
    print(0)
    sys.exit(1)
left,right = 1,m
while left <= right:
    mid = (left+right)>>1
    if check(mid):
        right = mid
    else:
        left = mid + 1
print("-1")
print(left)

