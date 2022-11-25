from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n]*n for _ in range(n)]
        for i,j in mines:
            dp[i][j] = 0
        for i in range(n):
            count = 0
            # 右
            for j in range(n):
                if dp[i][j]!=0:
                    count+=1
                else:
                    count = 0
                dp[i][j] = min(dp[i][j],count)
            count = 0
            # 左
            for j in range(n-1,-1,-1):
                if dp[i][j]!=0:
                    count+=1
                else:
                    count = 0
                dp[i][j] = min(dp[i][j],count)

        for j in range(n):
            count = 0
            #下
            for i in range(n):
                if dp[i][j]!=0:
                    count+=1
                else:
                    count = 0
                dp[i][j] = min(dp[i][j],count)
            count = 0
            #上
            for i in range(n-1,-1,-1):
                if dp[i][j]!=0:
                    count+=1
                else:
                    count= 0
                dp[i][j] = min(dp[i][j],count)
        print(dp)
        return max(map(max,dp))

n = 5
mines = [[4, 2]]
print(Solution().orderOfLargestPlusSign(n, mines))