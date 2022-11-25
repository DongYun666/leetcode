# -*- codeing = utf-8 -*-
# @Time : 2022/3/31 11:16
# @Author : DongYun
# @File : 1414.和为k的最少斐波那契额数字数目.py
# @Software : PyCharm

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        Fibonacci = [1,1]
        while k>=Fibonacci[-1]:
            Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
        ans , i = 0 ,len(Fibonacci)-1
        while k:
            if k >=Fibonacci[i]:
                k-=Fibonacci[i]
                ans+=1
            i-=1
        return ans



print(Solution().findMinFibonacciNumbers(19))