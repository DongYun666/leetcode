from typing import List
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i,j = len(arr1)-1,len(arr2)-1
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            temp = (arr1[i] if i>=0 else 0) + (arr2[j] if j >=0 else 0) + carry
            if temp >= 2:
                res.append(temp%2)
                carry = -1
            elif temp >= 0:
                res.append(temp)
                carry = 0
            elif temp == -1:
                res.append(1)
                carry = 1
            i-=1
            j-=1
        if carry == -1:
            res.append(1)
            res.append(1)
        elif carry == 1:
            res.append(1)
        res = res[::-1]
        while res[0] == 0:
            res.pop(0)
        return res
arr1 = [1,1,1,1,1]
arr1 = [1,0,1]
arr2 = [1,0,1]

arr1 = [1]
arr2 = [1,1,0,1]
print(Solution().addNegabinary(arr1, arr2))
  