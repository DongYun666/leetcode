# -*- codeing = utf-8 -*-
# @Time : 2022/4/30 9:53
# @Author : DongYun
# @File : 续迎萍美团笔试第一题.py
# @Software : PyCharm


while True:
    try:
        n,m = list(map(int,input().split()))
        cars = list(map(int,input().split()))
        count = 0
        temp = 0
        for x in cars:
            if abs(x)>m and x < 0:
                temp += 1
                continue
            elif abs(x)<m or x>0:
                m+=x
                count+=1
            if temp == 2:
                break
        print(count)
    except:
        break




        # for x in cars:
        #     if x>0:
        #         m+=x
        #         count+=1
        #     else:
        #         if abs(x)>m:
        #             continue
        #         else:
        #             m-=abs(x)
        #             count+=1
        # print(count)

#
# 4 10
# -16 2 -6 8