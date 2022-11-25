# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 10:31
# @Author : DongYun
# @File : 806.写字符串需要的行数.py
# @Software : PyCharm

from typing import List
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        hang = 1
        count = 0
        for ch in s:
            count+=widths[ord(ch)-ord("a")]
            if count > 100:
                hang+=1
                count = widths[ord(ch)-ord("a")]
        return [hang,count]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"

print(Solution().numberOfLines(widths,S))