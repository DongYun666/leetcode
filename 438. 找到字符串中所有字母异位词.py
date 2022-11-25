# -*- codeing = utf-8 -*-
# @Time : 2021/11/28 20:39
# @Author : DongYun
# @File : 438. 找到字符串中所有字母异位词.py
# @Software : PyCharm
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        resoult = []
        s_count = [0]*26
        p_count = [0]*26
        left,right = 0,len(p)-1
        for ch in p:
            p_count[ord(ch)-ord('a')] +=1
        while right < len(s):
            for ch in s[left:right+1]:
                s_count[ord(ch)-ord('a')]+=1
            if p_count == s_count:
                resoult.append(left)
            s_count = [0] * 26
            if right + 1 < len(s) and s[right + 1] not in p:
                left = right+2
                right = left+len(p)-1
            else:
                left+=1
                right+=1
        return resoult

print(Solution().findAnagrams("abab","ab"))