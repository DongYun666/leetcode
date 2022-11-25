# -*- codeing = utf-8 -*-
# @Time : 2022/5/6 19:30
# @Author : DongYun
# @File : 96.py
# @Software : PyCharm
class Solution:
    def numTrees(self, n: int) -> int:
        bp = [0]*(n+1)
        bp[0] = 1
        for i in range(1,n+1):
            for j in range(0,i):
                bp[i]+=bp[j]*bp[i-j-1]
        # print(bp)
        return bp[n]


n = 3
print(Solution().numTrees(n))
