from collections import defaultdict
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        p,q = 0,0
        for x,y in zip(A,B):
            p |= (1<<x)
            q |= (1<<y)
            res.append(bin(p&q).count("1"))
        return res
A = [1,3,2,4]
B = [3,1,2,4]

# A = [2,3,1]
# B = [3,1,2]
print(Solution().findThePrefixCommonArray(A, B))