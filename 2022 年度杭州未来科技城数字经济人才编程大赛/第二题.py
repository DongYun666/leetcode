# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 10:52
# @Author : DongYun
# @File : 第二题.py
# @Software : PyCharm

from typing import List


class Solution:
    def minSwaps(self, chess: List[int]) -> int:
        def sumhei(index, legth, chess):
            sumz = 0
            for i in range(index, legth + index):
                sumz += chess[i]
            return sumz
        sum_ = sumhei(0, len(chess), chess)
        sumzi = sumhei(0, sum_, chess)
        temp = sumzi
        for i in range(sum_, len(chess)):
            temp = temp + chess[i] - chess[i - sum_]
            sumzi = max(sumzi, temp)
        return sum_ - sumzi


chess = [1,0,1,0,1,0]
print(Solution().minSwaps(chess))