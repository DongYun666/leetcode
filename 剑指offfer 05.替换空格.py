# -*- codeing = utf-8 -*-
# @Time : 2022/3/7 10:35
# @Author : DongYun
# @File : 剑指offfer 05.替换空格.py
# @Software : PyCharm

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")



s = "We are happy."
print(Solution().replaceSpace(s))


