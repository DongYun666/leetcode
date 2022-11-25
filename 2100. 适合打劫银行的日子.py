# -*- codeing = utf-8 -*-
# @Time : 2022/3/6 9:48
# @Author : DongYun
# @File : 2100. 适合打劫银行的日子.py
# @Software : PyCharm
from typing import List
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        g = [0] * n
        for i in range(1,n):
            if security[i] == security[i-1]:
                continue
            g[i] = 1 if security[i]>security[i-1] else -1
        a = [0] * (n+1)
        b = [0] * (n+1)
        for i in range(1,n+1):
            a[i] = a[i-1]+(1 if g[i-1] == 1 else 0)
        for i in range(1,n+1):
            b[i] = b[i-1]+(1 if g[i-1] == -1 else 0)
        ans = []
        for i in range(time,n-time):
            c1 = a[i+1]-a[i+1-time]
            c2 = b[i+1+time] - b[i+1]
            if c1==0 & c2 ==0:
                ans.append(i)
        return ans
    def goodDaysToRobBank2(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        ans = []
        left,right = [0]*n,[0]*n
        for i in range(1,n):
            if security[i] <=security[i-1]:
                left[i] = left[i-1]+1
        for i in range(n-2,-1,-1):
            if security[i] <= security[i+1]:
                right[i] = right[i+1] +1
        for i in range(time,n-time):
            if left[i]>=time and right[i]>=time:
                ans.append(i)
        return ans

security = [2,4,0,5,5]
time = 1
print(Solution().goodDaysToRobBank2(security,time))