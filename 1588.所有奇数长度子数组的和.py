# -*- codeing = utf-8 -*-
# @Time : 2021/11/29 20:35
# @Author : DongYun
# @File : 1588.所有奇数长度子数组的和.py
# @Software : PyCharm
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        resoult=0
        for i in range(len(arr)):
            sub_arr_len = 1
            while i +sub_arr_len <=len(arr):
                resoult+=sum(arr[i:i+sub_arr_len])
                sub_arr_len+=2
        return resoult

print(Solution().sumOddLengthSubarrays([1,4,2,5,3]))