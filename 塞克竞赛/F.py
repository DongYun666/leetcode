# -*- codeing = utf-8 -*-
# @Time : 2022/7/24 9:20
# @Author : DongYun
# @File : F.py
# @Software : PyCharm
n = int(input())
Str_A = list(input())
Str_B = list(input())
print(Str_A,Str_B)
count = 0
for i in range(n):
    if Str_A == Str_B:
        print(count)
        break
    if Str_A[i]!=Str_B[i]:
        index = Str_A.index(Str_B[i])
        print("index",index)
        Str_A = Str_A[index]+Str_A[:index]+Str_A[index+1:]
        print(Str_A,Str_B)

