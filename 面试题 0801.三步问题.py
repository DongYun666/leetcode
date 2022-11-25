# -*- codeing = utf-8 -*-
# @Time : 2021/12/2 20:23
# @Author : DongYun
# @File : 面试题 0801.三步问题.py
# @Software : PyCharm
from typing import List

class Solution:
    def waysToStep(self, n: int) -> int:
        count = 0
        def dfs(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 4
            return dfs(n-1)+dfs(n-2)+dfs(n-3)
        return dfs(n)
    def waysToStep2(self, n: int) -> int:
        resoult = [0]*(n+3)
        resoult[0],resoult[1],resoult[2] = 1,1,2
        for i in range(3,n+1):
            resoult[i] = (resoult[i-1]+resoult[i-2]+resoult[i-3]) % 1000000007
        return resoult[n]


    def waysToStep3(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        mat = [
            [1, 1, 0],
            [1, 0, 1],
            [1, 0, 0],
        ]

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            rows, columns, temp = len(a), len(b[0]), len(b)
            c = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    c[i][j] = sum(a[i][k] * b[k][j] for k in range(temp)) % MOD
            return c

        def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
            ret = [[2, 1, 1]]
            while n > 0:
                if (n & 1) == 1:
                    ret = multiply(ret, mat)
                n >>= 1
                mat = multiply(mat, mat)
            return ret

        res = matrixPow(mat, n)
        return res[0][-1]
        # ans = sum(res[0])
        # return ans % MOD

        # dp = [1, 1, 2, 4]
        # for i in range(4, n + 1):
        #     dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007)
        # # print(dp)
        # return dp[n]
print(Solution().waysToStep2(61))