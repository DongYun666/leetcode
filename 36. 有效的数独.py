from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        policy = [[[0 for _ in range(9)]for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    index = ord(board[i][j]) - ord('1')
                    rows[i][index] += 1
                    cols[j][index] += 1
                    policy[i // 3][j // 3][index] += 1
                    if rows[i][index] > 1 or cols[j][index] > 1 or policy[i // 3][j // 3][index] > 1:
                        return False
        return True
    
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))