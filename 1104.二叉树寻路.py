import math
from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = [label]
        layers = int(math.log2(label))+1
        for i in range(layers,1,-1):
            temp = 3*2**(i-2)-res[-1]//2-1
            res.append(temp)
        res.reverse()
        return res

label = 14
print(Solution().pathInZigZagTree(label))
