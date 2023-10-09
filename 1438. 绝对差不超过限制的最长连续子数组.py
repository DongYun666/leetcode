from collections import deque
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        quemax,quemin = deque(),deque()
        left = right = res = 0
        while right < n:
            while quemax and quemax[-1] < nums[right]:
                quemax.pop()
            while quemin and quemin[-1] > nums[right]:
                quemin.pop()
            quemax.append(nums[right])
            quemin.append(nums[right])
            while quemax and quemin and quemax[0]-quemin[0] > limit:
                if nums[left] == quemax[0]:
                    quemax.popleft()
                if nums[left] == quemin[0]:
                    quemin.popleft()
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res
nums = [8,2,4,7]
limit = 4

nums = [10,1,2,4,7,2]
limit = 5
print(Solution().longestSubarray(nums,limit))