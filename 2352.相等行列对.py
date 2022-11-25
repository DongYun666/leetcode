from collections import Counter, defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        re_grid = list(map(list, zip(*grid)))
        res = 0
        for r_g in re_grid:
            for  g in grid:
                if r_g == g:
                    res+=1
        return res





grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(Solution().equalPairs(grid))