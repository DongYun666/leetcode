from typing import List
from collections import deque
from heapq import heappop, heappush

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        DIR4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ROW, COL = len(grid), len(grid[0])
        values = [[0] * COL for _ in range(ROW)]
        queue = deque()
        visited = [[False] * COL for _ in range(ROW)]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited[r][c] = True

        while queue:
            len_ = len(queue)
            for _ in range(len_):
                curRow, curCol = queue.popleft()
                for dr, dc in DIR4:
                    newRow, newCol = curRow + dr, curCol + dc
                    if 0 <= newRow < ROW and 0 <= newCol < COL and not visited[newRow][newCol]:
                        values[newRow][newCol] = values[curRow][curCol] + 1
                        visited[newRow][newCol] = True
                        queue.append((newRow, newCol))
        print(values)
        pq = [(-values[0][0], 0, 0)]  # (safety, row, col)
        dist = [[0] * COL for _ in range(ROW)]
        dist[0][0] = values[0][0]
        while pq:
            safety, curRow, curCol = heappop(pq)
            safety = -safety
            if curRow == ROW - 1 and curCol == COL - 1:
                return safety
            for dr, dc in DIR4:
                newRow, newCol = curRow + dr, curCol + dc
                if 0 <= newRow < ROW and 0 <= newCol < COL:
                    newSafety = min(safety, values[newRow][newCol])
                    if newSafety > dist[newRow][newCol]:
                        dist[newRow][newCol] = newSafety
                        heappush(pq, (-newSafety, newRow, newCol))
        return 0


grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]

grid = [[0,0,1],[0,0,0],[0,0,0]]
print(Solution().maximumSafenessFactor(grid))