from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        temp = []
        i,j = 0,len(nums)-1
        while i<=j:
            t = (nums[i] + nums[j])/2
            if t not in temp:
                temp.append(t)
            i += 1
            j -= 1
        return len(temp)



nums = [4, 1, 4, 0, 3, 5]

nums = [1,100]
print(Solution().distinctAverages(nums))