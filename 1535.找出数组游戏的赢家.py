# -*- codeing = utf-8 -*-
# @Time : 2022/5/24 20:39
# @Author : DongYun
# @File : 1535.找出数组游戏的赢家.py
# @Software : PyCharm
from typing import List
class Solution:
    def hou(self,arr,index,length):
        if index+1 == len(arr):
            return 0
        for x in arr[index+1:]:
            if arr[index]> x:
                length-=1
            else:
                break
        return length
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr)-1<=k:
            return max(arr)
        for i in range(len(arr)):
            if i == 0 and self.hou(arr,i,k) <= 0:
                return arr[i]
            else:
                if arr[i]>arr[i-1] and self.hou(arr,i,k-1) <= 0:
                    return arr[i]
                else :
                    continue
    def getWinner1(self, arr: List[int], k: int) -> int:
        i = k
        l = 0
        if len(arr)-1<=k:
            return max(arr)
        while l !=len(arr):
            if arr[0]<arr[1]:
                arr = arr[1:]+[arr[0]]
                l+=1
                continue
            else:
                for x in arr[1:]:
                    if arr[0]>x:
                        i -=1
                    else:
                        break
                if i == 0:
                    return arr[0]
                else :
                    i = k
                arr = arr[1:]+[arr[0]]
                l+=1
    def getWinner1(self, arr: List[int], k: int) -> int:
        if len(arr)-1<=k:
            return max(arr)
        p = max(arr[0],arr[1])
        count = 1
        max_num= p
        if count  == k:
            return p
        for x in arr[2:]:
            if x<p:
                count+=1
                if count == k:
                    return p
            else:
                count = 1
                p = x
            max_num = max(max_num,x)
        return max_num
# arr = [2,1,3,5,4,6,7]
# k = 2
# arr = [3,2,1]
# k = 10
arr = [1,9,8,2,3,7,6,4,5]
k = 7
print(Solution().getWinner1(arr,k))