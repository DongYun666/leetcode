# -*- codeing = utf-8 -*-
# @Time : 2022/3/7 11:24
# @Author : DongYun
# @File : 剑指 Offer 58.左旋转字符串.py
# @Software : PyCharm

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]
s = "abcdefg"
k = 2
print(Solution().reverseLeftWords(s,k))
