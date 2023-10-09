from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = 0
        right = 0
        sum = 0
        res = float('inf')
        dp = [float('inf')] * n
        while right < n:
            sum += arr[right]
            while sum > target:
                sum -= arr[left]
                left += 1
            if sum == target:
                if left > 0 and dp[left-1] != float('inf'):
                    res = min(res,dp[left-1] + right - left + 1)
                dp[right] = min(dp[right-1],right - left + 1)
            else:
                if right > 0:
                    dp[right] = dp[right-1]
            right += 1
        return res if res != float('inf') else -1
arr = [4,3,2,6,2,3,4]
target = 6

arr = [7,3,4,7]
target = 7
print(Solution.minSumOfLengths(Solution,arr,target))