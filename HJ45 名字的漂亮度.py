# -*- codeing = utf-8 -*-
# @Time : 2022/4/16 21:27
# @Author : DongYun
# @File : HJ45 名字的漂亮度.py
# @Software : PyCharm
from collections import Counter


def beautiful(s):
    res = 0
    s = Counter(s)
    sorted(s.items(), key=lambda x: x[1], reverse=True)
    s = s.values()
    for i in range(26,26-len(s),-1):
        res += s[26-i]*i
    return res

while True:
    try:
        N = int(input())
        while N!=0:
            N-=1
            s = input()
            print(beautiful(s))
    except:
        break
