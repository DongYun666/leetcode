# -*- codeing = utf-8 -*-
# @Time : 2022/4/19 20:24
# @Author : DongYun
# @File : 部队集合.py
# @Software : PyCharm
def func(res,he,attack,define,index,attack_sum,define_sum):
    if index>=len(attack):
        return 0
    if he[index] <=0:
        func(res,he,attack,define,index+1,attack_sum,define_sum)
    res[index] = max(func(res, he, attack, define, index + 1, attack_sum + attack[index], define_sum + define[index]),
                     func(res, he, attack, define, index + 1, attack_sum, define_sum))
    if attack_sum<=0 or define_sum <=0:
        return 0
    else:
        return 1
while True:
    try:
        N = int(input())
        attack = [0]*N
        define = [0]*N
        he = [0]*N #认为攻击力和防守力和位负数时 对总体无利
        for i in range(N):
            attack[i],define[i] = list(map(int,input().split()))
            he[i] = attack[i]+define[i]
        res = [0]*N
        # func(res,he,attack,define,0,0,0)
        print(res)
        print(attack,define,he)
    except:
        break


# 5
# -5 7
# 8 -6
# 6 -3
# 2 1
# -8 -5