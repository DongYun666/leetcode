# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 19:46
# @Author : DongYun
# @File : 2220.转换数字的最少位翻转次数.py
# @Software : PyCharm

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        count = 0
        while x > 0:
            x &= (x-1)
            count+=1
        return count

print(Solution().minBitFlips(10,7))