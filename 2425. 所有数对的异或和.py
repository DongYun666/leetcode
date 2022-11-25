from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = 0,0
        for num in nums1: n1^=num
        for num in nums2: n2^=num
        l1,l2 = len(nums1),len(nums2)
        if l1%2 == 0 and l2%2 == 0: return 0
        if l1%2 == 0 and l2%2 != 0: return n1
        if l1%2 != 0 and l2%2 == 0: return n2
        if l1%2 != 0 and l2%2 != 0: return n1^n2

nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
print(Solution().xorAllNums(nums1, nums2))