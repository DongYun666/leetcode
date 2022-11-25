from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        temp=0
        for i in range(len(nums)):
            temp+=nums[i]*cost[i]
        sum_cost = sum(cost)
        target = temp//sum_cost
        res = 0
        for index,c in enumerate(cost):
            res+=abs(nums[index]-target)*c
        return res

nums = [1, 3, 5, 2]
cost = [2, 3, 1, 14]

nums = [2,2,2,2,2]
cost = [4,2,8,1,3]
print(Solution().minCost(nums, cost))