# -*- codeing = utf-8 -*-
# @Time : 2022/3/26 8:49
# @Author : DongYun
# @File : 1300. 转变数组后最接近目标值的数组和.py
# @Software : PyCharm
import bisect
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        r, ans, diff = max(arr), 0, target
        for i in range(target//len(arr), r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans


arr = [60864,25176,27249,21296,20204]
target = 56803
print(Solution().findBestValue(arr,target))