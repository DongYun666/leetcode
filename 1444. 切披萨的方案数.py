from functools import cache
from typing import List
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m,n,mod = len(pizza),len(pizza[0]),10**9 + 7
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                apples[i][j] = apples[i][j + 1] + apples[i + 1][j] - apples[i + 1][j + 1] + (pizza[i][j] == "A")
        @cache
        def dfs(c,i,j):
            if c == 0:
                return 1 if apples[i][j] > 0 else 0
            res = 0
            for x in range(i + 1,m):
                if apples[i][j] - apples[x][j] > 0:
                    res += dfs(c - 1,x,j)
            for y in range(j + 1,n):
                if apples[i][j] - apples[i][y] > 0:
                    res += dfs(c - 1,i,y)
            return res % mod
        
        return dfs(k - 1,0,0) % mod

pizza = ["A..","AAA","..."]
k = 3
print(Solution().ways(pizza, k))