# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 17:54
# @Author : DongYun
# @File : 1.5.3数串问题.py
# @Software : PyCharm
n = int(int(input()))
num = list(map(int,input().split()))
def getSubArrayCountGreaterThan(nums):
    result=0
    count=1<<len(nums)
    for mark in range(count):
        temp=0
        for i in range(len(nums)):
            if((1<<i)&mark)!=0:
                temp+=nums[i]
        if temp>0:
            result+=1
    return result
resoult = getSubArrayCountGreaterThan(num)
print(resoult if sum(num)<=0 else resoult-1)

#求所有的子集
def getAllSubArray(nums):
    result=[]
    count=1<<len(nums)
    for mark in range(count):
        temp=[]
        for i in range(len(nums)):
            if((1<<i)&mark)!=0:
                temp.append(nums[i])
        result.append(temp)
    return result


print(getAllSubArray(num))
# print(getSubArrayCountGreaterThan([1,2,3]))