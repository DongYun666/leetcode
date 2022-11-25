from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [0]*n
        nums1.sort()
        ids = sorted(range(n),key=lambda i: nums2[i])
        left,right = 0,n-1
        for x in nums1:
            if x > nums2[ids[left]]:
                ans[ids[left]] = x
                left+=1
            else:
                ans[ids[right]] = x
                right+=1
        return ans

nums1 = [12, 24, 8, 32]
nums2 = [13, 25, 32, 11]
print(Solution().advantageCount(nums1, nums2))