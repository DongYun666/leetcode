from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right,ans = 0,len(arr)-1,0
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] > arr[middle+1]:
                ans = middle
                right = middle - 1
            else:
                left = middle + 1
        return ans

arr = [0,10,5,2]
print(Solution().peakIndexInMountainArray(arr))