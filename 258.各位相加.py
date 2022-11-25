# -*- codeing = utf-8 -*-
# @Time : 2022/3/3 11:01
# @Author : DongYun
# @File : 258.各位相加.py
# @Software : PyCharm
class Solution:
    def addDigits(self, num: int) -> int:
        while num>10:
            sum = 0
            while num:
                sum+=num%10
                num//=10
            num = sum
        return num


num = 38
print(Solution().addDigits(num))