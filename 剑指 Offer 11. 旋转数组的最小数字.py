from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        def binarySearch(numbers,left,right):
            while left < right:
                mid = (left + right) // 2
                if numbers[mid] > numbers[right]:
                    left = mid + 1
                elif numbers[mid] < numbers[right]:
                    right = mid
                else:
                    right -= 1
            return  numbers[left]
        return binarySearch(numbers,0,len(numbers)-1)

numbers = [3,4,5,1,2]
print(Solution().minArray(numbers))