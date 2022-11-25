# -*- codeing = utf-8 -*-
# @Time : 2022/4/27 19:10
# @Author : DongYun
# @File : 62.不同路径.py
# @Software : PyCharm
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m,n = n,m
        if n == 1:
            return 1
        if n == 2:
            return m
        if n == 3:
            return (m+1)*m//2
        return (m+1)*m//2+m*(m-1)*(n-3)

m = 7
n = 4
print(Solution().uniquePaths(m,n))