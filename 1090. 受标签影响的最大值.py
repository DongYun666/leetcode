from collections import Counter
from typing import List
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        v_l = zip(values,labels)
        v_l = sorted(v_l,key=lambda x:x[0],reverse=True)
        count = Counter()
        res = 0
        for v,l in v_l:
            if count[l] < useLimit:
                res += v
                count[l] += 1
                numWanted -= 1
            if numWanted == 0:
                break
        return res
        # print(v_l)
values = [5,4,3,2,1]
labels = [1,1,2,2,3]
numWanted = 3
useLimit = 1

values = [5,4,3,2,1]
labels = [1,3,3,3,2]
numWanted = 3
useLimit = 2
print(Solution().largestValsFromLabels(values,labels,numWanted,useLimit))