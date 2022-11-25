from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) %k != 0:
            return False
        temp = []
        for num in arr:
            temp.append(num%k)
        temp.sort()
        left,right = 0,len(arr)-1
        while left<right and temp[left] == 0:
            left += 1
        while left < right:
            if temp[left]+temp[right] != k:
                return False
            left+=1
            right -= 1
        return True




arr = [-10,10]
k = 2
print(Solution().canArrange(arr, k))