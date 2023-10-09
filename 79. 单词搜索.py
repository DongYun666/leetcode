from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        def dfs(i,j,c):
            if c == len(word) - 1:
                return True
            visted[i][j] = True
            for x,y in [(i + 1, j),(i - 1, j),(i , j + 1),(i , j - 1)]:
                if 0 <= x < m and 0 <= y < n and not visted[x][y] and board[x][y] == word[c + 1]:
                    if dfs(x,y,c+1):
                        return True
            visted[i][j] = False
            return False
        visted = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(Solution().exist(board,word))