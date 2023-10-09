from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找
        if len(nums) == 1 or nums[0]<nums[-1]:
            return nums[0]
        nums = nums+[nums[0]]
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[r]


nums = [5, 6, 7, 0 ,1,2,4]
print(Solution().findMin(nums))


