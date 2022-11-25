# -*- codeing = utf-8 -*-
# @Time : 2022/4/10 11:36
# @Author : DongYun
# @File : 集换卡.py
# @Software : PyCharm

class Solution:
     def check(self,nums):
         temp = [-1]*10
         for index,num in enumerate(nums):
             for j in num:
                 if temp[int(j)] == -1 :
                     temp[int(j)]+=2
             if len(set(nums)) == 1:
                 return index+1
         return -1
if __name__ == '__main__':
    nums  = list(map(str,input().split()))
    print(Solution().check(nums))