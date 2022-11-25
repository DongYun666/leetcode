# -*- codeing = utf-8 -*-
# @Time : 2022/7/21 11:43
# @Author : DongYun
# @File : 剑指 Offer 64. 求1+2+…+n.py
# @Software : PyCharm
class Solution:
    def sumNums(self, n: int) -> int:
        return n*(n+1)>>1

print(Solution().sumNu1ms(3))
