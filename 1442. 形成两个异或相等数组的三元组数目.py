from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:  
        res = 0
        pre_xor = [0]
        for num in arr:
            pre_xor.append(pre_xor[-1]^num)
        for i in range(len(arr)):
            for k in range(i+1,len(arr)):
                if pre_xor[i] == pre_xor[k+1]:
                    res += k-i
        return res
arr = [2,3,1,6,7]

arr = [1,1,1,1,1]

arr = [2,3]
print(Solution().countTriplets(arr))