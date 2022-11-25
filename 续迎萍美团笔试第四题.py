# -*- codeing = utf-8 -*-
# @Time : 2022/4/30 9:53
# @Author : DongYun
# @File : 续迎萍美团笔试第一题.py
# @Software : PyCharm


while True:
    try:
        def max_sub_array(a):
            maxSub = -100
            pre = -100
            for i in range(1,len(a)-1):
                pre = max(a[i],pre+a[i])
                maxSub = max(maxSub,pre)
            return maxSub
        T = int(input())
        for _ in range(T):
            n = int(input())
            a = list(map(int,input().split()))
            if max_sub_array(a)>=sum(a):
                print("Yes")
            else:
                print("No")
    except:
        break


# if x>0:
            #     m+=x
            #     count+=1
            #     door = True
            # else:
            #     if abs(x)>m:
            #         continue
            #         door = False
            #     elif not door:
            #         door = True
            #         m-=abs(x)
            #         count+=1

# 2
# 4
# 1 2 3 4
# 3
# -5 5 -5