from statistics import mean
from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        new_arr = arr[int(len(arr)*0.05) : int(len(arr)-len(arr)*0.05)]
        print(mean(new_arr))

arr = [4, 8, 4, 10, 0, 7, 1, 3, 7, 8, 8, 3, 4, 1, 6, 2, 1, 1, 8, 0, 9, 8, 0, 3, 9, 10, 3, 10, 1, 10, 7, 3, 2, 1,
               4, 9, 10, 7, 6, 4, 0, 8, 5, 1, 2, 1, 6, 2, 5, 0, 7, 10, 9, 10, 3, 7, 10, 5, 8, 5, 7, 6, 7, 6, 10, 9, 5,
               10, 5, 5, 7, 2, 10, 7, 7, 8, 2, 0, 1, 1]
print(Solution().trimMean(arr))