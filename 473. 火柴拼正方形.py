from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_,n = sum(matchsticks),len(matchsticks)
        if sum_ % 4 or n < 4:
            return False
        target = sum_ // 4
        ids = [0] * 4
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i == n:
                return True
            for j in range(4):
                if ids[j] + matchsticks[i] <= target:
                    ids[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    ids[j] -= matchsticks[i]
            return False
        return dfs(0)
matchsticks = [1,1,2,2,2]
matchsticks = [3,3,3,3,4]
matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
matchsticks = [1,1,1,1,2,2,2,2,3,3,3,3]
print(Solution().makesquare(matchsticks))
