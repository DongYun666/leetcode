from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        n = len(nums)
        res = []
        while i < n:
            low = i
            i += 1
            while i < n and nums[i] == nums[i-1] + 1:
                i += 1
            high = i - 1
            temp = str(nums[low])
            if low < high:
                temp += "->" + str(nums[high])
            res.append(temp)
        return res
nums = [0,1,2,4,5,7]
print(Solution().summaryRanges(nums))