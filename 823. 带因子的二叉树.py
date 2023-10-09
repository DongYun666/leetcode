from typing import List
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        n = len(arr)
        index = {x:i for i,x in enumerate(arr)}
        dp = [1] * n
        for i in range(n):
            for left in range(i):
                if arr[i] % arr[left] == 0:
                    right = arr[i] // arr[left]
                    if right in index:
                        dp[i] += dp[left] * dp[index[right]]
                        dp[i] %= (mod)
        return sum(dp) % (mod)
    
arr = [2,4,5,10,20]
print(Solution().numFactoredBinaryTrees(arr))