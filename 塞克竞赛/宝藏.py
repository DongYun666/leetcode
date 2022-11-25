# -*- codeing = utf-8 -*-
# @Time : 2022/7/23 15:11
# @Author : DongYun
# @File : 宝藏.py
# @Software : PyCharm
l,r = list(map(int,input().split()))
count = 2
def check(x):
    flag = False
    temp = []
    while x != 0:
        temp.append(x%10)
        x//=10
    for i in range(1,len(temp)):
        temp[i] = abs(temp[i]-temp[i-1])
        if temp[i]<5:
            return False
    return True
for i in range(l,r+1):
    if i <= 16:
        continue
    elif check(i):
        count+=1
        print(i)
print(count)
