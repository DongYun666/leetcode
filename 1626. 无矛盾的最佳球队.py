from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores,ages = zip(*sorted(zip(scores,ages),key=lambda x: (x[1],x[0])))
        print(ages)
        print(scores)
        dp = [0]*len(scores)
        res = 0
        for i in range(len(scores)):
            dp[i] = scores[i]
            for j in range(i):
                if scores[j]<=scores[i]:
                    dp[i] = max(dp[i],dp[j]+scores[i])
            res = max(res,dp[i])

        return res,dp



scores = [1, 3, 5, 10, 15]
ages = [1, 2, 3, 4, 5]

scores = [4,5,6,5]
ages = [2,1,2,1]
#
# scores = [1,2,3,5]
# ages = [8,9,10,1]
print(Solution().bestTeamScore(scores, ages))



