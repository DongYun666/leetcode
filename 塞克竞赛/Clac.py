# -*- codeing = utf-8 -*-
# @Time : 2022/7/23 16:38
# @Author : DongYun
# @File : Clac.py
# @Software : PyCharm
from math import sqrt

L,R,p = list(map(int,input().split()))
def Gn(n):
    res = 1
    for k in range(int(sqrt(n)+1)):
        res*=(n-k**2)
    return res
def S(n,p):
    if Gn(n)%p == 0:
        print(Gn(n))
        return 1
    else:
        return 0
def ans(L,R,p):
    res = 0
    for i in range(L,R+1):
        res+=S(i,p)
    return res
print(ans(L,R,p))
