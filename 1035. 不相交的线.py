from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums2)+1)] for j in range(len(nums1)+1)]
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

nums1 = [2, 5, 1, 2, 5]

nums2 = [10, 5, 2, 1, 5, 2]

nums1 = [1,4,2]
nums2 = [1,2,4]
print(Solution().maxUncrossedLines(nums1, nums2))