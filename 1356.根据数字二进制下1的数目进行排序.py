# -*- codeing = utf-8 -*-
# @Time : 2022/6/7 20:59
# @Author : DongYun
# @File : 1356.根据数字二进制下1的数目进行排序.py
# @Software : PyCharm
import functools
from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_1_in_binary(x):
            count = 0
            while x>0:
                x&=x-1
                count+=1
            return count
        def my_quick_sort(arr,temp,start,end):
            if start >= end:
                return
            mid_data,temp_data,left,right = arr[start],temp[start],start,end
            while left < right:
                while arr[right] >= mid_data and temp[right]>=temp_data and left <right:
                    right-=1
                arr[left] = arr[right]
                temp[left] = temp[right]
                while arr[left] < mid_data and temp[left]<temp_data and left <right:
                    left+=1
                arr[right] = arr[left]
                temp[right] = temp[left]
            arr[left] = mid_data
            temp[left] = mid_data
            my_quick_sort(arr,temp,start,left-1)
            my_quick_sort(arr,temp,left+1,end)
        temp = []
        for x in arr:
            temp.append(count_1_in_binary(x))
        return my_quick_sort(arr,temp,0,len(arr)-1)

arr = [0,1,2,3,4,5,6,8,7]
print(Solution().sortByBits(arr))