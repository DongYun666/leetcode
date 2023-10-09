from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        d = defaultdict(list)
        for i, size in enumerate(groupSizes):
            d[size].append(i)
        res = []

        for size, group in d.items():
            for i in range(0, len(group), size):
                res.append(group[i:i+size])
        return res
groupSizes = [3,3,3,3,3,1,3]
print(Solution().groupThePeople(groupSizes))