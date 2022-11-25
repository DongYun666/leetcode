from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        dp1 = [0]*len(arr)
        dp2 = [0]*len(arr)
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                dp1[i] = dp1[i-1]+1
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>arr[i+1]:
                dp2[i] = dp2[i+1]+1
        res = 0
        for i in range(len(arr)):
            if dp1[i]>0 and dp2[i]>0:
                res = max(res,dp1[i]+dp2[i]+1)
        return res,dp1,dp2


arr = [2, 1, 4, 7, 3, 2, 5]
# arr = [2,2,2]
# arr = [7,4,8]
arr = [2,3]
arr = [2,3,1,2,3,4,5,6]
print(Solution().longestMountain(arr))