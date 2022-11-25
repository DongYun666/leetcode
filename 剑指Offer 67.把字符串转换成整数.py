# -*- codeing = utf-8 -*-
# @Time : 2022/7/21 14:33
# @Author : DongYun
# @File : 剑指Offer 67.把字符串转换成整数.py
# @Software : PyCharm
class Solution:
    def strToInt(self, str) -> int:
        res = 1
        str = str.strip()
        if str[0] == "-":
            res*=-1
            str = str[1:]
        for x in str:
            res *= 10
            if 48<=ord(x)<=57:
                res+=(ord(x)-48)
            else:
                break
        return res
str = "    -42"
print(Solution().strToInt(str))