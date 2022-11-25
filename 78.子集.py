from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def dfs(cur):
            if cur == len(nums):
                res.append(temp[:])
                return
            temp.append(nums[cur])
            dfs(cur+1)
            temp.pop()
            dfs(cur+1)
        dfs(0)
        return res
nums = [1,2,3]
print(Solution().subsets(nums))