# -*- codeing = utf-8 -*-
# @Time : 2022/3/22 18:03
# @Author : DongYun
# @File : 1471. 数组中的 k 个最强值.py
# @Software : PyCharm

from typing import List
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res = []            #结果集
        arr.sort()          # 先排序
        mid_num = arr[(len(arr)-1)//2]  #获取中位数
        left,right = 0 ,len(arr)-1
        while left < right:
            if arr[right]-mid_num >= abs(arr[left]-mid_num):
                res.append(arr[right])
                right-=1
            else:
                res.append(arr[left])
                left+=1
        res.append(mid_num)
        return res[:k]



arr = [-493,598,-262,-918,-76,-532,521]
k = 7
print(Solution().getStrongest(arr,k))