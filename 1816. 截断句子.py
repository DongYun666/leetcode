# -*- codeing = utf-8 -*-
# @Time : 2021/12/6 17:18
# @Author : DongYun
# @File : 1816. 截断句子.py
# @Software : PyCharm
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # return " ".join(s.split()[:k])
        resoult = ""
        for ch in s:
            if ch == " ":
                k-=1
                if k == 0:
                    return resoult
            resoult+=ch
        return resoult


print(Solution().truncateSentence("chopper is not a tanuki", k = 5))















