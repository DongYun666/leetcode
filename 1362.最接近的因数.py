import math
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def compute_de(n):
            for i in range(int(math.sqrt(n))+1,0,-1):
                if n%i == 0:
                    return [i,n//i]
        res = [0,float("inf")]
        for i in range(num+1,num+3):
            temp = compute_de(i)
            if temp[1]-temp[0] < res[1]-res[0]:
                res = temp
        return res

num = 999

# num = 123
print(Solution().closestDivisors(num))