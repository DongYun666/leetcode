from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = min(baseCosts)
        def dfs(index,cur_cost):
            nonlocal res
            if res - target < cur_cost-target:
                return

            if abs(res - target) >= abs

            if index == len(baseCosts):
                return
            dfs(index+1,cur_cost + toppingCosts[index]*2)
            dfs(index+1,cur_cost + toppingCosts[index])
            dfs(index+1,cur_cost)
        for c in baseCosts:
            dfs(0,c)
        return res





baseCosts = [2, 3]
toppingCosts = [4, 5, 100]
target = 18
print(Solution().closestCost(baseCosts,toppingCosts,target))