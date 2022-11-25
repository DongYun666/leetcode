class Solution:
    def numTilings1(self, n: int) -> int:
        num = [1,2,3,3,4,4]
        res = 0
        res_l = []
        temp = 0
        temp_l = []
        def dfs(target):
            if target<0:
                return
            if target == 0:
                res_l.append(temp_l[:])
                nonlocal res
                res = (res+1)% (10**9+7)
                return
            for i in range(len(num)):
                nonlocal temp
                temp +=num[i]
                temp_l.append(num[i])
                dfs(target - num[i])
                temp-=num[i]
                temp_l.pop()
        dfs(n)
        print(res,res_l)
        return res

    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        dp = [0]*(n+2)
        dp[0] = dp[1] = 1
        dp[2] = 2
        for i in range(3,n+2):
            dp[i] = (2*dp[i-1]+dp[i-3])%mod
        return dp[-1]
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        a,b,c = 1,1,2
        for i in range(3,n+1):
            a,b,c = b,c,(2*c+a)%mod
        return c
n = 5
print(Solution().numTilings(n))