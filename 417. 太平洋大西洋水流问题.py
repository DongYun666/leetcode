from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        def search(starts):
            visited = set()
            def dfs(x,y):
                if (x,y) in visited:
                    return
                visited.add((x,y))
                for new_x,new_y in [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]:
                    if 0<=new_x<n and 0<=new_y<m and heights[new_x][new_y] >= heights[x][y]:
                        dfs(new_x,new_y)
            for x,y in starts:
                dfs(x,y)
            return visited
        def bfs(starts):
            q = starts
            visited = set(starts)
            while q:
                x,y = q.pop(0)
                for new_x, new_y in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                    if 0 <= new_x < n and 0 <= new_y < m and heights[new_x][new_y] >= heights[x][y] and (new_x,new_y) not in visited:
                        q.append((new_x,new_y))
                        visited.add((new_x,new_y))
            return visited
        pacific = [(0,i) for i in range(m)] + [(i,0) for i in range(1,n)]
        atlantic = [(n-1,i) for i in range(m)] + [(i,m-1) for i in range(n-1)]

        # return list(map(list,search(pacific) & search(atlantic)))
        return list(map(list,bfs(pacific) & bfs(atlantic)))
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(Solution().pacificAtlantic(heights))