# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 10:28
# @Author : DongYun
# @File : 1.4.3 网线主管.py
# @Software : PyCharm
N,K=list(map(int,input().split()))
# num = list(map(float,input().split()))
num = []
l,r= 0,0
for i in range(N):
    num.append(int(float(input())*100))
    if num[i]>r:
        r = num[i]
def count(x):
    res = 0
    for i in num:
        res+=i//x
    return res

while l<=r:
    mid = (l+r)>>1
    if count(mid)<K:
        r = mid - 1
    else:
        l = mid+1
print("%.2f"% (r/100))