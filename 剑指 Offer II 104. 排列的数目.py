from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        def dfs(index,tt):
            if tt == 0:
                nonlocal res
                res += 1
                return
            if tt < 0 or index == n:
                return
            for i in range(0,n):
                dfs(i,tt-nums[i])
        dfs(0,target)
        return res
    
nums = [1,2,3]
target = 4

nums = [4,2,1]
target = 32
print(Solution().combinationSum4(nums,target))

