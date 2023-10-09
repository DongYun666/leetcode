from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n = len(land),len(land[0])
        res = []
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and land[i][j] == 1:
                land[i][j] = 0
                nonlocal right,bottom
                right = max(right,j)
                bottom = max(bottom,i)
                for nx,ny in [(i+1,j),(i,j+1)]:
                    dfs(nx,ny)
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    right,bottom = 0,0
                    dfs(i,j)
                    res.append([i,j,bottom,right])
        return res
land = [[1,0,0],[0,1,1],[0,1,1]]
print(Solution().findFarmland(land))