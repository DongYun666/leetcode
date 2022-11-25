from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        def check(x):
            top_count = 0
            bottom_count = 0
            for i in range(len(tops)):
                if tops[i]!= x and bottoms[i]!= x:
                    return -1
                if tops[i] == x:
                    top_count+=1
                if bottoms[i] == x:
                    bottom_count+=1
            return min(n - top_count,n - bottom_count)
        res = check(tops[0])
        if res != -1 or tops[0] == bottoms[0]:
            return res
        else:
            return check(bottoms[0])


A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]

A = [3,5,1,2,3]
B = [3,6,3,3,4]
print(Solution().minDominoRotations(A,B))
