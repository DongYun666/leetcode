class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        if k ==1:
            return 1
        dp = [0]*(k+1)
        dp[1] = 1
        i_3,i_5,i_7 = 1,1,1
        i = 2
        while i <= k:
            n_3,n_5,n_7 = dp[i_3]*3,dp[i_5]*5,dp[i_7]*7
            dp[i] = min(n_3,n_5,n_7)
            if dp[i] == n_3:
                i_3 += 1
            if dp[i] == n_5:
                i_5 += 1
            if dp[i] == n_7:
                i_7 += 1
            i+=1
        return dp[k]
k = 6
print(Solution().getKthMagicNumber(k))