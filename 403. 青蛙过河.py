from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        visited = set()
        def dfs(index,k):
            if (index,k) in visited:
                return False
            if index == len(stones)-1: #走到终点
                return True
            for i in range(index+1,len(stones)):
                if stones[i] - stones[index] > k+1:
                    visited.add((index,k))
                    break
                if stones[i] - stones[index] >= k-1:
                    if dfs(i,stones[i]-stones[index]):
                        return True
            return False
        return dfs(0,0)
stones = [0,1,3,5,6,8,12,17]
print(Solution().canCross(stones))