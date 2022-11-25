# -*- codeing = utf-8 -*-
# @Time : 2022/4/30 9:53
# @Author : DongYun
# @File : 续迎萍美团笔试第一题.py
# @Software : PyCharm


while True:
    try:
        T = int(input())
        for _ in range(T):
            n,m = list(map(int,input().split()))
            temp1 = list(map(int,input().split()))
            temp2 = list(map(int,input().split()))
            if n!= m or m%2!=0:
                print("No")
            else:
                temp1.sort()
                temp2.sort()
                if temp1 == temp2:
                    print("Yes")
    except:
        break

# 3
# 8 8
# 1 3 7 8 5 6 2 4
# 3 7 8 5 6 2 4 1
# 9 9
# 1 3 7 8 5 6 2 4 3
# 3 7 8 5 6 2 4 1 9
# 7 7
# 1 5 6 7 3 4 2
# 5 6 7 3 4 2 1

# 4 10
# -16 2 -6 8