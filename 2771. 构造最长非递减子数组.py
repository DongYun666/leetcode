from typing import List
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[1]* n for _ in range(2)]
        for i in range(1,n):
            if nums1[i] >= nums1[i-1]:
                dp[0][i] = dp[0][i-1] + 1
            if nums1[i] >= nums2[i-1]:
                dp[0][i] = max(dp[0][i],dp[1][i-1] + 1)
            if nums2[i] >= nums2[i-1]:
                dp[1][i] = dp[1][i-1] + 1
            if nums2[i] >= nums1[i-1]:
                dp[1][i] = max(dp[1][i],dp[0][i-1] + 1)
        return max(max(dp[0]),max(dp[1]))
    
nums1 = [2,3,1]
nums2 = [1,2,1]

# nums1 = [1,3,2,1]
# nums2 = [2,2,3,4]

# nums1 = [1,1]
# nums2 = [2,2]

# nums1 = [8,7,4]
# nums2 = [13,4,4]
print(Solution().maxNonDecreasingLength(nums1,nums2))