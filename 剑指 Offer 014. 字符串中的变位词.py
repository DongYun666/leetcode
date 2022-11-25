# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 20:06
# @Author : DongYun
# @File : 剑指 Offer 014. 字符串中的变位词.py
# @Software : PyCharm
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_count = Counter(s1)
        print(s1_count)
        for index,s in enumerate(s2[0:(len(s2)-n-1)]):
            if s in s1:
                s2_counter = Counter(s2[index:index+n-1])
                if s2_counter == s1_count:
                    return True
        return False
s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1,s2))
