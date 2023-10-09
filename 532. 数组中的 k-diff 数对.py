from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited = set()
        res = set()
        for num in nums:
            if num - k in visited:
                res.add((num - k, num))
            if num + k in visited:
                res.add((num, num + k))
            visited.add(num)
        return len(res)
    
    
        


nums = [3, 1, 4, 1, 5]
k = 2

nums = [1, 3, 1, 5, 4, 2]
k = 0
print(Solution().findPairs(nums, k))