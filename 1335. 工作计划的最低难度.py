from functools import lru_cache
from typing import List

# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         if d > len(jobDifficulty):
#             return -1
#         if d == len(jobDifficulty):
#             return sum(jobDifficulty)
#         dp = [[0 for _ in range(len(jobDifficulty))] for _ in range(d)]
#         dp[0][0] = jobDifficulty[0]
#         for i in range(1,len(jobDifficulty)):
#             dp[0][i] = max(jobDifficulty[i],dp[0][i-1])
#         for i in range(1,d):
#             for j in range(i,len(jobDifficulty)):
#                 dp[i][j] = float("inf")
#                 maxd = 0
#                 for k in range(j,i-1,-1):
#                     maxd = max(maxd,jobDifficulty[k])
#                     dp[i][j] = min(dp[i][j],dp[i-1][k-1]+maxd)
#         return dp[-1][-1]
    
        
# jobDifficulty = [11,111,22,222,33,333,44,444]
# d = 6
# print(Solution().minDifficulty(jobDifficulty,d))

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dfs(left,day):
            if day == 1:
                return max(jobDifficulty[left:])
            base = 0
            resoult = sum(jobDifficulty[left:])
            for i in range(left,len(jobDifficulty)-day+1):
                base = max(base,jobDifficulty[i])
                resoult = min(resoult,base+dfs(i+1,day-1))
            return resoult

        if d > len(jobDifficulty):
            return -1
        return dfs(0,d)
jobDifficulty = [11,111,22,222,33,333,44,444]
d = 6
print(Solution().minDifficulty(jobDifficulty,d))