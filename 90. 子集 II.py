from functools import cache
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        self.dfs(nums,0,res,path)
        return res
    def dfs(self,nums,index,res,path):
        res.append(path[:])
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums,i + 1,res,path)
            path.pop()
    
nums = [1,2,2]
print(Solution().subsetsWithDup(nums))