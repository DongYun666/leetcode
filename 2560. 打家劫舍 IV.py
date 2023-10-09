from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(x):
            visted = False
            count = 0
            for num in nums:
                if num <= x and not visted:
                    count += 1
                    visted = True
                else:
                    visted = False
            return count >= k
        left,right = min(nums),max(nums)
        while left<right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left
    
nums = [2,3,5,9]
k = 2

nums = [2,7,9,3,1] 
k = 2
print(Solution().minCapability(nums,k))