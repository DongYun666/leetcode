# -*- codeing = utf-8 -*-
# @Time : 2021/12/1 18:27
# @Author : DongYun
# @File : 1446. 连续字符.py
# @Software : PyCharm
class Solution:
    def maxPower(self, s: str) -> int:
        record = s[0]
        count = 1
        max_count = count
        for ch in s[1:]:
            if record == ch:
                count+=1
                max_count = max(count,max_count)
            else:
                max_count = max(count,max_count)
                record = ch
                count = 1
        return max_count

print(Solution().maxPower("abbcccddddeeeeedcba"))