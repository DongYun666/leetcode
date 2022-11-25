# -*- codeing = utf-8 -*-
# @Time : 2021/12/4 8:50
# @Author : DongYun
# @File : 960.删列造序.py
# @Software : PyCharm
from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        W = len(strs[0])
        dp = [1] * W
        for i in range(W - 2, -1, -1):
            for j in range(i + 1, W):
                if all(row[i] <= row[j] for row in strs):
                    dp[i] = max(dp[i], 1 + dp[j])
        return W - max(dp)

print(Solution().minDeletionSize(["abcd"]))