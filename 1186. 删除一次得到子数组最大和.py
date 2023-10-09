from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp1,dp0,res = arr[0],0,arr[0]
        for i in range(1,len(arr)):
            dp1,dp0 = max(dp1+arr[i],dp0),max(dp0+arr[i],dp1)
            res = max(res,dp1,dp0)
        return res
    
arr = [1,-2,0,3]
print(Solution().maximumSum(arr))