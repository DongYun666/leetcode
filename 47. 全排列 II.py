from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index):
            if index == len(nums):
                res.append(nums[:])
            visited = [0 for i in range(22)]
            for i in range(index,len(nums)):
                if not visited[nums[i]+10]:
                    visited[nums[i]+10] = 1
                    nums[index],nums[i] = nums[i],nums[index]
                    dfs(index+1)
                    nums[index],nums[i] = nums[i],nums[index]
        dfs(0)
        return res

nums = [1, 2, 1]
print(Solution().permuteUnique(nums))