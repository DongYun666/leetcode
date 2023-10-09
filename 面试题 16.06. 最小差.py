from typing import List

class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        if len(a) == len(b) == 1:
            return abs(a[0] - b[0])
        m,n = len(a),len(b)
        i,j = 0,0
        res = float("inf")
        a.sort()
        b.sort()
        while i < m and j < n:
            if a[i] == b[j]:
                return 0
            diff = a[i] - b[j]
            res = min(abs(diff),res)
            if diff > 0:
                j += 1
            else:
                i += 1
        return res


a = [1,3,15,11,2]
b = [23,127,235,19,8]
print(Solution().smallestDifference(a, b))