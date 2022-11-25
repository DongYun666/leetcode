from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        #并查集
        n = len(grid)
        p = [i for i in range(n*n)]
        size = [1 for _ in range(n*n)]
        def find(x):
            if p[x]!=x:
                p[x] = find(p[x])
            return p[x]
        def union(a,b):
            pa,pb = find(a),find(b)
            if pa == pb:
                return
            p[pa] = pb
            size[pb]+=size[pa]
        #将所有的岛屿为1的进行合并
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for a,b in [[0,-1],[-1,0]]:
                        x,y = i+a,j+b
                        if 0<=x<n and 0<=y<n and grid[x][y]:
                            union(x*n+y,i*n+j)
        ans = max(size)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    vis = []
                    cur = 1
                    for a,b in [[0,1],[1,0],[0,-1],[-1,0]]:
                        x,y = i+a,j+b
                        if 0<=x<n and 0<=y<n and grid[x][y]:
                            root = find(x*n+y)
                            if root not in vis:
                                vis.append(root)
                                cur+=size[root]
                    ans = max(ans,cur)
        return ans







grid = [[1, 0], [0, 1]]
print(Solution().largestIsland(grid))