from typing import List
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [float("inf")]*(1<<n)
        dp[0] = 0
        for mask in range(1<<n):
            cnt = bin(mask).count("1")
            for i in range(n):
                if mask&(1<<i):
                    dp[mask] = min(dp[mask],dp[mask^(1<<i)]+(nums1[cnt-1]^nums2[i]))
        return dp[-1]

nums1 = [0,1,3,5,6,8]
nums2 = [1,2,4,8,7,6]
print(Solution().minimumXORSum(nums1,nums2))