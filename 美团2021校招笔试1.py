# -*- codeing = utf-8 -*-
# @Time : 2022/4/29 19:14
# @Author : DongYun
# @File : 美团2021校招笔试1.py
# @Software : PyCharm

while True:
    try:
        n,x,y = list(map(int,input().split()))
        scores = list(map(int,input().split()))
        scores.sort()
        if len(scores)-y>y:
            print(-1)
        else:
            if len(scores)-y >=x:
                print(scores[len(scores)-y-1])
            else:
                print(scores[x-1])
    except:
        break