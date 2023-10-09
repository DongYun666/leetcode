from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(b.count("X") for b in board)
        o_count = sum(b.count("O") for b in board)
        if x_count < o_count or x_count-o_count>1:
            return False
        board = [list(b) for b in board]
        #判断是谁赢了
        def Winner(x):
            if board[1][1] ==  board[0][0] == board[2][2] == x or board[1][1] ==  board[0][2] == board[2][0] == x:
                return True
            for b in board+list(map(list, zip(*board))):
                if b == [x]*3:
                    return True
            return False
        if Winner("X") and Winner("O"):
            return False
        elif Winner("X") and x_count-o_count != 1:
            return False
        elif Winner("O") and x_count != o_count:
            return False
        return True

board = ["XOX", "O O", "XOX"]
# board = ["O  ","   ","   "]
board = ["XXX","   ","OOO"]
board = ["XO ","XO ","XO "]
print(Solution().validTicTacToe(board))