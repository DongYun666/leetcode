from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        flag = False
        def dfs(pos):
            if pos == len(space):
                nonlocal flag
                flag = True
                return 
            i,j = space[pos]
            for num in range(9):
                if rows[i][num] == cols[j][num] == policy[i // 3][j // 3][num] == False:
                    rows[i][num] = cols[j][num] = policy[i // 3][j // 3][num] = True
                    board[i][j] = str(num + 1)
                    dfs(pos + 1)
                    rows[i][num] = cols[j][num] = policy[i // 3][j // 3][num] = False
                if flag:
                    return

        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        policy = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        space = [] 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    space.append((i,j))
                else:
                    index = int(board[i][j]) - 1
                    rows[i][index] = cols[j][index] = policy[i // 3][j // 3][index] = True
        dfs(0)
        return board

# board = [["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]] 
board = [[".",".",".",".","7","3",".","1","9"],
         ["3",".",".",".","1",".","2",".","."],
         [".","5",".",".",".","9",".",".","."],
         [".",".","9","4",".",".",".","5","."],
         [".",".",".",".",".",".","1",".","8"],
         [".","6","2",".","9",".",".",".","."],
         [".",".",".",".","5",".",".","8","."],
         [".","8",".","6",".",".",".",".","."],
         [".",".",".",".",".","4","9",".","7"]] 
print(Solution().solveSudoku(board))