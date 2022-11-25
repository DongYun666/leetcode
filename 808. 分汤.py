from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        n = (n+24)//25
        @cache
        def dfs(a,b):
            if a <= 0 and b<=0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0
            return (dfs(a-4,b)+dfs(a-3,b-1)+dfs(a-2,b-2)+dfs(a-1,b-3))/4
        return dfs(n,n)




n = 1
print(Solution().soupServings(n))