from typing import List

class Solution:
    def maxChunksToSorted2(self, arr: List[int]) -> int:
        res,region_max= 0,0
        for i,num in enumerate(arr):
            region_max = max(region_max,num)
            res += region_max == i
        return res


    def maxChunksToSorted(self, arr: List[int]) -> int:
        res,region_max = 1,arr[0]
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                if region_max < arr[i]:
                    res+=1
                    region_max = max(region_max,arr[i])
                else:
                    break
        return res















arr = [1,0,2,3,4]
# arr = [4,3,2,1,0]
# arr = [2,0,1]
print(Solution().maxChunksToSorted(arr))