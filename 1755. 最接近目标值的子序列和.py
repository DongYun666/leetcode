# -*- codeing = utf-8 -*-
# @Time : 2022/3/31 15:08
# @Author : DongYun
# @File : 1755. 最接近目标值的子序列和.py
# @Software : PyCharm
from bisect import bisect_left
from typing import List

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def divide_and_conquer(lst, left, right):
            if left == right:
                return 0
            center = (left + right) // 2
            # 左边界最大子序列和右边界最大子序列
            max_left_sum = divide_and_conquer(lst, left, center)
            max_right_sum = divide_and_conquer(lst, center + 1, right)

            max_left_border_sum ,left_border_sum = float("inf"),0
            for i in range(center, left - 1, -1):
                left_border_sum += lst[i]
                if abs(left_border_sum-goal) < max_left_border_sum:
                    max_left_border_sum = left_border_sum

            max_right_border_sum,right_border_sum = float("inf"),0
            for i in range(center + 1, right + 1):
                right_border_sum += lst[i]
                if abs(right_border_sum-goal) < max_right_border_sum:
                    max_right_border_sum = right_border_sum

            # 左、右与跨越边界的子序列
            return min(max_left_sum, max_right_sum, max_left_border_sum + max_right_border_sum)
        return divide_and_conquer(nums,0,len(nums)-1)


    def minAbsDifference2(self, nums: List[int], goal: int) -> int:
        part1, part2 = nums[::2], nums[1::2]

        parts_sum = [{0}, {0}]
        for i, numbers in enumerate([part1, part2]):
            for num in numbers:
                parts_sum[i] |= {num + s for s in parts_sum[i]}
        part1_sum, part2_sum = parts_sum
        part2_sum = sorted(part2_sum)

        result = abs(goal)
        for num in part1_sum:
            target = goal - num
            if part2_sum[0] - result < target < part2_sum[-1] + result:
                index = bisect_left(part2_sum, target)
                for i in [index - 1, index]:
                    if 0 <= i < len(part2_sum):
                        result = min(result, abs(target - part2_sum[i]))
                        if result == 0:
                            return 0

        return result
nums = [1,2,3]
goal = -7
print(Solution().minAbsDifference2(nums,goal))

