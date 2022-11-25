# -*- codeing = utf-8 -*-
# @Time : 2022/4/16 20:28
# @Author : DongYun
# @File : HJ60 查找组成一个偶数最接近的两个素数.py
# @Software : PyCharm
import math

def isProme(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
while True:
    try:
        x = int(input())
        for i in range(2,x//2+1):
            if isProme(i) and isProme(x-i):
                a,b = i , x-i
        print(a)
        print(b)
    except:
        break


