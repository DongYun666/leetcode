# -*- codeing = utf-8 -*-
# @Time : 2022/4/25 18:46
# @Author : DongYun
# @File : 美团笔试2.py
# @Software : PyCharm

while True:
    try:
        N = int(input())
        S = input()
        flag_M,flag_T = False,False
        for index in range(len(S)):
            if S[index] == "T" and "M" in S[0:index]:
                S = S[index+1:]
                break
        for index in range(len(S)-1,-1,-1):
            if S[index] == "M" and "T" in S[index:]:
                S = S[:index]
                break
        print(S)
    except:
        break