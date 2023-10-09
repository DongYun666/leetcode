# -*- codeing = utf-8 -*-
# @Time : 2021/10/19 21:09
# @Author : DongYun
# @File : 264.丑数2.py
# @Software : PyCharm

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2,p3,p5 = 1,1,1
        for i in range(2,n + 1):
            num2,num3,num5 = dp[p2] * 2,dp[p3] * 3,dp[p5] * 5
            dp[i] = min(num2,num3,num5)
            if num2 == dp[i]:
                p2 += 1
            if num3 == dp[i]:
                p3 += 1
            if num5 == dp[i]:
                p5 += 1
        return dp[n]
    
n = 10
print(Solution().nthUglyNumber(n))