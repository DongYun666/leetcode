from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        greater,lower = [1],[1]
        res = 1
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                lower.append(greater[-1]+1)
                greater.append(1)
            elif arr[i] > arr[i-1]:
                greater.append(lower[-1]+1)
                lower.append(1)
            else:
                lower.append(1)
                greater.append(1)
            res = max([res,greater[i],lower[i]])
        return res




arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
arr = [4,8,12,16]
arr = [100]
arr = [9,9]
print(Solution().maxTurbulenceSize(arr))