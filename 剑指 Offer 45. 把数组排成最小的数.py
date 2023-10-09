from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        def quick_sort(l,r):
            if l >= r:
                return
            i,j = l,r
            while i < j:
                while i < j and nums[j] + nums[l] >= nums[l] + nums[j]:
                    j -= 1
                while i < j and nums[i] + nums[l] <= nums[l] + nums[i]:
                    i += 1
                nums[i],nums[j] = nums[j],nums[i]
            nums[i],nums[l] = nums[l],nums[i]
            quick_sort(l,i-1)
            quick_sort(i+1,r)
        quick_sort(0,len(nums)-1)
        return ''.join(nums)

nums = [3,30,34,5,9]
print(Solution().minNumber(nums))