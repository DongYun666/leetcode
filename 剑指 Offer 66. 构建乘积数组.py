from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        L,R = [1]*len(a),[1]*len(a)
        for i in range(1,len(a)):
            L[i] = L[i-1]*a[i-1]
        for i in range(len(a)-2,-1,-1):
            R[i] = R[i+1]*a[i+1]
        return [L[i]*R[i] for i in range(len(a))]
a = [1,2,3,4,5]
print(Solution().constructArr(a))