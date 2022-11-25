from collections import Counter
from typing import List

class Solution:
    def findSwapValues2(self, array1: List[int], array2: List[int]) -> List[int]:
        sum_1 = sum(array1)
        sum_2 = sum(array2)
        array2.sort()
        diff = sum_1 - sum_2
        if diff % 2 != 0:
            return []
        else:
            diff //=2
        def bisearch(arr, x):
            if x not in arr or x > arr[-1]:
                return -1
            left, right = -1, len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    return mid
                if arr[mid] > x:
                    right = mid
                else:
                    left = mid + 1
            return left
        for num in array1:
            temp = bisearch(array2,num-diff)
            if temp!=-1:
                return [num,array2[temp]]
        return []
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        array1.sort()
        array2.sort()
        sum_1 = sum(array1)
        sum_2 = sum(array2)
        cnt = Counter(array2)
        diff = sum_1 - sum_2
        if diff % 2 != 0:
            return []
        else:
            diff //= 2
        for num in array1:
            if num-diff in cnt.keys():
                return [num,num-diff]
        return []


array1 = [4, 1, 2, 1, 1, 2]
array2 = [3, 6, 3, 3]

# array1 = [1,2,3]
# array2 = [4,5,6]
print(Solution().findSwapValues(array1, array2))