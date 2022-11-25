from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0]+horizontalCuts+[h]
        horizontalCuts.sort()
        verticalCuts = [0]+verticalCuts+[w]
        verticalCuts.sort()
        h,v = [],[]
        for i in range(1,len(horizontalCuts)):
            h.append(horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            v.append(verticalCuts[i]-verticalCuts[i-1])
        res = 0
        for i in range(len(h)):
            for j in range(len(v)):
                res = max(res,h[i]*v[j])
        return res

h = 5
w = 4
horizontalCuts = [1, 2, 4]
verticalCuts = [1, 3]

h = 5
w = 4
horizontalCuts = [3,1]
verticalCuts = [1]
print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))