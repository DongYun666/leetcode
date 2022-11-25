# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 14:48
# @Author : DongYun
# @File : 1.5.4 人物风云榜.py
# @Software : PyCharm
from collections import Counter
n = int(input())
num = list(map(int,input().split()))
copyNum = sorted(num.copy(),reverse=True)
dic = {}
b = Counter(num)
a = {key:value for key,value in b.items() if value > 1}
for i,v in enumerate(copyNum):
    if v in list(a.keys()):
        dic[v] = i
    else:
        dic[v] = i+1
for i,v in enumerate(num):
    print(dic[v], end = " ")
# result = []
# tempNum = list(range(1,len(num)+1))
# dct = dict(zip(sorted(num,reverse=True),tempNum))
# for i in num:
#     result.append(dct[i])
# print(result)

