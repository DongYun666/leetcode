from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def dfs(cur):
            if cur == len(nums):
                ans.append(temp[:])
                return
            temp.append(nums[cur])
            dfs(cur + 1)
            temp.pop()
            dfs(cur + 1)
        dfs(0)
        return ans



nums = [1,2,3]
print(Solution().subsets(nums))