# -*- codeing = utf-8 -*-
# @Time : 2022/4/29 19:28
# @Author : DongYun
# @File : 美团2021校招笔试2.py
# @Software : PyCharm

while True:
    try:
        n = int(input())
        # temp = [0]*(n+1)
        nums = list(map(int,input().split()))
        nums.sort()
        count = 0
        for index in range(1,len(nums)+1):
            count+=abs(nums[index-1]-index)
        print(count)
    except:
        break