class Solution:
    def findIntegers1(self, n: int) -> int:
        res = 0
        for i in range(n+1):
            if i&i<<1 == 0:
                res+=1
        return res
    def findIntegers(self, n: int) -> int:
        res = 1
        def dfs(x):
            if x > n:
                return
            nonlocal res
            res += 1
            if x & 1:
                dfs(x<<1)
            else:
                dfs(x<<1)
                dfs((x<<1)+1)
        dfs(1)
        return res






n = 8
print(Solution().findIntegers(n))