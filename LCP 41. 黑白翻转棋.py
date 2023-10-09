from typing import List
class Solution:
    def flipChess(self, chessboard: List[str]) -> int:

        def judged(chessboard,i,j,dx,dy):
            x,y = i+dx,j+dy
            while 0<=x<len(chessboard) and 0<=y<len(chessboard[0]):
                if chessboard[x][y] == 'X':
                    return True
                elif chessboard[x][y] == '.':
                    return False
                x,y = x+dx,y+dy
            return False

        def bfs(chessboard,i,j):
            chessboard = [list(i) for i in chessboard]
            chessboard[i][j] = 'X'
            queue = [(i,j)]
            res = 0
            while queue:
                x,y = queue.pop(0)
                for dx,dy in [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]]:
                    if judged(chessboard,x,y,dx,dy):
                        nx,ny = x+dx,y+dy
                        while chessboard[nx][ny] != 'X':
                            queue.append((nx,ny))
                            chessboard[nx][ny] = 'X'
                            nx,ny = nx+dx,ny+dy
                            res += 1
            return res
        res = 0
        for i in range(len(chessboard)):
            for j in range(len(chessboard[0])):
                if chessboard[i][j] == '.':
                    res = max(res, bfs(chessboard,i,j))
        return res
    

chessboard = [".......",
              ".......",
              ".......",
              "X......",
              ".O.....",
              "..O....",
              "....OOX"]
print(Solution().flipChess(chessboard))