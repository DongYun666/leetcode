# -*- codeing = utf-8 -*-
# @Time : 2021/12/3 15:50
# @Author : DongYun
# @File : 1005.K次取反后最大化的数组和.py
# @Software : PyCharm
from collections import Counter
from typing import List
import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        index = 0
        while k != 0:
            if nums[index] < 0:
                nums[index] *=-1
                index+=1
                k -= 1
            if nums[index] >= 0:
                nums.sort()
                nums[0] *=-1
                k -= 1
        return sum(nums)
    def largestSumAfterKNegations2(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
        while k != 0:
            x = heapq.heappop(heap)
            heapq.heappush(heap,-x)
            k-=1
        return sum(heap)


    def largestSumAfterKNegations3(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i]:
                ops = min(k, freq[i])
                ans += -i * ops * 2
                freq[i] -= ops
                freq[-i] += ops
                k -= ops
                if k == 0:
                    break

        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break

        return ans




print(Solution().largestSumAfterKNegations3([4,2,3],1))