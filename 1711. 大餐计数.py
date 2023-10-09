from collections import Counter
from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        delic_dict = Counter(deliciousness)
        deliciousness = list(delic_dict.keys())
        res = 0
        for i in range(len(deliciousness)):
            for j in range(i,len(deliciousness)):
                temp = deliciousness[i]+deliciousness[j]
                if temp & (temp - 1) == 0:
                    if i != j:
                        res += delic_dict[deliciousness[i]]*delic_dict[deliciousness[j]]
                    elif delic_dict[deliciousness[i]] != 1:
                        res += delic_dict[deliciousness[i]]
        return res
deliciousness = [1, 1, 1, 3, 3, 3, 7]
print(Solution().countPairs(deliciousness))