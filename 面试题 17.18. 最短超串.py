from collections import Counter
from typing import List
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        if len(big) < len(small):
            return []
        counter = Counter(small)
        l = 0
        n = 0
        res = []
        for right in range(len(big)):
            if big[right] not in counter:
                continue
            counter[big[right]] -= 1
            if counter[big[right]] == 0:
                n += 1
            while  big[l] not in counter or counter[big[l]] < 0:
                if counter[big[l]] < 0:
                    counter[big[l]] += 1
                l += 1
            if n == len(small):
                if not res or right-l < res[1]-res[0]:
                    res = [l, right]
        return res
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
print(Solution().shortestSeq(big, small))
