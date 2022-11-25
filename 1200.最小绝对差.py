from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        current_min = arr[1]-arr[0]
        res = [[arr[0],arr[1]]]
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1] == current_min:
                res.append([arr[i-1],arr[i]])
            elif arr[i]-arr[i-1] < current_min:
                res = []
                res.append([arr[i-1],arr[i]])
                current_min = arr[i]-arr[i-1]
        return res

arr = [40,11,26,27,-20]
print(Solution().minimumAbsDifference(arr))