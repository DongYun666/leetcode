from typing import List
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for g in grid:
            g.sort()
        res = list(map(list, zip(*grid)))[::-1]
        for r in res:
            ans += max(r)
        return ans

grid = [[1,2,4],[3,3,1]]
print(Solution().deleteGreatestValue(grid))