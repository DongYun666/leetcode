# -*- codeing = utf-8 -*-
# @Time : 2022/4/25 19:10
# @Author : DongYun
# @File : 美团笔试3.py
# @Software : PyCharm


while True:
    try:
        N = int(input())
        recoder = [0]*N
        res = []
        for _ in range(N):
            serial = list(map(int,input().split()))
            for x in serial:
                if recoder[x-1] == 0 and x not in res:
                    recoder[x-1] =1
                    res.append(x)
                    break
        for x in res:
            print(x,end=" ")
    except:
        break