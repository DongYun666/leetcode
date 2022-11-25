# -*- codeing = utf-8 -*-
# @Time : 2022/3/16 15:27
# @Author : DongYun
# @File : 剑指Offer10-1 斐波那契额数列.py
# @Software : PyCharm
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        list_ = [0] * (n + 1)
        list_[1] = 1
        for i in range(2, n + 1):
            list_[i] = list_[i - 1] + list_[i - 2]
        return list_[n]

print(Solution().fib(2))