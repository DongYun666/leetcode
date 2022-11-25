# -*- codeing = utf-8 -*-
# @Time : 2022/4/15 20:58
# @Author : DongYun
# @File : HJ41 称砝码.py
# @Software : PyCharm

while True:
    try:
        n = int(input())
        weight = list(map(int,input().split()))
        count = list(map(int,input().split()))
        weight_temp = []
        weights = {0,}
        for i in range(n):
            for j in range(count[i]):
                weight_temp.append(weight[i])
        for w in weight_temp:
            for j in list(weights):
                weights.append(w+j)
        print(len(weights))
    except:
        break
