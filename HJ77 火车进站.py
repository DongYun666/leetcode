# -*- codeing = utf-8 -*-
# @Time : 2022/4/21 18:06
# @Author : DongYun
# @File : HJ77 火车进站.py
# @Software : PyCharm
from itertools import permutations

def check(train_list,x):
    stack = []
    index = 0
    for train in train_list:
        stack.append(train)
        while len(stack) != 0 and stack[-1] == x[index]:
            stack.pop(len(stack)-1)
            index+=1
    return True if len(stack) == 0 else False
while True:
    try:
        N = int(input())
        train_list = list(map(int,input().split()))
        for x in permutations(sorted(train_list)):
            if check(train_list,x):
                for t in x:
                    print(t,end=" ")
                print()
    except:
        break
