from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[float("inf"),float("inf")] for _ in range(len(nums1))]
        dp[0] = [0,1]
        for i in range(1,len(nums1)):
            if nums1[i]>nums1[i-1] and nums2[i]>nums2[i-1]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]+1
            if nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]:
                dp[i][0] = min(dp[i][0],dp[i-1][1])
                dp[i][1] = min(dp[i][1],dp[i-1][0]+1)
        return min(dp[-1])



nums1 = [0, 3, 5, 8, 9]
nums2 = [2, 1, 4, 6, 9]
print(Solution().minSwap(nums1, nums2))