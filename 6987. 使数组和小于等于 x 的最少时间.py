from typing import List
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        nums = sorted((nums2[i],nums1[i]) for i in range(n))
        f = [0] * (n+1)
        for l,r in nums:
            for i in range(n-1,-1,-1):
                f[i + 1] = max(f[i + 1],f[i] + (i + 1) *l + r)
        nums2_sum = sum(nums2)
        nums1_sum = sum(nums1)
        print(f)
        for i in range(n+1):
            if nums2_sum * i + nums1_sum - f[i] <= x:
                return i
        return -1
    

        # n = len(nums1)
        # p = sorted([(nums2[i], nums1[i]) for i in range(n)])
        # f = [0] * (n + 1)
        # for x, y in p:
        #     for i in reversed(range(n)):
        #         f[i + 1] = max(f[i + 1], f[i] + (i + 1) * x + y)
        # k = sum(nums2)
        # b = sum(nums1)
        # for i in range(0, n + 1):
        #     if k * i + b - f[i] <= xx:
        #         return i
        # return -1
    
nums1 = [1,2,3]
nums2 = [1,2,3]
x = 4

print(Solution().minimumTime(nums1,nums2,x))