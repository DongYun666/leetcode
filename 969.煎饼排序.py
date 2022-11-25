# -*- codeing = utf-8 -*-
# @Time : 2022/2/19 9:45
# @Author : DongYun
# @File : 969.煎饼排序.py
# @Software : PyCharm
from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        last = len(arr)
        ans = []
        while last>1:
            index = arr.index(last)
            if index == last-1:
                last-=1
                continue
            else:
                ans.append(index+1)
                self.rev(arr,index)
                ans.append(last)
                self.rev(arr,last-1)
                last-=1
        return ans
    def rev(self,arr,end):
        n = (end+2)//2
        for i in range(n):
            arr[i],arr[end] = arr[end],arr[i]
            end-=1

    def pancakeSort2(self, arr: List[int]) -> List[int]:
        res = []
        N = len(arr)
        while N:
            idx = arr.index(N)
            res.append(idx+1)
            arr = arr[:idx+1][::-1]+arr[idx+1:]
            res.append(N)
            arr = arr[:N][::-1]+arr[N:]
            N -= 1
        print(arr)
        return res

a = [3,2,4,1]
print(Solution().pancakeSort(a))
